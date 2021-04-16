# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        # Method 1 : Using Hashmap (recursion)
        
        # Time : O(n) , traversing entire tree, and hashmap
        # clearing output list multiple times will also take O(n) maximum
        # Space : O(n), stack space + hashmap
        
        # self.prev_count = float('-inf')
        # self.prev_val = inf('-inf')
        self.hashmap = {}
        self.dfs(root)
        print(self.hashmap)
        
        maxval = 0
        output = []
        for key,val in self.hashmap.items():
            if val>maxval: # if max value is updated, clear output list
                output.clear()
                output.append(key)
                maxval = val
            elif val == maxval:
                output.append(key)            
        return output
    
    
    def dfs(self,root):
        
        if root == None:
            return
        
        self.dfs(root.left)
        if root.val not in self.hashmap:
            self.hashmap[root.val] = 1
        else:
            self.hashmap[root.val]+=1
        self.dfs(root.right)
            
            
        # Method 2 : Without extra space
        
        
        