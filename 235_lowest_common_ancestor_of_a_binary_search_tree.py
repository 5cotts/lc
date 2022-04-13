# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ### 5cotts SOLUTION
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Head right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # Head left
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            # If none of the above are true, we must have arrived at the LCA.
            # This is the definition of "the lowest node T that has both p and
            # q as descendants (where we allow a node to be a descendant of itself)""
            return root
    
    ### OTHER SOLUTION
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = []
        qPath = []

        parents = {root.val: None}

        stack = [root]

        while stack:
            currentNode = stack.pop()

            if currentNode.left != None:
                stack.append(currentNode.left)
                parents[currentNode.left.val] = currentNode
            if currentNode.right != None:
                stack.append(currentNode.right)
                parents[currentNode.right.val] = currentNode

            if currentNode == p:
                temp = currentNode
                while parents[temp.val] != None:
                    pPath.append(temp)
                    temp = parents[temp.val]
                pPath.append(temp)
                pPath.reverse()
            if currentNode == q:
                temp = currentNode
                while parents[temp.val] != None:
                    qPath.append(temp)
                    temp = parents[temp.val]
                qPath.append(temp)
                qPath.reverse()

        prev = None
        for pVal, qVal in zip(pPath, qPath):
            if pVal is not qVal:
                return prev
            prev = pVal
        return prev
