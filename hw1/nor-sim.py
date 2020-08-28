'''
Liam Adams - lbadams2
'''

from dimod import ExactSolver

sampler = ExactSolver()
Q = {('q1','q2'): 1, ('q1','q3'): 2, ('q2','q3'): 2, ('q1','q1'): -1, ('q2','q2'): -1, ('q3','q3'): -1}
response = sampler.sample_qubo(Q)
for datum in response.data(['sample', 'energy']):
    print(datum.sample, 'Energy: ', datum.energy)

'''
Below 4 are correct outputs for q1 NOR q2 = q3 with lowest energy state
{'q1': 1, 'q2': 0, 'q3': 0} Energy:  -1.0
{'q1': 1, 'q2': 1, 'q3': 0} Energy:  -1.0
{'q1': 0, 'q2': 1, 'q3': 0} Energy:  -1.0
{'q1': 0, 'q2': 0, 'q3': 1} Energy:  -1.0

Below 4 are incorrect with higher energy
{'q1': 0, 'q2': 0, 'q3': 0} Energy:  0.0
{'q1': 0, 'q2': 1, 'q3': 1} Energy:  0.0
{'q1': 1, 'q2': 0, 'q3': 1} Energy:  0.0
{'q1': 1, 'q2': 1, 'q3': 1} Energy:  2.0
'''