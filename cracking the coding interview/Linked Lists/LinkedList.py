class Node():

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        # return "{} | {}".format(self.data, self.next)
        return f"data: {self.data}, next: {self.next.data}"


class LinkedList():
    ''' A well tested implimentation of Linked List
        Warning: This code only works on Python versions
                later than 3.6.0 because the code contains
                f-strings

        TODO: refactor the entire code to remove print statements and replace them with throwing errors

        also, add some functions like 'isempty()' that return something


    '''

    def __init__(self, *args):
        self.head = None

        if args:
            self.head = Node(args[0])
            curr = self.head
            for ele in args[1:]:
                curr.next = Node(ele)
                curr = curr.next

    def isempty(self):
        if self.head is None:
            return 1
        else:
            return 0

    def insert(self, data, index=None):
        # sanitary checks
        assert type(index) is int or index is None, "Please enter an Integer index"

        if self.head is None:
            self.head = Node(data)

        else:
            if index is None:  # append at the end
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                curr.next = Node(data)

            elif index == 0:  # prepend (at the beginning)
                self.head = Node(data=data, next=self.head)

            elif index > 0:  # insert at the specified index
                curr = self.head

                try:
                    for _ in range(index - 1):
                        curr = curr.next
                    curr.next = Node(data=data, next=curr.next)

                except AttributeError:  # if index is out of range
                    print(f"Index out of Range")

                except TypeError:  # if index in not an integer (index is float)
                    print(f"Please give a valid Integer Index")

            else:
                print("Please give a valid positive Integer Index")

    def delete(self, data=None, index=None):
        if self.head is None:
            # Should I raise an error instead of just printing?
            print("The LinkedList has no elements to delete")
            return

        if data is not None and index is not None:
            print("You cannot give both data and index at the same time")
            return

        else:
            if index is None:  # delete the first occurance of data

                if self.head.data == data:  # check at the beginning
                    node_to_delete = self.head
                    self.head = self.head.next
                    del node_to_delete
                    return

                # if required data is not at the beginning then search the list and delete if found
                curr = self.head

                while curr.next is not None:
                    if curr.next.data != data:
                        curr = curr.next
                    else:
                        break

                try:
                    node_to_delete = curr.next
                    curr.next = curr.next.next
                    del node_to_delete

                except AttributeError:  # element not found in the list
                    print(f"The element '{data}' is not found in the list")

            elif index == 0:  # delete at the beginning
                node_to_delete = self.head
                self.head = self.head.next
                del node_to_delete

            elif index > 0:  # delete at the specified index
                curr = self.head

                try:
                    for _ in range(index - 1):
                        curr = curr.next
                    node_to_delete = curr.next
                    curr.next = curr.next.next
                    del node_to_delete

                except AttributeError:  # if index is out of range
                    print(f"Index out of Range")

                except TypeError:  # if index in not an integer
                    print(f"Please give a valid Integer Index")

            else:
                print("Please give a valid positive Integer Index")

    def find(self, data):  # prints the first occurance of the element
        if self.head is None:
            print("The LinkedList is empty")
            return

        curr = self.head
        index = 0
        while curr.next is not None:  # checks till the 2nd last element
            if curr.data == data:
                print(f"Found at index: {index}")
                return

            curr = curr.next
            index += 1

        # checking the last element
        if curr.data == data:
            print(f"Found at index: {index}")
            return

        # else
        print("The element is not in the LinkedList")

    def fetch(self, index):  # returns the data at the specified index
        if self.head is None:
            print("The LinkedList is empty")
            return

        if index < 0:
            print("Please give a valid positive index")
            return

        curr = self.head
        try:
            for _ in range(index):
                curr = curr.next

            return curr.data

        except AttributeError:
            print("Index out of range")
            return

    # nice representation for the interpreter
    def __repr__(self):
        nodes_data = []

        curr = self.head
        if curr is None:
            return 'Empty LinkedList'

        while curr.next is not None:
            nodes_data.append(str(curr.data))
            curr = curr.next
        nodes_data.append(str(curr.data))

        return ' -> '.join(nodes_data)

    # iterator for "for-in" loops
    def __iter__(self):
        return LinkedListIterator(self.head)


# Iterator class
class LinkedListIterator():

    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current == None:
            raise StopIteration

        else:
            item = self.current.data
            self.current = self.current.next
            return item


if __name__ == '__main__':
    l = LinkedList()

    l.insert(10)
    l.insert(15)
    l.insert(68)
    l.insert(4)
    l.insert(15)
    l.insert(0)
    l.insert(69)
