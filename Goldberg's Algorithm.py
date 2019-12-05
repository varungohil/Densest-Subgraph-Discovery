# #####################################################
#   Authors  #  Varun Gohil (gohil.varun@iitgn.ac.in) #
#######################################################
import maxflow
import time

def Find_Density(answer):
        ''' Finds the density of the returned subgraph.'''
        degree = 0
        file = open("edges.txt","r")
        while True:
                edge = file.readline()
                #print "Reading an edge"
                if not edge:
                        break
                from_node, to_node = edge.split()
                if(int(from_node) in answer and int(to_node) in answer):
                        degree += 2
        print degree/(2.0*(len(answer)))


def Find_Densest_Subgraph(number_of_nodes,number_of_edges):
        ''' This function performs the binary search of the density of subgraph and finds the densest subgraph.''' 
        min_degree = 0
        max_degree = number_of_edges
        subgraph = []
        difference = 1.0/(number_of_nodes*(number_of_nodes - 1))
        #print difference, " diff"
        while(max_degree - min_degree >= difference):
                print "Algo at work!"
                #print "max - min = ", max_degree - min_degree
                least_density = (max_degree + min_degree)/2.0
                #print "ld--->", least_density 
                source_segment = make_graph(number_of_nodes, number_of_edges, least_density)
                if(source_segment == []):
                        max_degree = least_density
                else:
                        min_degree = least_density
                        subgraph = source_segment
                #print subgraph
        return subgraph


def make_graph(number_of_nodes, number_of_edges, least_density):
        ''' Constructs the network as per the specifications given by Goldberg'''
        graph = maxflow.Graph[float](number_of_nodes, number_of_edges)
        nodes = graph.add_nodes(number_of_nodes)
        #print nodes
        degrees = {}
        #print degrees
        file = open("edges.txt","r")
        while True:
                edge = file.readline()
                if not edge:
                        break
                from_node, to_node = edge.split()
                #print edge.split()
                graph.add_edge(nodes[int(from_node)], nodes[int(to_node)], 1,1)
                if from_node in degrees:
                        degrees[from_node] += 1
                else:
                        degrees[from_node] = 1
                if to_node in degrees:
                        degrees[to_node] += 1
                else:
                        degrees[to_node] = 1
        file.close()
        for i in range(number_of_nodes):
                if str(i) not in degrees:
                        degrees[str(i)] = 0
                graph.add_tedge(nodes[i], number_of_edges, number_of_edges + 2*least_density - degrees[str(i)])
                #print "s -- ",number_of_edges,"-->", nodes[i], "--",number_of_edges + 2*least_density - degrees[str(i)], "-->t\n"  
        source_segment = []
        '''Computes the max-flow in the graph'''
        graph.maxflow()
        '''The following section of code finds which node belongs to which cutset.'''
        for i in nodes:
                #print nodes[i] ,"--->", graph.get_segment(nodes[i])
                if(graph.get_segment(nodes[i]) == 0):
                        source_segment.append(nodes[i])
        #print degrees
        return source_segment




number_of_nodes = int(raw_input("Enter number of nodes: ")) + 1
number_of_edges = int(raw_input("Enter number of edges: "))

start_time = time.clock()
answer = Find_Densest_Subgraph(number_of_nodes, number_of_edges)
print time.clock() - start_time
print answer
Find_Density(answer)

