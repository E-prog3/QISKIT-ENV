import numpy as np

from qiskit import IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
from qiskit import QuantumCircuit, execute
from qiskit.tools.jupyter import *
IBMQ.save_account('c44fda755ee32da1671773d72a62194485b231bc6a279e2b332fcf0d567d0b1a0c8f11455b32ca6cfc7ff7c581c5c08701a5f2b1c93911a0eb8a80e5a7369a31')
provider = IBMQ.load_account()
from qiskit.visualization import plot_histogram


def dj_oracle(case, n):
    oracle_qc = QuantumCircuit(n+1)
    if case == 'Balanced':
        for qubit in range(n):
            oracle_qc.cx(qubit, n)

    if case == 'Constant':
        output = np.random.randint(2)
        if output == 1:
            oracle_qc.x(n)

    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = 'Oracle'
    return oracle_gate


def dj_algo(n, case = 'Random'):
    dj_circuit = QuantumCircuit(n+1, n)

    for qubit in range(n):
        dj_circuit.h(qubit)
    dj_circuit.x(n)
    dj_circuit.h(n)

    if case == 'Random':
        random = np.random.randint(2)
        if random == 0:
            case = 'Constant'
        else:
            case = 'Balanced'

    oracle = dj_oracle(case, n)
    dj_circuit.append(oracle, range(n+1))

    for i in range(n):
        dj_circuit.h(i)
        dj_circuit.measure(i, i)
    return dj_circuit

print('Dutche-Joza Algo')
