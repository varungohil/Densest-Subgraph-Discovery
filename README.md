# Densest-Subgraph-Discovery
This repository contains python programs for finding the densest subgraph in a undirected graph.

### Notion of Density
Here the density of a graph refers to the ratio of the number of edges between the nodes of the graph and the number of nodes of the graph.

### Implemented Algorithms 
The repo consists of the following algorithms:
- Goldberg's Algorithm
- Charikar's greedy 2 approximation algorithm 

### Usage Methodology
For running the programs you will need to install [PyMaxflow library](https://github.com/pmneila/PyMaxflow).

Before running any programs copy the set of edges in the edges.txt file(only the set of edges, no extra information).
After that run the program and input the number of nodes and edges as requested.

The programs have been written in Python 2.7 but can be run with Python 3 with minors alterations.

### Output
The program returns a python list of the nodes that are in the densest subgraph and the density of the subgraph.
