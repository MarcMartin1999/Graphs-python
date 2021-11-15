# Graphs-python
Some code to try to implement graphs in python. I recently studied Graph theory so i want to apply it to python
I created a class named Graph, this class allows to create graphs passing it vertices and adjacencies:
                            graph_a = Graph("1,2,3","1-2,2-3") 
                            graph_b = Graph("a,b,c","b-c,a-c")
Vertices will be csv and adjacencies will be csv too but separated the two vertices with "-".
I implemented the substraction of one graph with one of its subgraphs, and i implemented too the posibility to know if two 
graphs are isomorphs
