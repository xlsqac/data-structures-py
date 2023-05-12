from singly_linked_list import SinglyLinkedList


def main():
    link_list = SinglyLinkedList()
    link_list.append(1)
    link_list.append(2)
    link_list.add(3)
    link_list.insert(2, 4)
    link_list.travel()
    link_list.remove(2)
    print("")
    link_list.travel()
    print(link_list.length())
    print(link_list.search(5))
    print(link_list.search(3))


if __name__ == "__main__":
    main()
