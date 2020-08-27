from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)
Q = {('q1','q2'): 1, ('q1','q3'): 2, ('q2','q4'): 2, ('q3','q4'): -2, ('q1','q1'): -1, ('q2','q2'): -1, ('q3','q3'): .5, ('q3','q3'): .5}
response = sampler_embedded.sample_qubo(Q, num_reads=5000)
for datum in response.data(['sample', 'energy', 'num_occurrences']):   
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)


'''
Correct
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 1} Energy:  -1.5 Occurrences:  4788
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0} Energy:  -1.0 Occurrences:  68
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0} Energy:  -1.0 Occurrences:  50
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0} Energy:  -1.0 Occurrences:  59

Incorrect
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1} Energy:  -1.0 Occurrences:  34
{'q1': 1, 'q2': 0, 'q3': 1, 'q4': 1} Energy:  -0.5 Occurrences:  1
'''