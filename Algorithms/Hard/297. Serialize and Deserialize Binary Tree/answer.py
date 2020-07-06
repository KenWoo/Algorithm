from tying import List

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        def preOrder(node):
            if not node:
                res.append('#')
            else:
                res.append(str(node.val))
                preOrder(node.left)
                preOrder(node.right)
        preOrder(root)
        return ','.join(res)
        

    def deserialize(self, data):
        arr = data.split(',')
        def build():
            if arr:
                value = arr.pop(0)
                if value == '#':
                    return None
                node = TreeNode(int(value))
                node.left = build()
                node.right = build()
                return node
        return build()

        

if __name__ == "__main__":
    pass