'''
Liam Adams - lbadams2
'''

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)
Q = {('q1','q2'): 1, ('q1','q3'): 1, ('q1','q4'): 1, ('q1','q5'): 50, ('q2','q3'): 1, ('q2','q4'): 1, ('q2','q5'): 50, \
    ('q3','q4'): -2, ('q3','q5'): 50, ('q4','q5'): 50, ('q1','q1'): -2, ('q2','q2'): -2, \
        ('q3','q3'): -2, ('q4','q4'): -2, ('q5','q5'): -2}
response = sampler_embedded.sample_qubo(Q, num_reads=5000)
for datum in response.data(['sample', 'energy', 'num_occurrences']):   
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)