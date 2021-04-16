# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:45:05 2020

@author: mourya
"""
"""graph implementation""collections"""
from collections import defaultdict
class Graph:
    def __init__(self,vertices=0):
        self.lis=defaultdict(list)
        self.vertices=vertices
        self.size=0
    def addEdge(self,u,v):
        self.lis[u].append(v)
        self.lis[v].append(u)
        if u not in self.lis:
            self.size+=1
        if v not in self.lis:
            self.size+=1
    def isEdge(self,u,v):
        if u in self.lis:
            if v in self.lis[u]:
                return True
        return False
    def isVertex(self,u):
        if u in self.lis:
            return True
        False
    def size(self):
        return self.size
    def n_vertices(self):
        return self.vertices
    def prints(self):
        print (self.lis)
        for key in self.lis:
            print (str(key) +"-> ",end=" ")
            for val in self.lis[key]:
                print (str(val)+", ",end="")
            print("\n")
class queue:
    def __init__(self,n):
        self.maxsize=n
        self.a=[None]*n
        self.front=0
        self.rear=0
        self.size=0
    def insert(self,num):
        if self.size==self.maxsize:
            print ( "overflow")
            return            
        if self.size<self.maxsize:
            self.a[self.rear]=num
            self.rear=(self.rear+1)%self.maxsize
            self.size+=1
    def delete(self):
        num=self.a[self.front]
        self.a[self.front]=None
        self.front=(self.front+1)%self.maxsize
        self.size-=1
        return num
    def prints(self):
        i=self.front
        count=0
        while count<self.size:
            print (self.a[i])
            i=(i+1)%self.maxsize
            count+=1
    def get_size(self):
        return self.size
"""bfs problem"""
def bfs(graph,s):
    q=queue(10)
    q.insert(s)
    visited={s:True}
    while q.get_size()!=0:
        u=q.delete()
        print (u,end=" ")
        for v in graph.lis[u]:
            if v not in visited:
                visited[v]=True
                q.insert(v)
"""bfs:shortest distance"""
# import math
def shortdist(graph,u,v):
    q=queue(10)
    q.insert(u)
    dis={}
    dis[u]=0
    # dis[v]=math.inf  
    visited={u:True}
    while q.get_size()!=0:
        s=q.delete()
        if v==s:
            return dis[s]
        for n in graph.lis[s]:
            if n not in visited:
                dis[n]=dis[s]+1
                visited[n]=True
                q.insert(n)
"""connected components undirected graph:bfs"""
def connectedbfs(graph):
    visited={}
    count=0
    def bfs(graph,s):
        q=queue(len(graph.lis)+5)
        q.insert(s)
        visited[s]=True
        while q.get_size()!=0:
            u=q.delete()
            print (u,end=" ")
            for v in graph.lis[u]:
                if v not in visited:
                    visited[v]=True
                    q.insert(v)
    for i in range(1,len(graph.lis)+1):
        if i not in visited:
            count+=1
            print ("direct "+str(count),end=":")
            bfs(graph, i)
            print("\n")
# graph=Graph()
# graph.add_edge(1,3)
# graph.add_edge(1,5)
# graph.add_edge(3,5)
# graph.add_edge(5,7)
# graph.add_edge(5,9)
# graph.add_edge(2,4)
# graph.add_edge(6,8)
# graph.add_edge(6,10)
# graph.add_edge(8,10)
# connectedbfs(graph)    

"""dfs :::"""    
def dfs(graph,s):
    visited={}
    def df(graph,v,visited):
        
        print (v,end=" ")
        visited[v]=True
        for w in graph.lis[v]:
            if w not in visited:
                df(graph,w,visited)
        
    return df(graph,s,visited)
"""topological sort"""
global x
def topologysort(graph):
    visited={}
    x=graph.n_vertices()
    top=[0]*x
    # current_label=x
    def dfs(graph,s):
        nonlocal x
        visited[s]=True
        if s in graph.lis:
            for w in graph.lis[s]:
                if w not in visited:
                    dfs(graph, w)
        top[x-1]=s
        x =x-1
    for vertex in graph.lis:
        if vertex not in visited:
            dfs(graph, vertex)
    
    print (top)
    
# g = Graph(6) 
# g.addEdge(5, 2) 
# g.addEdge(5, 0) 
# g.addEdge(4, 0) 
# g.addEdge(4, 1) 
# g.addEdge(2, 3) 
# g.addEdge(3, 1)
# topologysort(g)    
class stack:
    def __init__(self):
        self.arr=[]
        self.size=0
    def push(self,num):
        self.arr.append(num)
        self.size+=1
    def pop(self):
        x=self.arr[-1]
        del(self.arr[-1])
        self.size -=1
        return x
    def peek(self):
        return self.arr[-1]
"""kosaraju algo for calculating scc in directed graph"""
def dfsloop(graph):
    st=stack()
    grev=revgraph(graph)
    x=grev.n_vertices()
    visited=[False]*x

    def dfs(graph,s,stack):
        visited[s]=True
        if s in graph.lis:
            for w in graph.lis[s]:
                if visited[w]!=True:
                    dfs(graph, w, stack)
        stack.push(s)
    for i in range(x-1,-1,-1):
        if visited[i]==False:
            dfs(grev, i,st)
    return st
def dfsloo(graph,stack):
    x=graph.n_vertices()
    visited=[False]*x
    def dfs(graph,s):
        visited[s]=True
        print (s,end=" ")
        for w in graph.lis[s]:
            if visited[w]==False:
                dfs(graph, w)
    while stack.size>0:
        i=stack.pop()
        if visited[i]==False:
            print ("\n")
            dfs(graph, i)
        
        
def revgraph(grap):
    grev=Graph(grap.n_vertices())
    for u in grap.lis:
        for v in grap.lis[u]:
            grev.lis[v].append(u)
    return grev
def scc(graph):
    st=dfsloop(graph)
    dfsloo(graph, st)
    
    
# g = Graph(9) 
# g.addEdge(8,2) 
# g.addEdge(5,8) 
# g.addEdge(2,5) 
# g.addEdge(6,0) 
# g.addEdge(0,3) 
# g.addEdge(7,5)
# g.addEdge(8,6)
# g.addEdge(1,7)
# g.addEdge(4,1)
# g.addEdge(7,4)
# g.addEdge(3,6)
# # print (g.n_vertices())
# # print (revgraph(g))
# scc(g)

"""dijkstra algo:"""
from collections import defaultdict
class Graph:
    def __init__(self,vertices=0):
        self.lis=defaultdict(list)
        self.dist=[[0 for i in range(vertices)] for j in range(vertices)]
        self.vertices=vertices
        self.size=0
    def addEdge(self,u,v,dist):
        self.lis[u].append(v)
        self.lis[v].append(u)
        self.dist[u][v]=dist
        self.dist[v][u]=dist
        if u not in self.lis:
            self.size+=1
        if v not in self.lis:
            self.size+=1
    def isEdge(self,u,v):
        if u in self.lis:
            if v in self.lis[u]:
                return True
        return False
    def isVertex(self,u):
        if u in self.lis:
            return True
        False
    def size(self):
        return self.size
    def n_vertices(self):
        return self.vertices



# class minheapNode:
#     def __init__(self,node,dist):
#         self.i=node
#         self.j=dist
#     def __str__(self):
#         return str(self.i)+","+str(self.j)
# class minHeap:
#     def __init__(self,n,keys=[]):
#         self.arr=keys
#         self.mat=[]
#         self.size=0
#         # for key in self.arr:
#             # self.mat[key.i]=self.arr.index(key)
#         for i in range(len(self.arr)//2-1,-1,-1):
#             self.minheapify(i)
#     def parent(self,i):
#         return i//2-1 if i%2==0 else i//2
#     def left(self,i):
#         return 2*i+1
#     def right(self,i):
#         return 2*i+2
#     def minheapify(self,i):
#         smallest=i
#         left=2*i+1
#         right=2*i+2
#         if left<len(self.arr) and self.arr[left].j<self.arr[smallest].j:
#             smallest=left
#         if right<len(self.arr) and self.arr[right].j<self.arr[smallest].j:
#             smallest=right
#         if smallest!=i:
#             self.arr[i],self.arr[smallest]=self.arr[smallest],self.arr[i]
#             self.mat[i],self.mat[smallest]=self.mat[smallest],self.mat[i]
#             self.minheapify(smallest)
#     def bubbup(self,i):
#         if i>0:
#             if self.arr[self.parent(i)].j>self.arr[i].j:
#                self.arr[self.parent(i)],self.arr[i]=self.arr[i],self.arr[self.parent(i)]
#                self.mat[self.parent(i)],self.mat[i]=self.mat[i],self.mat[self.parent(i)]
               
#                self.bubbup(self.parent(i))
#     def insert(self,num,dist):
#         node=minheapNode(num, dist)
#         self.size+=1
#         self.arr.append(node)
#         self.mat.append(node.i)
#         # self.mat[node.i]=self.arr.index(node)
#         self.bubbup(len(self.arr)-1)
#     def bubbdown(self,i):
#         small=i
#         left=2*i+1
#         right=2*i+2
#         if left<len(self.arr) and self.arr[left].j<self.arr[small].j:
#             small=left
#         if right<len(self.arr) and self.arr[right].j<self.arr[small].j:
#             small=right
#         if small != i:
#             self.arr[i],self.arr[small]=self.arr[small],self.arr[i]
#             self.mat[i],self.mat[small]=self.mat[small],self.mat[i]
#             self.bubbdown(small)
            
#     def getMin(self):
#         x=self.arr[0]
#         self.size -=1
#         self.arr[0],self.arr[-1]=self.arr[-1],self.arr[0]
#         self.mat[0],self.mat[-1]=self.mat[-1],self.mat[0]
#         # self.arr[-1].j=math.inf
#         del(self.arr[-1])
#         # del(self.mat[-1])
#         self.bubbdown(0)
#         return x
#     def swapMinHeapNode(self,a, b):
#         t = self.arr[a]
#         self.arr[a] = self.arr[b]
#         self.arr[b] = t
#     def delete(self,i):
        
#         x=self.arr[i]
#         self.arr[i],self.arr[-1]=self.arr[-1],self.arr[i]
#         self.mat[i],self.mat[-1]=self.mat[-1],self.mat[i]
#         del(self.arr[-1])
#         self.size -=1
#         # del(self.mat[-1])
#         # self.arr[-1].j=math.inf
#         self.bubbdown(i)
#         return x.i
#     def decreaseKey(self,v,dist):
#         x=self.mat[v]
#         self.arr[x].j=dist
#         while x>0 and self.arr[x].j<self.arr[self.parent(x)].j:
#             self.mat[self.arr[x].i]=self.parent(x)
#             self.mat[self.arr[self.parent(x)].i]=x
#             self.swapMinHeapNode(x, self.parent(x))
        
#     def isInminHeap(self,v):
#         if v<self.size:
#             return True
#         return False
#     def isempty(self):
#         if self.size==0:
#             return True
#         return False
#     def prints(self):
#         for node in self.arr:
#             print ("("+str(node.i)+","+str(node.j)+")",end=" ")
#         return 

# import math
# def shortdis(graph,s,w):
#     dis=graph.dist
#     # x=[]
#     V=graph.n_vertices()
#     visited=[False]*V
#     A=[math.inf]*V
#     A[s]=0
#     visited[s]=True
#     heap=minHeap(V)
   
#     keys=[math.inf]*V
#     keys[0]=0
#     for i in range(len(keys)):
#         heap.insert(i,keys[i])
#     # print (heap.prints())
#     while not heap.isempty():       
#         pop=heap.getMin() 
#         # print (pop.i)
#         visited[pop.i]=True
#         A[pop.i]=pop.j
#         # x.append(pop.i)
#         u=pop.i
#         for v in graph.lis[u]:
#             if visited[v]==False:
#                 # print (v)
#                 # print(heap.mat)
#                 # for node in heap.arr:
#                 #     if node.i==v:
#                 #         pos_heap=heap.arr.index(node)
#                 pos_heap=heap.mat[v]
#                 # print (pos_heap)
#                 # print (heap.prints())
#                 # p=heap.delete(pos_heap)
#                 if heap.isInminHeap(pos_heap):
#                     keys[v]=min(keys[v],A[u]+dis[u][v])
#                 # print (keys[v])
#                 # heap.insert(v,keys[v])
#                     heap.decreaseKey(v, keys[v])
#                     # heap.arr[pos_heap].j=keys[v]
#                     # heap.minheapify(pos_heap)
                
        
#     return A
# g=graph(6)
# g.addEdge(0, 1, 4)
# g.addEdge(0,3,8)
# g.addEdge(1,3,11)
# g.addEdge(1, 2, 8)
# g.addEdge(2,4,2)
# g.addEdge(3,4,7)
# g.addEdge(4,5,6)
# g.addEdge(3,5,1)
# g.addEdge(2,3,7)
# g.addEdge(2,5,4)
# g.addEdge(6,5,2)
# g.addEdge(3,5,14)
# g.addEdge(3,4,9)
# g.addEdge(5,4,10)
# graph = Graph(9)
# graph.addEdge(0, 1, 4)
# graph.addEdge(0, 7, 8)
# graph.addEdge(1, 2, 8)
# graph.addEdge(1, 7, 11)
# graph.addEdge(2, 3, 7)
# graph.addEdge(2, 8, 2)
# graph.addEdge(2, 5, 4)
# graph.addEdge(3, 4, 9)
# graph.addEdge(3, 5, 14)
# graph.addEdge(4, 5, 10)
# graph.addEdge(5, 6, 2)
# graph.addEdge(6, 7, 1)
# graph.addEdge(6, 8, 6)
# graph.addEdge(7, 8, 7)
# # graph.dijkstra(0)
# print(shortdis(graph, 0, 3))

"""dijkstra algo: shortest path"""
import sys
from collections import defaultdict
class Heap:
    def __init__(self):
        self.array=[]
        self.size=0
        self.pos=[]
    def newMinHeapNode(self,v,dist):
        minHeapNode=[v,dist]
        return minHeapNode
    def swapMinHeapNode(self,a,b):
       t=self.array[b]
       self.array[b]=self.array[a]
       self.array[a]=t
      
    def minHeapify(self,idx):
        smallest=idx
        left=2*idx+1
        right=2*idx+2
        if left<self.size and self.array[left][1]<self.array[smallest][1]:
            smallest=left
        if right<self.size and self.array[right][1]<self.array[smallest][1]:
            smallest=right
        if smallest != idx:
            self.pos[self.array[smallest][0]]=idx
            self.pos[self.array[idx][0]]=smallest
            self.swapMinHeapNode(idx,smallest)
            self.minHeapify(smallest)
    def extractMin(self):
        if self.isEmpty()==True:
            return 
        
        root=self.array[0]
        lastNode=self.array[self.size-1]
        
        self.array[0]=lastNode
        self.pos[lastNode[0]]=0
        self.pos[root[0]]=self.size-1
        
        self.size -=1
        self.minHeapify(0)
        
        return root
    
    def isEmpty(self):
        return True if self.size==0 else False
    
    def decreaseKey(self, v ,dist):
        i=self.pos[v]
        
        self.array[i][1]=dist
        
        while i>0 and self.array[i][1] < self.array[(i-1)//2][1]:
            self.pos[self.array[i][0]]=(i-1)//2
            self.pos[self.array[(i-1)//2][0]]=i
            self.swapMinHeapNode(i, (i-1)//2)
            
            i=(i-1)//2
    def isInMinHeap(self,v):
        if self.pos[v]<self.size:
            return True
        return False
def printArr(dist,n):
    print ("vertex\tDistance From source")
    for i in range(n):
        print ("%d\t\t%d" % (i,dist[i]))
class GRAPH:
    def __init__(self,V):
        self.V=V
        self.graph=defaultdict(list)
    def addEdge(self,src,dest,weight):
        newNode=[dest,weight]
        self.graph[src].insert(0,newNode)
        
        newNode=[src,weight]
        self.graph[dest].insert(0,newNode)
    
    def dijkstra(self,src):
        V=self.V
        dist=[]
        
        minHeap=Heap()
        for v in range(V):
            dist.append(sys.maxsize)
            minHeap.array.append(minHeap.newMinHeapNode(v,dist[v]))
            minHeap.pos.append(v)
        
        minHeap.pos[src]=src
        dist[src]=0
        minHeap.decreaseKey(src, dist[src])

        minHeap.size=V
        
        while minHeap.isEmpty() == False:
            newHeapNode=minHeap.extractMin()
            u=newHeapNode[0]
            for pCrawl in self.graph[u]:
                v=pCrawl[0]
                if minHeap.isInMinHeap(v) and dist[u]!=sys.maxsize and pCrawl[1]+dist[u]<dist[v]:
                    dist[v]=pCrawl[1]+dist[u]
                    minHeap.decreaseKey(v, dist[v])
        printArr(dist, V)
graph = GRAPH(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.dijkstra(0)
        