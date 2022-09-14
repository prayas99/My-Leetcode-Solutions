# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):        
        def bfs():
            s = str(root.val) + ','
            layer, q = 0, deque([root])
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                        s += str(node.left.val)
                    else:
                        s += '.'
                    s += ','
                    if node.right:
                        q.append(node.right)
                        s += str(node.right.val)
                    else:
                        s += '.'
                    s += ','
            return s
        if not root: return ''
        return bfs()

    def deserialize(self, data):
        data = data.split(',')[:-1]
        n = len(data)
        #print(data)
        if not data: return 
        def bfs():
            ans = TreeNode(data[0])
            i, q = 0, deque([ans])
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if i >= n - 1:
                        return ans
                    
                    if data[i + 1] != '.':
                        node.left = TreeNode(data[i + 1])
                        q.append(node.left)
                        
                    if data[i + 2] != '.':
                        node.right = TreeNode(data[i + 2])
                        q.append(node.right)
                    
                    i += 2
            return ans
        return bfs()
                    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))