#!/usr/bin/env python3.12

import numpy as np
import pennylane as qml

@qml.qnode(qml.device('default.qubit', wires=3))
def circuit():
	qml.X(wires=0)
	qml.CNOT(wires=[0, 2])
	qml.CNOT(wires=[2, 1])
	qml.Z(wires=1)
	qml.CRY(np.pi, wires=[1, 0])
	qml.Hadamard(wires = 0)
	return qml.probs(wires=[0])

print('Probs q_1:', circuit())
qml.drawer.use_style('black_white')
fig, ax = qml.draw_mpl(circuit)()

fig.savefig('question1.png')
