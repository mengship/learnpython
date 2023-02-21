class Stack(object):
    items = []

    # 初始化
    def __int__(self):
        pass

    # 栈为空
    def is_empty(self):
        return len(self.items) == 0

    # 返回栈顶元素
    def front(self):
        return self.items[-1]

    # 返回栈元素大小
    def size(self):
        return len(self.items)

    # 入栈
    def push(self, num):
        self.items.append(num)

    # 出栈
    def pop(self):
        self.items.pop()


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push('h')
    my_stack.push('e')
    my_stack.push('l')
    my_stack.push('l')
    my_stack.push('o')
    print(my_stack.size())
    print(my_stack.front())
    my_stack.pop()
    print(my_stack.front())
    my_stack.pop()
    print(my_stack.front())
    print(my_stack.size())
    print(my_stack.is_empty())
