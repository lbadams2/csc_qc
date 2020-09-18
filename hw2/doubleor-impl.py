'''
Liam Adams - lbadams2
'''

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from dimod import ExactSolver
import sys


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


def hardcoded():
    Q = {('q1','q2'): 1, ('q1','q3'): 2, ('q2','q3'): 2, \
        ('q3','q4'): 1, ('q3','q5'): 2, ('q4','q5'): 2, ('q1','q1'): -1, ('q2','q2'): -1, \
            ('q3','q3'): -2, ('q4','q4'): -1, ('q5','q5'): -1}
    run_on_sim(Q)


def create_nor_qubo(num_gates):
    # if n=4 there will be 2 gates and an additional qubit for the output of the second gate
    Q = {}
    for i in range(num_gates + 1):
        i += 1 # start at 1
        qubit_name = 'q' + str(i)
        # every qubit should have -1 weight
        Q[(qubit_name, qubit_name)] = -1
        
        # inputs are 1, 2, 4, 6, ...
        # edges between inputs should be 1
        if i % 2 == 0:
            other_qubit = 'q' + str(i-1)
            Q[(qubit_name, other_qubit)] = 1

        # outputs will be 3, 5, ..., num_gates + 1
        # edges between inputs and outputs should be 2
        if i % 2 == 1 and i > 1: # odd qubit will have edges to previous 2 qubits
            other_qubit = 'q' + str(i-1)
            Q[(qubit_name, other_qubit)] = 2
            other_qubit = 'q' + str(i-2)
            Q[(qubit_name, other_qubit)] = 2

    run_on_sim(Q)


if __name__ == '__main__':
    #n = int(sys.argv[1])
    #create_nor_qubo(n)
    hardcoded()

'''
Output on hardware

{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0} Energy:  -2.0 Occurrences:  997
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -2.0 Occurrences:  1087
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -2.0 Occurrences:  234
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -2.0 Occurrences:  585
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -2.0 Occurrences:  204
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0} Energy:  -2.0 Occurrences:  617
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 0} Energy:  -2.0 Occurrences:  553
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0} Energy:  -2.0 Occurrences:  334
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0} Energy:  -2.0 Occurrences:  368
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0} Energy:  -2.0 Occurrences:  9
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -2.0 Occurrences:  1
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 0} Energy:  -1.0 Occurrences:  3
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 0} Energy:  -1.0 Occurrences:  1
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1} Energy:  1.0 Occurrences:  7
'''