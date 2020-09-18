'''
Liam Adams - lbadams2
'''

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import FixedEmbeddingComposite
from dimod import ExactSolver


def run_on_hw(Q, embedding):
    sampler = DWaveSampler()
    sampler_embedded = FixedEmbeddingComposite(sampler, embedding)
    response = sampler_embedded.sample_qubo(Q, num_reads=5000)
    for datum in response.data(['sample', 'energy', 'num_occurrences']):   
        print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)

def run_on_sim(Q, embedding):
    sampler = ExactSolver()
    sampler_embedded = FixedEmbeddingComposite(sampler, embedding)
    response = sampler_embedded.sample_qubo(Q)
    for datum in response.data(['sample', 'energy', 'num_occurrences']):
        print(datum.sample, 'Energy: ', datum.energy, "Occurrences: ", datum.num_occurrences)


def run():
    embedding = {'q1': {0}, 'q2': {4}, 'q3': {5}, 'q4': {1}, 'q5': {7}, 'q6': {6}, 'q7': {2}}
    Q = {('q1','q2'): 1, ('q1','q3'): 2, ('q2','q4'): 2, ('q3','q4'): -2, ('q4','q5'): 1, \
        ('q4','q6'): 2, ('q5','q7'): 2, ('q1','q1'): -1, ('q2','q2'): -1, ('q3','q3'): .5, \
            ('q4','q4'): -.5, ('q5','q5'): -1, ('q6','q6'): .5, ('q7','q7'): .5}
    run_on_hw(Q, embedding) 


if __name__ == "__main__":
    run()

'''
Output from hardware
q3 and q4 are coupled, they are the output from q1 NOR q2
q6 and q7 are coupled, they are the output from q4 NOR q5

{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0} Energy:  -2.0 Occurrences:  763
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0} Energy:  -2.0 Occurrences:  366
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0} Energy:  -2.0 Occurrences:  916
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 1, 'q6': 0, 'q7': 0} Energy:  -2.0 Occurrences:  1000
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 0} Energy:  -2.0 Occurrences:  1949
{'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0} Energy:  -1.5 Occurrences:  1
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 1} Energy:  -1.5 Occurrences:  2
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 1, 'q6': 0, 'q7': 0} Energy:  -1.5 Occurrences:  2
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 1, 'q7': 0} Energy:  -1.5 Occurrences:  1
'''