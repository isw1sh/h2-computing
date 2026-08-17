#Task 3.1
class Node:
    def __init__(self,value, left = None , right = None):
        self.left = left
        self.right = right
        self.value = int(value)
        
class Tree:
    def __init__(self,node):
        self.root = node
    
    def insert(self,value):
        if self.root is None:
            return "BST is empty"
        
        else:
            cur = self.root
            
        while True:
            if value.value < cur.value:
                if cur.left is None:
                    cur.left = value
                    return value , 'inserted'
                else:
                    cur = cur.left
                    
            else:
                if cur.right is None:
                    cur.right = value
                    return value , 'inserted'
                else:
                    cur = cur.right 
                    
    def in_order_traversal(self):
        self.in_order_recursive(self.root)
        
    def in_order_recursive(self, node):
        if node is not None:
            self.in_order_recursive(node.left)
            print(node.value, end=' ')
            self.in_order_recursive(node.right)
    
    def pre_order(self,node,result):
        if node:
            result.append(node.value)
        self.pre_order(node.left, result)
        self.pre_order(node.right , result)
        
    def pre_order_traversal(self):
        result = []
        self.pre_order(self.root , result)
        return result 
    
    def helper(self,node,prev):
        if node == None:
            return prev
        
        prev = self.helper(node.right , prev)
       
        
    
    
        
tree = Tree(Node(70))
for v in [50, 30, 20, 40, 60, 80]:
    tree.insert(Node(v))

tree.in_order_traversal() 

 
        