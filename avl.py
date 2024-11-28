from node import Node
from bin import Bin


def comp_1(node_1:Node, node_2:Node):
    if node_1.id < node_2.id:
        return -1
    elif node_1.id > node_2.id:
        return 1
    else:
        if node_1.store[0][0] < node_2.store[0][0]:
            return -1
        elif node_1.store[0][0] > node_2.store[0][0]:
            return 1
        else:
            return 0
        

def comp_2(node_1:Node, node_2:Node):
    if node_1.id < node_2.id:
        return -1
    elif node_1.id > node_2.id:
        return 1
    else:
        if(len(node_1.store) == 0  or len(node_1.store) == 0):
            return 0
        if node_1.store[0][0] < node_2.store[0][0]:
            return 1
        elif node_1.store[0][0] > node_2.store[0][0]:
            return -1
        else:
            return 0        
        

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function
    
    def getheight(self,node: Node):
        if(node == None):
            return 0
        else:
            return node.height
        
    def leftRotation(self,node : Node):
        x : Node= node.right
        t2 = x.left
        x.left = node
        node.right = t2
        
        node.height = 1+max(self.getheight(node.left),self.getheight(node.right))
        x.height = 1+max(self.getheight(x.left),self.getheight(x.right))
        return x
    def rightRotation(self,node : Node):
        x : Node= node.left
        t2 = x.right
        x.right = node
        node.left = t2
        
        node.height = 1+max(self.getheight(node.left),self.getheight(node.right))
        x.height = 1+max(self.getheight(x.left),self.getheight(x.right))
        return x   
    def insert(self,node: Node,id : int,data,bin :Bin):
        if(node == None):
            return Node(id,data,bin)
        if(node.id> id):
            node.left = self.insert(node.left,id,data,bin)
        elif(node.id< id):
            node.right = self.insert(node.right,id,data,bin)  
        else:
            if(node.store[0][0]>data):
                node.left = self.insert(node.left,id,data,bin)
            elif node.store[0][0] < data:
                node.right = self.insert(node.right, id, data, bin)
            else:
            # If id and data are both the same, append to the store
                node.store.append([data, bin])
                return node    
            # else:
            #     node.right = self.insert(node.right,id,data,bin)
            #     # node.store.append([data,bin])
            # return node 
        
        node.height = 1+max(self.getheight(node.left),self.getheight(node.right))
        bf = self.balancefactor(node)
        if(bf>1 and (node.left.id >id or (node.left.id == id and node.left.store[0][0] >data))):     
            return self.rightRotation(node)
        if(bf<-1 and (node.right.id <id or (node.right.id == id and node.right.store[0][0] <data))):
            return self.leftRotation(node)
        
        if(bf>1 and (node.left.id <id or (node.left.id == id and node.left.store[0][0] <data))):
            node.left = self.leftRotation(node.left)
            return self.rightRotation(node)
        if(bf<-1 and (node.right.id >id or (node.right.id == id and node.right.store[0][0] >data))):
            node.right = self.rightRotation(node.right)
            return self.leftRotation(node)
        return node
        # if bf > 1 and self.balancefactor(node.left) >= 0:      
        #     return self.rightRotation(node)
        # if bf > 1 and self.balancefactor(node.left) < 0:
        #     node.left = self.leftRotation(node.left)
        #     return self.rightRotation(node)
        # if bf < -1 and self.balancefactor(node.right) <= 0:
        #     return self.leftRotation(node)
        # if bf < -1 and self.balancefactor(node.right) > 0:
        #     node.right = self.rightRotation(node.right)
        #     return self.leftRotation(node)

        # return node
    def insuc(self,node : Node):
        current = node
        while current.left is not None:
            current = current.left
        return current    
    def delete(self,node : Node,element,id):
        if(node == None):
            return node
        if(node.id <element):
            node.right = self.delete(node.right,element,id)
        elif(node.id >element):
            node.left = self.delete(node.left,element,id)
        elif(node.id == element and len(node.store) != 0 and node.store[0][0] < id):
                # print(node.store[0][0])
                node.right = self.delete(node.right,element,id)
        elif(node.id == element and len(node.store) != 0 and node.store[0][0] > id):        
                # print(node.store[0][0])
                node.left = self.delete(node.left,element,id) 
        else:           

            res = node.right
            les = node.left
            if(res == None):
                nodes : Node= les
                node = None
                return les
            elif(les == None):
                nodes : Node= res               
                node = None
                return res
            
            temp = self.insuc(node.right)
            node.id = temp.id  
            node.store = temp.store  
            node.right = self.delete(node.right,temp.id,temp.store[0][0])

            if(node is None):
                return node
        node.height = 1+max(self.getheight(node.right),self.getheight(node.left))
        bf = self.balancefactor(node)

        
        if(bf>1 and self.balancefactor(node.left)>=0):
            return self.rightRotation(node)
           
        if(bf>1 and self.balancefactor(node.left)<0):
            node.left = self.leftRotation(node.left)
            return self.rightRotation(node)
        if(bf<-1 and self.balancefactor(node.right)<=0):
            return self.leftRotation(node)
        if(bf<-1 and self.balancefactor(node.right)>0):
            node.right = self.rightRotation(node.right)
            return self.leftRotation(node)


        return node 
    def balancefactor(self,node : Node):
        if(node is None):
            return 0
        return self.getheight(node.left) - self.getheight(node.right)

        

    def pri(self,Nodes: Node):
        Nod = Nodes
        if(Nod == None):
            return
        if(Nod.left != None):
            self.pri(Nod.left)
        print(Nod.id," ",Nod.height,self.balancefactor(Nod),Nod.store)  
        for i in range(len(Nod.store)):
            no = Nod.store[i][1]
            if no is not None:
                print(no.obj)

        
        if(Nod.right != None):
            self.pri(Nod.right)   











    def node_finder(self,node: Node,id,data):
        no = node
        maxi = no 
        while(no != None):
            if(no.id>id):
                no = no.left
            elif(no.id<id):
                no = no.right
            elif(no.store[0][0]>=data):
                if(no.right != None ):
                    maxi = no
                    no = no.right
                else:
                    return no 

            elif(no.store[0][0]<data):
                no = no.right

        return maxi

    def node_finder2(self,node: Node,id,data):
        no = node
        maxi = no 
        while(no != None):
            if(no.id>id):
                no = no.left
            elif(no.id<id):
                no = no.right
            elif(no.store[0][0]<=data):
                if(no.left != None):
                    maxi = no
                    no = no.left
                else:
                    return no 

            elif(no.store[0][0]>data):
                no = no.left

        return maxi 
    
    
      
           
                 

        
    def insertobj_compact(self,node: Node,id : int,size,color,obj =None):
        if(node == None):
            return None
        if(node.id <size):
            if(node.right == None):
               return None
            
            
            return self.insertobj_compact(node.right,id,size,color,obj)
        elif(node.id >=size ):
            # if(size== 70):
            #     print(node.left.right)
            if(node.left == None or node.left.id<size):
                 check = node
                 max = node
                 while check is not None:
                     if(check.id >= size ):
                         max = check
                         if check.left is not None:
                            check = check.left
                         else:
                             break   
                     else:
                         if check.right is not None:
                            check = check.right 
                         else:
                             break   
                #  print(check.store[0][0],'spw') 
                 check = max        
                 if(check.id >= size and node.id>=check.id):
                     node = check         
                 if(color == 1):
                     node.store[0][1].obj.append([id,obj])
                     node.store[0][1].cap = node.id-size
                     id1 = node.id
                    #  print(node.store[0][0],node.store[0][1])
                     id  = node.store[0][0]
                     bin = node.store[0][1]
                     node.store.pop()
                     if(len(node.store) == 0):
                        self.root = self.delete(self.root,node.id,id)
                     self.root = self.insert(self.root,id1-size,id,bin)
                     del node
                     return bin
                 else:
                     node = self.node_finder(self.root,node.id,node.store[0][0])
                    
                    #  node = node1
                    
                     node.store[0][1].obj.append([id,obj])
                     node.store[0][1].cap = node.id-size
                     id1 = node.id
                    #  print(node.store[0][0],node.store[0][1],node.id)
                     id  = node.store[0][0]
                     bin = node.store[0][1]
                      
                     node.store.pop()
                     if(len(node.store) == 0):
                        self.root = self.delete(self.root,node.id,id)
                    #  self.root = self.deletepart1(self.root,node.cap,color)
                     
                     self.root = self.insert(self.root,id1-size,id,bin)
                     del node
                     
                     return bin
                 
            else:
               return self.insertobj_compact(node.left,id,size,color,obj)      

        return  None  

         
                     
        
        




        
    def insertobj_largest(self,node: Node,id : int,size,color,obj= None):
        if(node == None):
            return None
        if(node.id <size):
            if(node.right == None):
               return None
            return self.insertobj_largest(node.right,id,size,color,obj)
        elif(node.id >=size ):
            if(node.right == None or node.right.id<size):
                 if(color == 4):
                     node.store[0][1].obj.append([id,obj])
                     node.store[0][1].cap = node.id-size
                     id1 = node.id
                    #  print(node.store[0][0],node.store[0][1])
                     id  = node.store[0][0]
                     bin = node.store[0][1]
                     node.store.pop()
                     if(len(node.store) == 0):
                        self.root = self.delete(self.root,node.id,id)
                     self.root = self.insert(self.root,id1-size,id,bin)
                     del node
                     return bin
                 else:
                    #  node.store[-1][1].obj.append(id)
                    #  return node.store[-1][1]
                     node = self.node_finder2(self.root,node.id,node.store[0][0])
                    #  node = node1
                    
                     node.store[0][1].obj.append([id,obj])
                     node.store[0][1].cap = node.id-size
                     id1 = node.id
                    #  print(node.store[0][0],node.store[0][1],node.id)
                     id  = node.store[0][0]
                     bin = node.store[0][1]
                      
                     node.store.pop()
                     if(len(node.store) == 0):
                        self.root = self.delete(self.root,node.id,id)
                    #  self.root = self.deletepart1(self.root,node.cap,color)
                     
                     self.root = self.insert(self.root,id1-size,id,bin)
                     del node
                     
                     return bin
            else:
                return self.insertobj_largest(node.right,id,size,color,obj)     

        return  None 
        
        

# roots = AVLTree() 
# Bi = Bin(100,55)
# Bi.obj.append(89)

# roots.root = roots.insert(roots.root,55,100,Bi)
# Bi2 = Bin(200,55)
# roots.root = roots.insert(roots.root,55,200,Bi2) 
# Bi3 = Bin(500,55)
# roots.root = roots.insert(roots.root,55,500,Bi3)  
# Bi6 = Bin(900,55)
# roots.root = roots.insert(roots.root,55,900,Bi6)  
# Bi31 = Bin(5100,55)
# roots.root = roots.insert(roots.root,55,5100,Bi31)  
# Bi13 = Bin(1000,55)
# roots.root = roots.insert(roots.root,55,1000,Bi13)  
# Bi4 = Bin(300,590)
# # roots.root = roots.insert(roots.root,57,300,Bi4)
# # roots.root = roots.insert(roots.root,590,300,Bi4) 
# # roots.root = roots.delete(roots.root,55,900)  
# # req2 = roots.node_finder2(roots.root,55,100)
# # print(req2.store[0][0])
# # req = roots.insertobj_compact(roots.root,1000,550,2) 
# req = roots.insertobj_largest(roots.root,1002,45,3) 
# req = roots.insertobj_largest(roots.root,1001,45,4)  

# req = roots.insertobj_compact(roots.root,1080,40,2) 
# req = roots.insertobj_compact(roots.root,1081,41,2)  
# req = roots.insertobj_compact(roots.root,1082,41,2)  

# # req = roots.insertobj_compact(roots.root,1008,54,2) 
# req = roots.insertobj_compact(roots.root,1007,54,2) 
# req = roots.insertobj_compact(roots.root,1009,1,2) 


# # req = roots.insertobj_compact(roots.root,1003,40,2) 
# # req = roots.insertobj_compact(roots.root,1006,56,2) 
# req = roots.insertobj_compact(roots.root,1004,1,1) 

# if req != None:
#     print(req.cap)  
# else:
#     print('Not Found')

# roots.pri(roots.root) 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 










# def insertobj_compact(self,node: Node,id : int,size,color):
#         if(node == None):
#             return None
#         if(node.id <size):
#             if(node.right == None):
#                if(size== 70):
#                    print(node.id,'special')
#                return None
#             return self.insertobj_compact(node.right,id,size,color)
#         elif(node.id >=size ):
#             if(size== 70):
#                 print(node.left.id)
#             if(node.left == None or node.left.id<size):
#                  if(color == 1):
#                      node.store[0][1].obj.append(id)
#                      node.store[0][1].cap = node.id-size
#                      id1 = node.id
#                     #  print(node.store[0][0],node.store[0][1])
#                      id  = node.store[0][0]
#                      bin = node.store[0][1]
#                      node.store.pop(0)
#                      if(len(node.store) == 0):
#                         self.root = self.delete(self.root,node.id,id)
#                      self.root = self.insert(self.root,id1-size,id,bin)
#                      del node
#                      return bin
#                  else:
#                      node = self.node_finder(self.root,node.id,node.store[0][0])
#                     #  node = node1
                    
#                      node.store[0][1].obj.append(id)
#                      node.store[0][1].cap = node.id-size
#                      id1 = node.id
#                     #  print(node.store[0][0],node.store[0][1],node.id)
#                      id  = node.store[0][0]
#                      bin = node.store[0][1]
                      
#                      node.store.pop(0)
#                      if(len(node.store) == 0):
#                         self.root = self.delete(self.root,node.id,id)
#                     #  self.root = self.deletepart1(self.root,node.cap,color)
                     