class Node:
    def __init__(self,data,store,bin=None):
        self.cap =0
        self.id = data
        self.right = None
        self.left = None
        self.height = 1
        self.link = bin
        self.store = [[store,self.link]]