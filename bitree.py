"""
二叉树的构建与遍历
重点代码
"""


# 　二叉树的节点类
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 二叉树类,进行遍历操作
class Bitree:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    #　先序遍历
    def preOrder(self,node):
        if node is None:
            return
        print(node.data,end=' ')
        self.preOrder(node.left)
        self.preOrder(node.right)

    #　中序遍历
    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data, end=' ')
        self.inOrder(node.right)

    # 　后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end=' ')


if __name__ == "__main__":
    #   按照后序遍历增加结点
    b = TreeNode('B')
    f = TreeNode('F')
    g = TreeNode('G')
    d = TreeNode('D', f, g)
    i = TreeNode('I')
    h = TreeNode('H')
    e = TreeNode('E', i, h)
    c = TreeNode('C', d, e)
    a = TreeNode('A', b, c)  # 根节点

    bt = Bitree(a)  # 初始化树对象，传入根结点

    print("pre order .....")
    bt.preOrder(bt.root)
    print()
    print("in order .....")
    bt.inOrder(bt.root)
    print()
    print("post order .....")
    bt.postOrder(bt.root)
    print()
