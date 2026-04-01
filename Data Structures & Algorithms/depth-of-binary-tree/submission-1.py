import random
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     randomfunction = random.choice([self.recursive, self.dfs, self.bfs])
    #     return randomfunction(root)





        
    # def recursive(self, root):
    #     print("re")
    #     if not root:
    #         return 0
    #     return 1 + max(self.recursive(root.left), self.recursive(root.right))
        
    # def bfs(self, root):
    #     print("bfs")
    #     if not root:
    #         return 0
    #     levels = 0
    #     q = collections.deque([root])

    #     while q:
    #         for i in range(len(q)):
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
        
    #         levels += 1
        
    #     return levels
    
    # def dfs(self, root):
    #     print("dfs")

    #     stack = [[root, 1]]
    #     max_depth = 0

    #     while stack:
    #         node, depth = stack.pop()

    #         if node:
    #             max_depth = max(max_depth,depth)
    #             stack.append([node.left, depth+1])
    #             stack.append([node.right], depth+1)
        
    #     return max_depth




    def maxDepth(self, root):
        runfunc = random.choice([self.recursion, self.dfs, self.bfs])
        return runfunc(root)

    # def bfs(self, root):
    def recursion(self, root):
        print("re")
        if not root:
            return 0
        
        return 1 + max(self.recursion(root.left), self.recursion(root.right))
    
    def dfs(self, root):
        print("dfs")
        if not root:
            return 0
        
        stack = [[root, 1]]
        maxdepth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                maxdepth = max(maxdepth, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
            
        return maxdepth
    
    def bfs(self, root):
        print("bfs")
        if not root:
            return 0
        
        q = collections.deque([root])
        levels = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levels += 1
    
        return levels

