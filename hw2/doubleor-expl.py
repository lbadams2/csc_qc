'''
Liam Adams - lbadams2
'''

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import FixedEmbeddingComposite
embedding = {'q1': {0}, 'q2': {4}, 'q3': {1}, 'q4': {2}, 'q5': {3}, 'q6': {5}, 'q7': {6}}
sampler = DWaveSampler()
sampler_embedded = FixedEmbeddingComposite(sampler, embedding)
Q = {('q1','q2'): 1, ('q1','q6'): 2, ('q2','q3'): 2, ('q4','q6'): 1, ('q5','q6'): 2, \
    ('q4','q7'): 2, ('q3','q6'): -2, ('q5','q7'): -2, ('q1','q1'): -1, ('q2','q2'): -1, \
        ('q3','q3'): .5, ('q4','q4'): -1, ('q5','q5'): .5, ('q6','q6'): .5, ('q7','q7'): .5}
response = sampler_embedded.sample_qubo(Q, num_reads=5000)
for datum in response.data(['sample', 'energy', 'num_occurrences']):   
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)


'''
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 1} Energy:  -2.0 Occurrences:  647
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 1} Energy:  -2.0 Occurrences:  316
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 0} Energy:  -2.0 Occurrences:  1362
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 0} Energy:  -2.0 Occurrences:  1319
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 1} Energy:  -2.0 Occurrences:  838
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 0} Energy:  -2.0 Occurrences:  518
'''