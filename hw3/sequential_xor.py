from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import Aer, execute
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt

# Quantum XOR - really just CNOT
# input qubits: a, b
# output qubits: b 
def qxor(circ, a, b):
    circ.cx(a, b)


'''
a XOR b XOR c will be 1 if:
a XOR b = 0 and c = 1
a XOR b = 1 and c = 0
'''
def create_xor_seq(n):
    a = QuantumRegister(n, 'in')  # input
    qc = QuantumCircuit(a)

    # Build a circuit that initializes the input bits to a full superposition
    # Calls the XOR function and then measures the output register

    qc.h(a) # puts hadamard on all qubits in register
    # barrier will prevent transpile (called by execute) to restrict optimizations between barriers 
    # and not entire circuit, won't combine gates and make optimizations across barriers
    qc.barrier()

    for i in range(n - 1):
        qxor(qc, a[i], a[i+1])
        
    qc.barrier()
    m = ClassicalRegister(1, 'output')
    qc.add_register(m)
    qc.measure(a[n-1], m)

    return qc


if __name__ == '__main__':
    qc = create_xor_seq(13)

    # Simulate and show results
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=4096)  # shots default = 1024
    result = job.result()
    print(result.get_counts())
    
    qc.draw(output='mpl')
    plot_histogram(result.get_counts()) # output is just the second qubit activated/inactivated by CNOT
    plt.show()