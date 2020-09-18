'''
Liam Adams - lbadams2
'''

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from dimod import ExactSolver

def run_on_hw(Q):
    sampler = DWaveSampler()
    sampler_embedded = EmbeddingComposite(sampler)
    response = sampler_embedded.sample_qubo(Q, num_reads=5000)
    for datum in response.data(['sample', 'energy', 'num_occurrences']):   
        print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)

def run_on_sim(Q):
    sampler = ExactSolver()
    response = sampler.sample_qubo(Q)
    for datum in response.data(['sample', 'energy', 'num_occurrences']):
        print(datum.sample, 'Energy: ', datum.energy, "Occurrences: ", datum.num_occurrences)


def get_nor_qubo(qub_in_1, qub_in_2, qub_out):
    qubo = {}
    qubo[(qub_in_1, qub_in_1)] = -1
    qubo[(qub_in_2, qub_in_2)] = -1
    qubo[(qub_out, qub_out)] = -1
    qubo[(qub_in_1, qub_in_2)] = 1
    qubo[(qub_in_1, qub_out)] = 2
    qubo[(qub_in_2, qub_out)] = 2
    return qubo


def duplicate_qubit(qubo, qubit_name, dup_qubit_name):
    couple_weight = -2
    qubit_weight = qubo[qubit_name]
    split_weight = qubit_weight / 2 + (-1*(.5 * couple_weight))
    qubo[qubit_name] = split_weight
    qubo[(dup_qubit_name, dup_qubit_name)] = split_weight
    qubo[qubit_name, dup_qubit_name] = couple_weight


def run():
    Q = {}
    first_gate = get_nor_qubo('q1', 'q2', 'q3')
    Q.update(first_gate)

    # duplicate q1 to q4
    duplicate_qubit(Q, 'q1', 'q4')

    # duplicate q2 to q5
    duplicate_qubit(Q, 'q2', 'q5')

    # duplicate q3 to q6
    duplicate_qubit(Q, 'q3', 'q6')

    # q4 NOR q3 = q7
    second_gate = get_nor_qubo('q3', 'q4', 'q7')




def run_hardcoded():
    Q = {('q1','q1'): -2, ('q2','q2'): -2, ('q3','q3'): -3, ('q4','q4'): -1, ('q5','q5'): -2, ('q6','q6'): -1, ('q7','q7'): -1, \
        ('q8','q8'): -2, ('q1','q1'): -2, ('q1','q2'): 1, ('q1','q3'): 4, ('q1','q4'): 2, ('q2','q3'): 3, ('q2','q4'): -1, \
            ('q2','q5'): 2, ('q3','q4'): 1, ('q3','q5'): 2, ('q4','q5'): 1, ('q4','q6'): 2, ('q4','q7'): 1, ('q5','q6'): 2, \
            ('q5','q7'): 1, ('q6','q8'): 2, ('q7','q8'): 2}

    '''
    Q = {('q1','q1'): .5, ('q2','q2'): .5, ('q3','q3'): -.5, ('q4','q4'): -.5, ('q5','q5'): -.5, ('q6','q6'): -.5, ('q7','q7'): -2, \
        ('q8','q8'): -2, ('q1','q2'): 1, ('q1','q3'): 2, ('q2','q3'): 2, ('q1','q4'): -2, ('q2','q5'): -2, ('q3','q6'): -2, \
            ('q3','q4'): 1, ('q3','q7'): 2, ('q4','q7'): 2, ('q5','q6'): 1, ('q5','q8'): 2, ('q6','q8'): 2, ('q9','q9'): -.5, \
                ('q10','q10'): -.5, ('q11','q11'): -1, ('q9','q10'): 1, ('q9','q11'): 2, ('q10','q11'): 2, ('q7','q8'): 1, \
                    ('q7','q9'): 2, ('q8','q9'): 2, ('q9','q10'): -2}
    '''

    run_on_hw(Q)


if __name__ == "__main__":
    run_hardcoded()


'''
Output from hardware
q1 XOR q2 = q8

{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -6.0 Occurrences:  3156
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -6.0 Occurrences:  1794
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -5.0 Occurrences:  14
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -5.0 Occurrences:  2
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 0, 'q6': 1, 'q7': 1, 'q8': 0} Energy:  -5.0 Occurrences:  2
{'q1': 0, 'q2': 1, 'q3': 1, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -5.0 Occurrences:  1
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -5.0 Occurrences:  6
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 1, 'q7': 1, 'q8': 0} Energy:  -5.0 Occurrences:  17
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -5.0 Occurrences:  1
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -5.0 Occurrences:  4
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 1, 'q8': 1} Energy:  -4.0 Occurrences:  2
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -4.0 Occurrences:  1
'''