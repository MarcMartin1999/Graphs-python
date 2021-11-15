import Adjacencie as ad
class Graph:
    #Nodes will be passed like "1,2,3,4" and connections like "1-2,2-3,4-4"
    def __init__(self,vertices:str,adjacencies:str):

        vertex_list = vertices.split(",") 
        adjacencies_list = adjacencies.split(",")

        #Search for vertices Errors
        for i,vertex in enumerate(vertex_list):
            auxList = vertex_list.copy()
            auxList.pop(i)
            if vertex in auxList:
                raise Exception("Node Error: Repeated nodes")
        #Search for adjacencies Errors
        aux_adjacencies = []
        for adjacencie in adjacencies_list:
            adj = ad.adjacencie.from_string(adjacencie)
            if adj.a and adj.b not in vertex_list:
                raise Exception("Adjacencies Error: Node not Exist")
            elif adj.a == adj.b:
                raise Exception("Adjacencies Error: Not graph")
            aux_adjacencies.append(adj)
        
        self.vertices = vertex_list
        self.adjacencies = aux_adjacencies
    #Returns a new graph with the same values than self
    def copy(self):
        
        copied_graph = Graph(','.join(self.vertices),','.join(self.adjacencies_string_list))
        return copied_graph
    def __str__(self) -> str:
        str_ret = "--Vertices: " + str(self.vertices)+ "\n" + "--Adjacencies: "+ str(self.adjacencies_string_list)
        return str_ret
    #order's graph is the number of vertices that has
    @property
    def order(self):
        return len(self.vertices)
    #length's graph is the number of adjacencies that has
    @property
    def length(self):
        return len(self.adjacencies)

    #Returns the adjacencies in a list of strings
    @property
    def adjacencies_string_list(self):
        adj_str = []
        for adj in self.adjacencies:
            adj_str.append(adj.to_string)
        return adj_str
    #Returns complementary's graph
    @property
    def complementary(self):
        return self.complete(self.order)-self 
    #Returns the degree of a vertex
    def vertex_degree(self,vertex):
        degree = 0
        for adj in self.adjacencies_string_list:
            if vertex in adj.split("-"):
                degree += 1 
        return degree

    #Returns true if the actual graph has an isomorphism with the other graph
    def isomorph(self,other:object):
        if other.__class__ != self.__class__: raise Exception("Isomorph Error: only isomorphism with graphs")

        if not self.__invariants(other): #If some invariant its not true then return false
            return False
        
        return self.__search_aplication(other) #If all invariants all true, will search some aplication with vertices and adjacencies
        
    #subtract operation only with graphs and its subgraphs
    def __sub__(self,other):
        for v in other.vertices:
            if v not in self.vertices:
                raise Exception("Aritmetic error: subgraph not correct")
        
        self_copy = self.copy()
        for adj in self.adjacencies:
            for adj2 in  other.adjacencies:
                if adj == adj2:
                    self_copy.adjacencies.remove(adj)
        
        return self_copy

    def __add__(self,other):
        raise Warning("Addition not implemented")

    #returns a n-complete graph
    @staticmethod
    def complete(n:int):
        n_vertices = []
        for i in range(n):
            n_vertices.append(str(i+1))
        
        n_vertices2 = n_vertices.copy()
        l_adj = []
        for v in n_vertices:
            n_vertices2.remove(v)
            for v2 in n_vertices2:
                l_adj.append(ad.adjacencie(v,v2).to_string)


        return Graph(",".join(n_vertices),",".join(l_adj))
    #Private methods
    def __invariants(self,other):
        if self.order != other.order or self.length != other.length:
            return False
        
        aux_b_vertices = other.copy().vertices
        for v in self.vertices:
            v_degree = self.vertex_degree(v)
            for v2 in aux_b_vertices:
                v2_degree = other.vertex_degree(v2)
                if v_degree == v2_degree:
                    aux_b_vertices.remove(v2)
        return  len(aux_b_vertices) == 0

 

    def __search_aplication(self,other):
            
        posible_isomorphs = self.__search_posible_isomorphs(other)
        
        for v in posible_isomorphs[0]: 

            iso2 = posible_isomorphs[1:]
            aux =  self.adjacencies_string_list.copy()

            for i,adj in enumerate(aux):
                aux[i]=adj.replace(self.vertices[0],v)
          
            v_used = [v]
            v_used2 = []

            for l in iso2:
                v_used2.append([])
            
            copyAdj = self.copy().adjacencies
            for i,l in enumerate(iso2):
                for v2 in l:
                    if v2 not in v_used and v2 not in v_used2[i]:
                        v_used.append(v2)
                        v_used2[i].append(v2)
                        print
                        for j,adj in enumerate(aux):
                            aux[j]=adj.replace(self.vertices[i+1],v2)
                        break
                        
            
            if(self.__same_adjacencies(aux,other.adjacencies_string_list)): 
                print(aux)
                return True
                

        return False

    def __search_posible_isomorphs(self,other):
        aux_b_vertices = other.copy().vertices
        posible_isomorphs = []
        for v in self.vertices:
            posible_isomorphs.append([])

        for i,v in enumerate(self.vertices):
            v_degree = self.vertex_degree(v)
            for v2 in aux_b_vertices:
                v2_degree = other.vertex_degree(v2)
                if v_degree == v2_degree and v2 not in posible_isomorphs[i]:
                    posible_isomorphs[i].append(v2)
        return posible_isomorphs

    def __same_adjacencies(self,str1,str2)-> bool:
        adj_list1 = []
        adj_list2 = []
        
        for adj1 in str1:
            adj_list1.append(ad.adjacencie.from_string(adj1))
        
        for adj2 in str2:
            adj_list2.append(ad.adjacencie.from_string(adj2))
        
        for adj1 in adj_list1:
          for adj2 in adj_list2:
              if adj1 == adj2:
                  adj_list2.remove(adj2)
                  break 
        
       
        return len(adj_list2) == 0


        






