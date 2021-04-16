# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:31:58 2020

@author: mourya
"""
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=[]
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent, parent[i])
    
    def union(self,parent,rank,x,y):
        xroot=self.find(parent, x)
        yroot=self.find(parent,y)
        
        if rank[xroot]<rank[yroot]:
            parent[xroot]=yroot
        elif rank[xroot]>rank[yroot]:
            parent[yroot]=xroot
        else:
            parent[xroot]=yroot
            rank[yroot]=+1
    def kruskalMST(self):
        parent=[]
        rank=[0]*self.V
        for i in range(self.V):
            parent.append(i)
        self.graph=sorted(self.graph,key= lambda item:item[2])
        
        result=[]
        e=0
        i=0
        
        while e<self.V-1:
            u,v,w=self.graph[i]
            i=i+1
            x=self.find(parent, u)
            y=self.find(parent, v)
            
            if x!=y:
                e=e+1
                self.union(parent, rank, x, y)
                result.append([u,v,w])
        mincost=0
        for res in result:
            mincost=mincost+res[2]
            print (res)
        print (mincost)
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.kruskalMST()
        