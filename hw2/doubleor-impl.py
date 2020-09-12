'''
Liam Adams - lbadams2
'''

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)
Q = {('q1','q2'): 1, ('q1','q3'): 2, ('q1','q4'): 0, ('q1','q5'): 0, ('q2','q3'): 2, ('q2','q4'): 0, ('q2','q5'): 0, \
    ('q3','q4'): 1, ('q3','q5'): 2, ('q4','q5'): 2, ('q1','q1'): -1, ('q2','q2'): -1, \
        ('q3','q3'): -1, ('q4','q4'): -1, ('q5','q5'): -1}
response = sampler_embedded.sample_qubo(Q, num_reads=5000)
for datum in response.data(['sample', 'energy', 'num_occurrences']):   
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)



'''
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -2.0 Occurrences:  1211
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0} Energy:  -2.0 Occurrences:  564
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0} Energy:  -2.0 Occurrences:  898
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -2.0 Occurrences:  843
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 0} Energy:  -2.0 Occurrences:  673
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 1} Energy:  -2.0 Occurrences:  805
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 1} Energy:  -1.0 Occurrences:  1
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0} Energy:  -1.0 Occurrences:  4
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 1} Energy:  0.0 Occurrences:  1
'''