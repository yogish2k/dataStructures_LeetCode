class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child):
        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = BinaryTree(child)
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = BinaryTree(child)

    def search(self, val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def max_tree(self):
        if self.right:
            self.right.max_tree()
        else:
            print(self.data)

    def min_tree(self):
        if self.left:
            self.left.min_tree()
        else:
            print(self.data)

    def cal_sum(self):
        l_sum = self.left.cal_sum() if self.left else 0
        r_sum = self.right.cal_sum() if self.right else 0
        return self.data + l_sum + r_sum


def build_tree(elements):
    root = BinaryTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    number_tree = build_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.pre_order_traversal())
    print(number_tree.post_order_traversal())
    print(number_tree.search(210))
    number_tree.max_tree()
    number_tree.min_tree()
    print(number_tree.cal_sum())
