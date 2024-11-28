from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bin_tree = AVLTree()
        self.bin_tree2 = AVLTree()
        self.obj_tree = AVLTree()

    def add_bin(self, bin_id, capacity):
        bin1 = Bin(bin_id, capacity)
        self.bin_tree.root = self.bin_tree.insert(self.bin_tree.root,capacity,bin_id,bin1)
        self.bin_tree2.root = self.bin_tree2.insert(self.bin_tree2.root,bin_id,capacity,bin1)
        

    def add_object(self, object_id, size, color):
        obj = Object(object_id, size, color)
        self.obj_tree.root = self.obj_tree.insert(self.obj_tree.root,object_id,size,obj)
        if(color == Color.BLUE or color == Color.YELLOW):
            
            color1 = 2
            if(color == Color.BLUE):
                color1 = 1
              
            bin1 = self.bin_tree.insertobj_compact(self.bin_tree.root,object_id,size,color1,obj)
            obj.link1 = bin1
            if(bin1 != None):
                obj.index = len(bin1.obj)-1
            if(bin1 == None):
                raise  NoBinFoundException
        else:
            color1 = 4
            if(color == Color.RED):
                color1 = 3
            bin2 = self.bin_tree.insertobj_largest(self.bin_tree.root,object_id,size,color1,obj) 
            obj.link1 = bin2 
            if(bin2 != None):
                obj.index = len(bin2.obj)-1
            
            if(bin2 == None):
                raise  NoBinFoundException  
        

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        user = self.obj_tree.root
        while(user != None):
            if(user.id>object_id):
                user = user.left
            elif(user.id<object_id):
                user = user.right   
            else:
                obj1: Object =  user.store[0][1]
                bin: Bin =  obj1.link1 
                cap = obj1.size
                cap_bin = bin.cap
                index = obj1.index
                id_bin = bin.id
                list = bin.obj 
                
                # cap = list[i] 
                # updating bin
                bin.cap = cap + cap_bin  
                list[index][0] = list[-1][0]
                list[index][1] = list[-1][1]
                obj2 = list[index][1]
                list.pop()  
                if(obj2 != obj1):
                    obj2.index  = index
                 
                # updating object params
                obj1.link1 = None
                obj1.index =-1

                self.bin_tree.root  = self.bin_tree.delete(self.bin_tree.root,cap_bin,id_bin)
                self.bin_tree.root = self.bin_tree.insert(self.bin_tree.root,cap_bin+cap,id_bin,bin)
                return
                

        





















        

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        user = self.bin_tree2.root
        while(user != None):
            if(user.id>bin_id):
                user = user.left
            elif(user.id<bin_id):
                user = user.right   
            else:
                bin :Bin =  user.store[0][1]  
                list = []
                for i in bin.obj:
                    if i[0] != None:
                        list.append(i[0])

                # list = bin.obj
                return (bin.cap,list)

        

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored\
        user = self.obj_tree.root
        while(user != None):
            if(user.id>object_id):
                user = user.left
            elif(user.id<object_id):
                user = user.right   
            else:
                obj1: Object =  user.store[0][1]
                # print(obj1.link1)
                if(obj1.link1 == None):
                    return
                bin: Bin =  obj1.link1   
                return bin.id  
        
        return 0
       
        
    
    