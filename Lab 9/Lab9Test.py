#Syed Yasoob Ali
#500953533
#Lab 9, Some assistance recieved from W3Schools website

class MinimumSpanningTree:
      
      road = [[]]        
      infinit = 88
      nodes = -1
      S = []
      T = []
      cost = 0
      output = [] 

      def __init__(self):
          self.readGraph('minspantree.in')

      def getCost(self):
          return self.cost
      
      def solution(self, n):

          self.draw(n)
          f = open('minspantree.out','w')
          out = "Minimum cost = " + str(self.cost) + "\n"
          out += "Minimum Spanning Tree from 1 to {} => {}". format(n, str(self.output))
          f.write(out) 
          f.close()
          return self.output
           
     
      def draw(self,node): 

          if self.T[ node ] != 0:
             self.draw( self.T[ node ] )
          self.output.append(node) 

      def solve(self):
          self.S = [ 0 ] * (self.nodes + 1)
          self.T = [ 0 ] * (self.nodes + 1)
          r = 1
          self.S[ r ] = 0

          for i in range(1,self.nodes+1):
              if i != r:
                 self.S[i] = r

          self.cost = 0 

          for i in range(1, self.nodes):
              min = self.infinit

              for j in range(1,self.nodes+1):
                  if self.S[ j ] != 0:
                     if self.road[ self.S[ j ] ][ j ] < min:
                        min = self.road[ self.S[ j ] ][ j ]
                        pos = j

              self.cost += self.road[self.S[pos]][pos]
              self.T[ pos ] = self.S[ pos ]
              self.S[ pos ] = 0

              for k in range(1, self.nodes+1):
                  if self.S[ k ] != 0:
                     if self.road[self.S[k]][k] > self.road[pos][k]:
                        self.S[ k ] = pos
                         
                                     
      def readGraph(self, filename):

          counter = 0
          input = []
  
          with open(filename, 'r') as file:

               for a_line in file:
                   counter += 1 
                
                   if counter == 1:
                      number_of_nodes = int(a_line.rstrip())

                   else:
                      input.append(a_line.rstrip()) 

          size = len( input )
          self.nodes = number_of_nodes
          self.road = [[0 for i in range(0, number_of_nodes + 1)] for j in range(0, number_of_nodes + 1)]

          for i in range(0, self.nodes + 1):
              for j in range(0, self.nodes + 1):
                  if i == j:
                     self.road[i][j] = 0
                  else:
                     self.road[i][j] = self.infinit          


          for i in range(0, size):
              component = input[ i ]
              node1 = int(component[ 0 ])
              node2 = int(component[ 2 ])
              cost = int(component[ 4 ])
              self.road[ node1 ][ node2 ], self.road[ node2 ][ node1 ] = cost, cost  


ob = MinimumSpanningTree()
ob.solve()

print("Min Cost = ",ob.getCost())
n = 4
print("From 1 to the node {} is {}".format(n, ob.solution(n)))
