# -*- coding: utf-8 _8-
# 参考 https://blog.csdn.net/weixin_43786241/article/details/108327747

# 二叉树-前序遍历
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        # print(x)

    def __str__(self):
        return self.val


class Solution(object):
    def preorderTraversal(self, root):
        # 如果树为空返回空
        if root is None: return []
        print(root.val)
        output = [root.val]
        output.extend(Solution.preorderTraversal(self, root.left))  # ['A', 'B', 'D', 'H', 'K']
        output.extend(Solution.preorderTraversal(self, root.right))  # ['A', 'C', 'G', 'J']
        return output

    # 中序
    def inrderTraversal(self, root):
        # 如果树为空返回空
        if root is None: return []
        print(root.val)
        output = []
        output.extend(Solution.inrderTraversal(self, root.left))  # ['A', 'B', 'D', 'H', 'K']
        output.extend(root.val)
        output.extend(Solution.inrderTraversal(self, root.right))  # ['A', 'C', 'G', 'J']
        return output

    # 后序
    def postorderTraversal(self, root):
        # 如果树为空返回空
        if root is None: return []
        print(root.val)
        output = []
        output.extend(Solution.postorderTraversal(self, root.left))  # ['A', 'B', 'D', 'H', 'K']
        output.extend(Solution.postorderTraversal(self, root.right))  # ['A', 'C', 'G', 'J']
        output.extend(root.val)
        return output



A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')
H = TreeNode('H')
I = TreeNode('I')
J = TreeNode('J')
K = TreeNode('K')

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G
D.left = H
F.left = I
G.right = J
H.left = K


s = Solution()
a = s.preorderTraversal(A)
print(a)
