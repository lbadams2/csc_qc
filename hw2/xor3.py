'''
Liam Adams - lbadams2
'''

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = DWaveSampler()
sampler_embedded = EmbeddingComposite(sampler)

Q = {('q1','q2'): 1, ('q1','q3'): 2, ('q2','q3'): 2, ('q1','q1'): -1, ('q2','q2'): -1, ('q3','q3'): -1, # q1 NOR q2 = q3
     ('q1','q3'): 1, ('q1','q4'): 2, ('q3','q4'): 2, ('q4','q4'): -1, # q1 NOR q3 = q4
     ('q2','q3'): 1, ('q2','q5'): 2, ('q3','q5'): 2, ('q5','q5'): -1, # q2 NOR q3 = q5
     ('q4','q5'): 1, ('q4','q6'): 2, ('q5','q6'): 2,  # q4 NOR q5 = q6
    # above valid except missing (q6,q6): -1

    # duplicate q6
     #('q6','q7'): -2, ('q6','q6'): .5, ('q7','q7'): .5,
     ('q6','q6'): .5, ('q7','q7'): .5,
    
    # combine duplicate weights with NOR weights (q6,q7): -2 + (q6,q7): 1
     ('q6','q7'): -1, ('q6','q8'): 2, ('q7','q8'): 2, ('q8','q8'): -1, # q6 NOR q7 = q8
    }

response = sampler_embedded.sample_qubo(Q, num_reads=5000)
for datum in response.data(['sample', 'energy', 'num_occurrences']):   
  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)



'''
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -3.0 Occurrences:  2049
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -3.0 Occurrences:  2869
{'q1': 0, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -2.0 Occurrences:  15
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -2.0 Occurrences:  7
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 0} Energy:  -2.0 Occurrences:  2
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -2.0 Occurrences:  9
{'q1': 0, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -2.0 Occurrences:  2
{'q1': 1, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -2.0 Occurrences:  13
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0, 'q8': 0} Energy:  -2.0 Occurrences:  4
{'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -2.0 Occurrences:  14
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -2.0 Occurrences:  9
{'q1': 0, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 1, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -2.0 Occurrences:  1
{'q1': 1, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -1.0 Occurrences:  1
{'q1': 0, 'q2': 1, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 1, 'q7': 1, 'q8': 0} Energy:  -1.0 Occurrences:  1
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 1, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -1.0 Occurrences:  1
{'q1': 1, 'q2': 0, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 1, 'q7': 1, 'q8': 0} Energy:  -1.0 Occurrences:  1
{'q1': 0, 'q2': 1, 'q3': 0, 'q4': 0, 'q5': 0, 'q6': 1, 'q7': 1, 'q8': 0} Energy:  -1.0 Occurrences:  1
{'q1': 1, 'q2': 0, 'q3': 0, 'q4': 1, 'q5': 0, 'q6': 0, 'q7': 0, 'q8': 1} Energy:  -1.0 Occurrences:  1
'''