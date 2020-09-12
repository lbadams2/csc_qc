import dimod
from dwavebinarycsp.core.constraint import Constraint
from dwavebinarycsp.core.csp import ConstraintSatisfactionProblem
from dwavebinarycsp import stitch
import neal

@dimod.decorators.vartype_argument('vartype')
def nor_gate(variables, vartype=dimod.BINARY, name='NOR'):
    """NOR gate.

    Args:
        variables (list): Variable labels for the and gate as `[in1, in2, out]`,
            where `in1, in2` are inputs and `out` the gate's output.
        vartype (Vartype, optional, default='BINARY'): Variable type. Accepted
            input values:

            * Vartype.SPIN, 'SPIN', {-1, 1}
            * Vartype.BINARY, 'BINARY', {0, 1}
        name (str, optional, default='NOR'): Name for the constraint.

    Returns:
        Constraint(:obj:`.Constraint`): Constraint that is satisfied when its variables are
        assigned values that match the valid states of an NOR gate.

    Examples:
        >>> import dwavebinarycsp.factories.constraint.gates as gates
        >>> csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.SPIN)
        >>> csp.add_constraint(gates.nor_gate(['x', 'y', 'z'], {-1,1}, name='NOR1'))
        >>> csp.check({'x': 1, 'y': -1, 'z': -1})
        True
    """

    variables = tuple(variables)

    if vartype is dimod.BINARY:
        configs = frozenset([(0, 0, 1),
                             (0, 1, 0),
                             (1, 0, 0),
                             (1, 1, 0)])

        def func(in1, in2, out): return ((not in1) and (not in2)) == out

    else:
        # SPIN, vartype is checked by the decorator
        configs = frozenset([(-1, -1, +1),
                             (-1, +1, -1),
                             (+1, -1, -1),
                             (+1, +1, -1)])

        def func(in1, in2, out): return ((in1 < 0) and (in2 < 0)) == (out > 0)

    return Constraint(func, configs, variables, vartype=vartype, name=name)



def xor_circuit(vartype=dimod.BINARY):
    # also checks the vartype argument
    csp = ConstraintSatisfactionProblem(vartype)

    gate = nor_gate(['in1', 'in2', 'out1'], vartype=vartype, name='NOR(in1, in2) = out1')
    csp.add_constraint(gate)

    gate = nor_gate(['in1', 'out1', 'out2'], vartype=vartype, name='NOR(in1, out1) = out2')
    csp.add_constraint(gate)

    gate = nor_gate(['in2', 'out1', 'out3'], vartype=vartype, name='NOR(in2, out1) = out3')
    csp.add_constraint(gate)

    gate = nor_gate(['out2', 'out3', 'out4'], vartype=vartype, name='NOR(out2, out3) = out4')
    csp.add_constraint(gate)

    gate = nor_gate(['out4', 'out4', 'out5'], vartype=vartype, name='NOR(out4, out4) = out5')
    csp.add_constraint(gate)

    return csp


def main():
    csp = xor_circuit()
    bqm = stitch(csp)
    bqm.fix_variable('in1', 1)
    bqm.fix_variable('in2', 0)
    sampler = neal.SimulatedAnnealingSampler()
    response = sampler.sample(bqm)
    p = next(response.samples(n=1, sorted_by='energy'))
    print(p)


if __name__ == '__main__':
    main()