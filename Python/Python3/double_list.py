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


def main():
    print("run double_list.py")
    # 空のdoublelist作成（インスタンス化）
    d_list = Double_List()
    for i in range(7):
        d_list.add("No:{:1d}".format(i))

    d_list.print_doubleList()
    d_list.print_detail()
    

if __name__ == "__main__":
    main()
