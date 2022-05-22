# 単方向リストの実装

# nodeは自分とnextを持つ
from http.client import NETWORK_AUTHENTICATION_REQUIRED


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    def display_node(self):
        print("[",self.data,"]",end="")

# 単方向リスト本体
class oneWayLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # リストの表示処理
    def display_list(self):
        print("head -> tail : ", end="")
        current = self.head
        # リストが空になるまで表示を続ける
        while current is not None:
            current.display_node()
            print("->", end="")
            current = current.next
        print("\n")
    
    # リストへの追加処理
    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            # まだ何もないならheadとtailがnew_nodeになる。
            self.head = new_node
            self.tail = new_node
        else:
            # 最後の要素のnextがnew_nodeになり、tailもnew_nodeになる
            self.tail.next = new_node
            self.tail = new_node
    # add_position(データ, 何番地に入れるか)
    
    def add_position(self,data,position):
        new_data = Node(data)
        current = self.head
        if position != 0:
            for i in range(0,position-1):
                current = current.next
            next_node = current.next
            current.next = new_data
            new_data.next = next_node
        else:
            next_node = self.head
            self.head = new_data
            current = self.head
            current.next = next_node

def main():
    hoge = oneWayLinkedList()
    for i in range(5):
        hoge.add(i)
    hoge.display_list()
    hoge.add_position("後入",5)
    hoge.display_list()



if __name__ == "__main__":
    main()