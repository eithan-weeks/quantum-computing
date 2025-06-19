#!/usr/bin/env python3.12

import numpy as np
import pennylane as qml

@qml.qnode(qml.device('default.qubit', wires=3))
def circuit():
	qml.RX(np.pi/3, wires = 0)
	qml.CNOT(wires=[0, 1])
	qml.Hadamard(wires = 1)
	qml.CNOT(wires=[1, 2])
	qml.Hadamard(wires = 2)
	return qml.probs()

print('Probs q_1:', circuit())
qml.drawer.use_style('black_white')
fig, ax = qml.draw_mpl(circuit)()

fig.savefig('example3.png')
