class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Double_List:
    def __init__(self):
        self.num = 0
        self.head = None
        self.tail = None

    def print_detail(self):
        current = self.head
        i = 0
        # 1番地以降
        while current is not None:
            if current.prev is None:
                print(i, "番地(head):", current.data, "| prev = None ", "next =", current.next.data)
            elif current.next is None:
                print(i, "番地(tail):", current.data, "| prev =",current.prev.data, "    next = None")
                break
            else:
                print(i, "番地      :", current.data, "| prev =",current.prev.data, "    next =", current.next.data)
            current = current.next
            i += 1

    def print_doubleList(self):
        print("(", self.num, "個のNode) " "[first -> last]" )
        current = self.head
        print("head -> ", end="")
        while current is not None:
            print("[", current.data, "]", end="")
            if current==self.tail:
                break
            elif self.tail is None:
                break
            print(" <-> ", end="")
            current = current.next
        print(" <- tail")
        print()

    def add(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = None
            self.num += 1
        else:
            self.tail.next = new_node
            self.tail.next.prev = self.tail
            self.tail = new_node
            self.num += 1

    def pos_add(self, pos, data):
        new_node = Node(data)
        # 半分より手前の番地に追加
        if pos <= self.num/2:
            current = self.head
            # head
            if pos == 0:
                self.head = new_node
                self.head.next = current
                current.prev = self.head
                self.num += 1
            # error
            elif pos < 0:
                print(pos, "番地にノードを追加することはできません。")    
            # head以外
            else:
                for i in range(pos):
                    c_prev = current
                    current = current.next
                current.prev = new_node
                current.prev.next = current
                c_prev.next = new_node
                c_prev.next.prev = c_prev
                self.num += 1
        # 半分より奥の番地に追加
        else:
            current = self.tail
            # tail
            if pos == self.num:
                self.add(data)
            # error
            elif pos > self.num:
                print("要素数", self.num, "なので", pos, "番地にノードを追加することはできません。")    
            # tail以外
            else:
                for i in range(self.num - pos):
                    c_next = current
                    current = current.prev
                current.next = new_node
                current.next.prev = current
                c_next.prev = new_node
                c_next.prev.next = c_next
                self.num += 1                

    def rm_head(self):
        print("remove head")
        current = self.head
        if self.head is not None:
            if self.head.next is not None:
                self.head = current.next
                current.next.prev = None
                self.num -= 1
            else:
                self.head = None
                self.tail = None
                self.num -= 1

    def rm_tail(self):
        print("remove tail")
        current = self.tail
        if self.tail is not None:
            if self.tail.prev is not None:
                self.tail = current.prev
                current.prev.next = None
                self.num -= 1
            else:
                self.head = None
                self.tail = None
                self.num -= 1

    # def rm_node(self,pos):


def main():
    print("run double_list.py")
    d_list = Double_List()
    for i in range(7):
        d_list.add("No:{:1d}".format(i))

    d_list.print_detail()
    d_list.rm_head()
    d_list.rm_tail()
    d_list.print_detail()
    d_list.print_doubleList()


if __name__ == "__main__":
    main()