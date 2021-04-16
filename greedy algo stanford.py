# # -*- coding: utf-8 -*-
# """
# Created on Sun Nov 15 17:37:07 2020

# @author: mourya
# """
# """greedy mst algo: prim"""
# from collections import defaultdict
# import sys
# class Heap:
#     def __init__(self):
#         self.array=[]
#         self.pos=[]
#         self.size=0
#     def newMinHeapNode(self,v,dist):
#         minHeapNode=[v,dist]
#         return minHeapNode
#     def swapMinHeapNode(self,a,b):
#         t = self.array[a] 
#         self.array[a] = self.array[b] 
#         self.array[b] = t 
#         # self.array[a],self.array[b]=self.array[b],self.array[a]
#     def minHeapify(self,idx):
#         smallest=idx
#         left=2*idx+1
#         right=2*idx+2
#         if left<len(self.array) and self.array[left][1]<self.array[smallest][1]:
#             smallest=left
#         if right<len(self.array) and self.array[right][1]<self.array[smallest][1]:
#             smallest=right
#         if smallest != idx:
#             self.pos[self.array[smallest][0]]=idx
#             self.pos[self.array[idx][0]]=smallest
#             self.swapMinHeapNode(idx, smallest)
#             self.minHeapify(smallest)
#     def extractMin(self):
#         if self.isEmpty():
#             return
#         root=self.array[0]
#         lastNode=self.array[self.size-1]
        
#         self.array[0]=lastNode
#         self.pos[lastNode[0]]=0
#         self.pos[root[0]]=self.size-1
        
#         self.size -=1
#         self.minHeapify(0)
        
#         return root
#     def isEmpty(self):
#         if self.size==0:
#             return True
#         return False
#     def decreaseKey(self,v,dist):
#         i=self.pos[v]
#         self.array[i][1]=dist
        
#         while i>0 and self.array[i][1]<self.array[(i-1)//2][1]:
#             self.pos[self.array[i][0]]=(i-1)//2
#             self.pos[self.array[(i-1)//2][0]]=i
#             self.swapMinHeapNode(i, (i-1)//2)
            
#             i=(i-1)//2
#     def isMinHeapNode(self,v):
#         if self.pos[v]<self.size:
#             return True
#         return False
# def printfn(parent,n):
#     for i in range(1,n):
#         print ("%d - %d"%(parent[i],i))
# class Graph:
#     def __init__(self,V):
#         self.V=V
#         self.grap=defaultdict(list)
#     def addEdge(self,src,dest,weight):
#         newNode=[dest,weight]
#         self.grap[src].insert(0,newNode)
#         newNode=[src,weight]
#         self.grap[dest].insert(0,newNode)
#     def primalgo(self):
#         V=self.V
#         keys=[]
        
#         parent=[]
#         minHeap=Heap()
#         for v in range(V):
#             parent.append(-1)
#             keys.append(sys.maxsize)
#             minHeap.array.append(minHeap.newMinHeapNode(v, keys[v]))
#             minHeap.pos.append(v)            
            
#         keys[0]=0
#         minHeap.pos[0]=0
#         minHeap.decreaseKey(0, keys[0])
        
#         minHeap.size=V
#         while not minHeap.isEmpty():
#             root=minHeap.extractMin()
#             u=root[0]
            
#             for pCrawl in self.grap[u]:
#                 v=pCrawl[0]
#                 if minHeap.isMinHeapNode(v) and pCrawl[1]<keys[v]:
#                     keys[v]=pCrawl[1]
#                     parent[v]=u
                    
#                     minHeap.decreaseKey(v, keys[v])
#         print (parent)
#         printfn(parent, V)        
            
        
#         # n=self.V
#         # x=[]
#         # T=[s]
#         # if s>self.V:
#         #     return "vertex not there in graph"
#         # visited=[False]*n
#         # visited[s]=True
#         # # u=s
#         # dist=0
#         # while len(T)<n:
#         #     mini=math.inf
#         #     small=None
#         #     for u in T:
#         #         for v in self.grap[u]:
#         #             if visited[v[0]]==False:
#         #                 if v[1]<mini:
#         #                     mini=v[1]
#         #                     small=[u,v[0]]
#         #     visited[small[1]]=True
#         #     dist+=mini
#         #     x.append(small)
#         #     T.append(small[1])
#         # print (dist)
#         # print (x)
# # g=graph(4)
# # g.addEdge(0, 1, 1)
# # g.addEdge(0,2,4)
# # g.addEdge(0,3,3)
# # g.addEdge(1,3,2)
# # g.addEdge(2,3,5)
# # g.primalgo(0)
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
# graph.primalgo() 
            
                


from collections import defaultdict 
import sys 

class Heap(): 

	def __init__(self): 
		self.array = [] 
		self.size = 0
		self.pos = [] 

	def newMinHeapNode(self, v, dist): 
		minHeapNode = [v, dist] 
		return minHeapNode 

	# A utility function to swap two nodes of 
	# min heap. Needed for min heapify 
	def swapMinHeapNode(self, a, b): 
		t = self.array[a] 
		self.array[a] = self.array[b] 
		self.array[b] = t 

	# A standard function to heapify at given idx 
	# This function also updates position of nodes 
	# when they are swapped. Position is needed 
	# for decreaseKey() 
	def minHeapify(self, idx): 
		smallest = idx 
		left = 2 * idx + 1
		right = 2 * idx + 2

		if left < self.size and self.array[left][1] < self.array[smallest][1]: 
								
			smallest = left 

		if right < self.size and self.array[right][1] < self.array[smallest][1]: 
								
			smallest = right 

		# The nodes to be swapped in min heap 
		# if idx is not smallest 
		if smallest != idx: 

			# Swap positions 
			self.pos[ self.array[smallest][0] ] = idx 
			self.pos[ self.array[idx][0] ] = smallest 

			# Swap nodes 
			self.swapMinHeapNode(smallest, idx) 

			self.minHeapify(smallest) 

	# Standard function to extract minimum node from heap 
	def extractMin(self): 

		# Return NULL wif heap is empty 
		if self.isEmpty() == True: 
			return

		# Store the root node 
		root = self.array[0] 

		# Replace root node with last node 
		lastNode = self.array[self.size - 1] 
		self.array[0] = lastNode 

		# Update position of last node 
		self.pos[lastNode[0]] = 0
		self.pos[root[0]] = self.size - 1

		# Reduce heap size and heapify root 
		self.size -= 1
		self.minHeapify(0) 

		return root 

	def isEmpty(self): 
		return True if self.size == 0 else False

	def decreaseKey(self, v, dist): 

		# Get the index of v in heap array 

		i = self.pos[v] 

		# Get the node and update its dist value 
		self.array[i][1] = dist 

		# Travel up while the complete tree is not 
		# hepified. This is a O(Logn) loop 
		while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]: 
					

			# Swap this node with its parent 
			self.pos[ self.array[i][0] ] = (i-1)//2
			self.pos[ self.array[(i-1)//2][0] ] = i 
			self.swapMinHeapNode(i, (i - 1)//2 ) 

			# move to parent index 
			i = (i - 1) // 2; 

	# A utility function to check if a given vertex 
	# 'v' is in min heap or not 
	def isInMinHeap(self, v): 

		if self.pos[v] < self.size: 
			return True
		return False


def printArr(parent, n): 
	for i in range(1, n): 
		print ("% d - % d" % (parent[i], i) )


class Graph(): 

	def __init__(self, V): 
		self.V = V 
		self.graph = defaultdict(list) 

	# Adds an edge to an undirected graph 
	def addEdge(self, src, dest, weight): 

		# Add an edge from src to dest. A new node is 
		# added to the adjacency list of src. The node 
		# is added at the beginning. The first element of 
		# the node has the destination and the second 
		# elements has the weight 
		newNode = [dest, weight] 
		self.graph[src].insert(0, newNode) 

		# Since graph is undirected, add an edge from 
		# dest to src also 
		newNode = [src, weight] 
		self.graph[dest].insert(0, newNode) 

	# The main function that prints the Minimum 
	# Spanning Tree(MST) using the Prim's Algorithm. 
	# It is a O(ELogV) function 
	def PrimMST(self): 
		# Get the number of vertices in graph 
		V = self.V 
		
		# key values used to pick minimum weight edge in cut 
		key = [] 
		
		# List to store contructed MST 
		parent = [] 

		# minHeap represents set E 
		minHeap = Heap() 

		# Initialize min heap with all vertices. Key values of all 
		# vertices (except the 0th vertex) is is initially infinite 
		for v in range(V): 
			parent.append(-1) 
			key.append(sys.maxsize) 
			minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) ) 
			minHeap.pos.append(v) 
       
		# Make key value of 0th vertex as 0 so 
		# that it is extracted first 
		minHeap.pos[0] = 0
		key[0] = 0
		minHeap.decreaseKey(0, key[0]) 

		# Initially size of min heap is equal to V 
		minHeap.size = V; 

		# In the following loop, min heap contains all nodes 
		# not yet added in the MST. 
		while minHeap.isEmpty() == False: 

			# Extract the vertex with minimum distance value 
			newHeapNode = minHeap.extractMin() 
			u = newHeapNode[0] 

			# Traverse through all adjacent vertices of u 
			# (the extracted vertex) and update their 
			# distance values 
			for pCrawl in self.graph[u]: 

				v = pCrawl[0] 

				# If shortest distance to v is not finalized 
				# yet, and distance to v through u is less than 
				# its previously calculated distance 
				if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]: 
					key[v] = pCrawl[1] 
					parent[v] = u 

					# update distance value in min heap also 
					minHeap.decreaseKey(v, key[v])
       printArr(parent, V)
        
graph = Graph(9) 
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
graph.PrimMST() 

# This code is contributed by Divyanshu Mehta 
