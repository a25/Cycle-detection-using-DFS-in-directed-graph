from collections import  defaultdict
n=6
T=[[0 for i in range(n+1)] for j in range(n+1)]
#Its directed graph
T[1][2]=1
T[2][3]=1
T[1][3]=1
T[4][1]=1
T[4][5]=1
T[5][6]=1
T[6][4]=1

black_set=[0]*(n+1) #nodes completed visit
gray_set=[0]*(n+1) #nodes currenty in visit
parents=defaultdict(int)
white_set=[1]*(n+1) # node not started visiting
white_set[0]=0

def check_set(arr):
  for i,el in enumerate(arr):
    if el :
      return i
  return 0

# dfs 
def dfs(node):
  gray_set[node]=1
  white_set[node]=0
  for neighbour in range(n+1):
    value=T[node][neighbour]
    # print(neighbour,gray_set,node,black_set[neighbour])
    if(value and not gray_set[neighbour] and not black_set[neighbour] ): # its not currently in visit and not totally visited yet
      parents[neighbour]=node
      dfs(neighbour)
    elif(value and gray_set[neighbour]):
      print("cycle detected")
      node1=node
      print(node1,"<--",end='')
      while(1):
        node1=parents[node1]
        if(node1<1):
          # print(parents)
          break
        print(node1,"<--",end='')
      print('')
  

  black_set[node]=1
  gray_set[node]=0
  if(check_set(gray_set)==0):# means white set still exists and grey is empty
    unvisited_index=check_set(white_set)
    if(unvisited_index!=0):
      dfs(unvisited_index)

dfs(1)
  
