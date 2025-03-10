# 배열(리스트)를 기반으로 하는 완전이진트리를 구현하시오.

class BinaryTree:
    def __init__(self, data):
        self.data = [-1] + data # 첫번째 노드가 인덱스 1로 시작

    def preorder(self):
        def recursive(node):
            if node >= len(self.data):
                return
            # 현재 노드를 방문
            print(self.data[node], end=" ")
            # 왼쪽 자식 노드 방문
            recursive(2*node)
            # 오른쪽 자식 노드 방문
            recursive(2*node +1)

        recursive(1)
        print()

    def inorder(self):
        def recursive(node):
            if node >= len(self.data):
                return
            # 왼쪽 자식 노드 방문
            recursive(2*node)
            # 현재 노드를 방문
            print(self.data[node], end=" ")
            # 오른쪽 자식 노드 방문
            recursive(2*node +1)

        recursive(1)
        print()

    def postorder(self):
        def recursive(node):
            if node >= len(self.data):
                return
            # 왼쪽 자식 노드 방문
            recursive(2*node)
            # 오른쪽 자식 노드 방문
            recursive(2*node +1)
            # 현재 노드를 방문
            print(self.data[node], end=" ")

        recursive(1)
        print()

    def levelorder(self):
        for value in self.data[1:]:
            print(value, end=" ")
        print()
    
    # 레벨오더 방식으로 value 를 찾아가는 함수
    def bfs(self, value):
        for elem in self.data[1:]:
            if value == elem:
                return True
        return False

    # 프리오더 방식으로 value 를 찾아가는 함수
    def dfs(self, value):
        is_found = False
        def recursive(node):
            nonlocal is_found
            if node >= len(self.data):
                return
            if self.data[node] == value:
                is_found = True
                return
            if is_found:
                return
            # 왼쪽 자식 노드 방문
            recursive(2*node)
            # 오른쪽 자식 노드 방문
            recursive(2*node +1)
            # 현재 노드를 방문
            print(self.data[node], end=" ")

        recursive(1)
        print()
        return is_found

tree = BinaryTree([i for i in range(13)])
tree.preorder()
tree.inorder()
tree.postorder()
tree.levelorder()

print(tree.dfs(15))
print(tree.dfs(11))

print(tree.bfs(6))
print(tree.bfs(17))