#!/usr/bin/env python3.12

import numpy as np
import pennylane as qml

@qml.qnode(qml.device('lightning.qubit', wires=3))
def circuit():
	qml.Hadamard(wires = 0)
	qml.CNOT(wires=[0, 1])
	qml.RX(np.pi/3, wires = 1)
	qml.CSWAP(wires = [0, 1, 2])
	return qml.probs()

print('Probs q_1:', circuit())
qml.drawer.use_style('sketch')
fig, ax = qml.draw_mpl(circuit)()

fig.savefig('example2.png')
