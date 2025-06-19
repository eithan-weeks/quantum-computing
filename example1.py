#!/usr/bin/env python3.12

import pennylane as qml

@qml.qnode(qml.device('lightning.qubit', wires=2))
def circuit():
	qml.Hadamard(wires = 0)
	qml.CNOT(wires=[0, 1])
	return qml.probs()

print('Probs q_1:', circuit())
qml.drawer.use_style('black_white')
fig, ax = qml.draw_mpl(circuit)()

fig.savefig('example1.png')
