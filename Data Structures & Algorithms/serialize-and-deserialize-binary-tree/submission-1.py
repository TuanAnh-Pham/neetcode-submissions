# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'
        queue = deque([root])
        res = []
        while queue:
            nod = queue.popleft()
            if not nod:
                res.append('N')
            else:
                res.append(str(nod.val))
                queue.append(nod.left)
                queue.append(nod.right)
        return ','.join(res)        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        char  = data.split(',')
        if char[0] == 'N':
            return None

        index = 1
        root = TreeNode(int(char[0]))
        queue = deque([root])

        while queue:
            nod = queue.popleft()
            if char[index] != 'N':
                nod.left = TreeNode(int(char[index]))
                queue.append(nod.left)
            index += 1

            if char[index] != 'N':
                nod.right = TreeNode(int(char[index]))
                queue.append(nod.right)
            
            index +=1
        return root

