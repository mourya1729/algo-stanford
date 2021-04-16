# # -*- coding: utf-8 -*-
# """
# Created on Mon Nov  2 13:26:14 2020

# @author: mourya
# """
# class minHeap:
#     def __init__(self,arr):
#         self.arr=arr
#         for i in range(len(arr)//2-1,-1,-1):
#             self.minheapify(i)
#     def minheapify(self,i):
#         smallest=i
#         left=2*i+1
#         right=2*i+2
#         if left<len(self.arr) and self.arr[left]<self.arr[smallest]:
#             smallest=left
#         if right<len(self.arr) and self.arr[right]<self.arr[smallest]:
#             smallest=right
#         if smallest!=i:
#             self.arr[i],self.arr[smallest]=self.arr[smallest],self.arr[i]
#             # self.minheapify(smallest)
#     def minheaparr(self):
        # return self.arr
# arr=[5,3,17,10,84,19,6,22,9,1]
# mi=minHeap(arr)
# print (mi.minheaparr())
# class minheapNode:
#     def __init__(self,num,dist):
#         self.x=num
#         self.j=dist
#     def __str__(self):
#         return (str(self.x),str(self.j))
# class minHeap:
#     def __init__(self,keys=[]):
#         self.arr=keys
#         self.mat=[]
#         for i in range(len(self.arr)):
#             self.mat.append(i)
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
#     def bubbup(self,i):
#         if i>0:
#             if self.arr[self.parent(i)].j>self.arr[i].j:
#                 self.arr[self.parent(i)],self.arr[i]=self.arr[i],self.arr[self.parent(i)]
#                 self.bubbup(self.parent(i))
#     def insert(self,num,dist):
#         node=minheapNode(num, dist)
#         self.arr.append(node)
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
#             self.bubbdown(small)
            
#     def pop(self):
#         x=self.arr[0]
#         self.arr[0],self.arr[-1]=self.arr[-1],self.arr[0]
#         del(self.arr[-1])
#         self.bubbdown(0)
#         return x
#     def delete(self,i):
#         # x=self.arr[i]
#         self.arr[i],self.arr[-1]=self.arr[-1],self.arr[i]
#         del(self.arr[-1])
#         self.bubbdown(i)
        
#     def prints(self):
#         for node in self.arr:
#             print ("("+str(node.x)+","+str(node.j)+")",end=" ")
#         return 
# node=minheapNode(0, 7)
# node1=minheapNode(1,8)
# node2=minheapNode(2,2)
# node3=minheapNode(3,3)
# node4=minheapNode(4,5)
# node5=minheapNode(5,9)
# node6=minheapNode(6,10)
# # node7=minheapNode()
# # node8=minheapNode(0, 7)
# # node9=minheapNode(0, 7)
# arr=[node,node1,node2,node3,node4,node5,node6]
# mi=minHeap(arr)
# print (mi.prints())
# mi.insert(7,4)
# mi.insert(8,0)
# print (mi.prints())
# mi.pop()
# print (mi.prints())
# mi.delete(1)
# print (mi.prints())
# # print (mi.minheaparr())

class minheapNode:
    def __init__(self,node,dist):
        self.i=node
        self.j=dist
class minHeap:
    def __init__(self,keys=[]):
        self.arr=keys
        self.mat=[]
        self.size=0
        for key in self.arr:
            self.mat[key.i]=self.arr.index(key)
        for i in range(len(self.arr)//2-1,-1,-1):
            self.minheapify(i)
    def parent(self,i):
        return i//2-1 if i%2==0 else i//2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def minheapify(self,i):
        smallest=i
        left=2*i+1
        right=2*i+2
        if left<len(self.arr) and self.arr[left].j<self.arr[smallest].j:
            smallest=left
        if right<len(self.arr) and self.arr[right].j<self.arr[smallest].j:
            smallest=right
        if smallest!=i:
            self.arr[i],self.arr[smallest]=self.arr[smallest],self.arr[i]
            self.mat[i],self.mat[smallest]=self.mat[smallest],self.mat[i]
            self.minheapify(smallest)
    def bubbup(self,i):
        if i>0:
            if self.arr[self.parent(i)].j>self.arr[i].j:
               self.arr[self.parent(i)],self.arr[i]=self.arr[i],self.arr[self.parent(i)]
               self.mat[self.parent(i)],self.mat[i]=self.mat[i],self.mat[self.parent(i)]
               
               self.bubbup(self.parent(i))
    def insert(self,num,dist):
        node=minheapNode(num, dist)
        self.arr.append(node)
        self.mat.append(node.i)
        self.bubbup(len(self.arr)-1)
    def bubbdown(self,i):
        small=i
        left=2*i+1
        right=2*i+2
        if left<len(self.arr) and self.arr[left].j<self.arr[small].j:
            small=left
        if right<len(self.arr) and self.arr[right].j<self.arr[small].j:
            small=right
        if small != i:
            self.arr[i],self.arr[small]=self.arr[small],self.arr[i]
            self.mat[i],self.mat[small]=self.mat[small],self.mat[i]
            self.bubbdown(small)
            
    def getMin(self):
        x=self.arr[0]
        self.arr[0],self.arr[-1]=self.arr[-1],self.arr[0]
        self.mat[0],self.mat[-1]=self.mat[-1],self.mat[0]
        del(self.arr[-1])
        # del(self.mat[-1])
        self.bubbdown(0)
        return x
    def delete(self,i):
        # x=self.arr[i]
        self.arr[i],self.arr[-1]=self.arr[-1],self.arr[i]
        self.mat[i],self.mat[-1]=self.mat[-1],self.mat[i]
        del(self.arr[-1])
        # del(self.mat[-1])
        self.bubbdown(i)
    def isempty(self):
        if len(self.arr)==0:
            return True
        return False
    def prints(self):
        for node in self.arr:
            print ("("+str(node.i)+","+str(node.j)+")",end=" ")
        return 

# node=minheapNode(0, 7)
# node1=minheapNode(1,8)
# node2=minheapNode(2,2)
# node3=minheapNode(3,3)
# node4=minheapNode(4,5)
# node5=minheapNode(5,9)
# node6=minheapNode(6,10)
# # # node7=minheapNode()
# # # node8=minheapNode(0, 7)
# # # node9=minheapNode(0, 7)
# arr=[node,node1,node2,node3,node4,node5,node6]
# mi=minHeap(7,arr)
# print (mi.prints())
# print (mi.mat)

# mi.delete(2)
# print (mi.prints())
# print(mi.mat)
# # mi.delete(1)
# print (mi.prints())
# # print (mi.minheaparr())
        
        