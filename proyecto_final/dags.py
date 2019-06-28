import numpy as np
import itertools
import networkx as nx
import scipy
import matplotlib.pyplot as plt

N = 5

def is_valid(x):
	for i in range(0, N):
		if x[i,i] == 1:
			return False
		for j in range(0,N):
			if	x[i,j] == x[j,i] and x[i,j] == 1:
				return False
	return True

x = [np.reshape(np.array(i), (N, N))
		for i in itertools.product([0, 1], repeat = N**2)]

x = [m for m in x if is_valid(m)]

A = [np.matrix(m) for m in x]

dags = [nx.from_numpy_matrix(a, create_using = nx.DiGraph()) for a in A]


dags = [dag for dag in dags if nx.is_directed_acyclic_graph(dag)]


adj_matrices = []
for G in dags:
	A = nx.adjacency_matrix(G)
	A = A.todense()
	adj_matrices.append(A)

print(adj_matrices)
