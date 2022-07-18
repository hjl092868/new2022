# -*- coding: utf-8 -*-


'''
从前序和中序结果返回二叉树
例如前序和中序分别为：
1 2 4 7 3 5 6 8
4 7 2 1 5 3 8 6
返回二叉树
参考https://blog.csdn.net/SEVENY_/article/details/82745802
上述网页的思路，找到每一个节点以及该节点的左子树和右子树
'''

class Tree():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return self.val


class Solution(object):
    def preorderTraversal(self, root):
        # 如果树为空返回空
        if root is None: return []
        # print(root.val)
        output = [root.val]
        output.extend(Solution.preorderTraversal(self, root.left))  # ['A', 'B', 'D', 'H', 'K']
        output.extend(Solution.preorderTraversal(self, root.right))  # ['A', 'C', 'G', 'J']
        return output

    # 中序
    def inrderTraversal(self, root):
        # 如果树为空返回空
        if root is None: return []
        # print(root.val)
        output = []
        output.extend(Solution.inrderTraversal(self, root.left))  # ['A', 'B', 'D', 'H', 'K']
        output.extend(root.val)
        output.extend(Solution.inrderTraversal(self, root.right))  # ['A', 'C', 'G', 'J']
        return output

    # 后序
    def postorderTraversal(self, root):
        # 如果树为空返回空
        if root is None: return []
        # print(root.val)
        output = []
        output.extend(Solution.postorderTraversal(self, root.left))  # ['A', 'B', 'D', 'H', 'K']
        output.extend(Solution.postorderTraversal(self, root.right))  # ['A', 'C', 'G', 'J']
        output.extend(root.val)
        return output


# def recover_tree(str1: str, str2: str, root_inner=None):
#     root_str = str1[0]
#     if root_inner == None:
#         root = Tree(root_str)
#     else:
#         root = root_inner
#
#     if len(str1) == len(str2) == 2:
#         # root_in = Tree(str1[0])
#         root_in = root
#         if str1 == str2:
#             # root_in.left = str1[1]
#             # root_in.right = Tree(str1[1])
#             right_t = Tree(str1[1])
#             root_in.right = right_t
#             print('111-{}（id为{}）的右是{}（id为{}）'.format(root_in, id(root_in), right_t, id(right_t)))
#         else:
#             # root_in.right = str1[1]
#             # root_in.left = Tree(str1[1])
#             left_t = Tree(str1[1])
#             root_in.left = left_t
#             print('222-{}（id为{}）的左是{}（id为{}）'.format(root_in, id(root_in), left_t, id(left_t)))
#         # return root
#         return
#
#     zuo = str2.split(root_str)[0]
#     if len(zuo) >= 2:
#         # root.left = str1[1:][:len(zuo)][0]
#         root_left = Tree(str1[1:][:len(zuo)][0])
#         root.left = root_left
#         print('333-{}（id为{}）的左是{}（id为{}）'.format(root, id(root), root_left, id(root_left)))
#         recover_tree(str1[1:][:len(zuo)], zuo, root_left)
#     elif len(zuo) == 1:
#         # root.left = str1[1:][:len(zuo)][0]
#         # root.left = Tree(str1[1:][:len(zuo)][0])
#         left_t = Tree(str1[1:][:len(zuo)][0])
#         root.left = left_t
#         print('444-{}（id为{}）的左是{}（id为{}）'.format(root, id(root), left_t, id(left_t)))
#         # print(111, len(zuo))
#
#     you = str2.split(root_str)[1]
#     if len(you) >= 2:
#         # root.right = str1[1:][len(zuo):][0]
#         root_right = Tree(str1[1:][len(zuo):][0])
#         root.right = root_right
#         print('555-{}（id为{}）的右是{}（id为{}）'.format(root, id(root), root_right, id(root_right)))
#         recover_tree(str1[1:][len(zuo):], you, root_right)
#     elif len(you) == 1:
#         # root.right = str1[1:][len(zuo):][0]
#         # root.right = Tree(str1[1:][len(zuo):][0])
#         right_t = Tree(str1[1:][len(zuo):][0])
#         root.right = right_t
#         print('666-{}（id为{}）的右是{}（id为{}）'.format(root, id(root), right_t, id(right_t)))
#         # print(222, len(you))


def recover_tree(str1: str, str2: str, root_inner=None):
    root_str = str1[0]
    if root_inner == None:
        root = Tree(root_str)
    else:
        root = root_inner

    if len(str1) == len(str2) == 2:
        root_in = root
        if str1 == str2:
            right_t = Tree(str1[1])
            root_in.right = right_t
        else:
            left_t = Tree(str1[1])
            root_in.left = left_t
        return

    zuo = str2.split(root_str)[0]
    if len(zuo) >= 2:
        root_left = Tree(str1[1:][:len(zuo)][0])
        root.left = root_left
        recover_tree(str1[1:][:len(zuo)], zuo, root_left)
    elif len(zuo) == 1:
        left_t = Tree(str1[1:][:len(zuo)][0])
        root.left = left_t

    you = str2.split(root_str)[1]
    if len(you) >= 2:
        root_right = Tree(str1[1:][len(zuo):][0])
        root.right = root_right
        recover_tree(str1[1:][len(zuo):], you, root_right)
    elif len(you) == 1:
        right_t = Tree(str1[1:][len(zuo):][0])
        root.right = right_t


str_1 = '12473568'
str_2 = '47215386'
root_ori = Tree(str_1[0])
recover_tree(str_1, str_2, root_ori)
s = Solution()
a = s.postorderTraversal(root_ori)
print(a)
