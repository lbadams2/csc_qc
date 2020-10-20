# Adapted from a qiskit notebook

from qiskit import Aer, QuantumCircuit, execute

def dotprod(a, b):
    temp_sum = 0
    for i in range(len(a)):
        temp_sum += int(a[i])*int(b[i])
    return temp_sum%2

def oracle(circ, b):
    # TODO generalize this function
    for i, char in enumerate(b):
        circ.cx(i, i+len(b))

    circ.cx(1, 4)
    circ.cx(1, 5)

# Main function
b = '110'
n = len(b)
circ = QuantumCircuit(n*2, n)

circ.h(range(n))
circ.barrier()
oracle(circ, b)
circ.barrier()
circ.h(range(n))

circ.measure(range(n), range(n))
print(circ)

backend = Aer.get_backend('qasm_simulator')
shots = 1024
job = execute(circ, backend=backend, shots=shots)
results = job.result()
counts = results.get_counts()

for code in counts:
    print("(" + str(b) + " dot " + str(code) + ")%2 = " + str(dotprod(b, code)))
