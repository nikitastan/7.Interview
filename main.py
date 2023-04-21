class Stack:
    def __init__(self):
        self.list_ = []

    def size(self):
        return len(self.list_)

    def is_empty(self):
        return len(self.list_) == 0

    def push(self,item):
        self.list_.append(item)

    def pop(self):
        return self.list_.pop()

    def peek(self):
        return self.list_[-1]


def brackets_check(ls):
    stack = Stack()
    dict_ = {'(': ')', '[': ']', '{': '}'}
    flag = 'Сбалансирован'
    if not len(ls)==0:
        for item in ls:
            if item in dict_.keys():
                stack.push(item)
                continue
            if item in dict_.values():
                    if stack.is_empty() or item != dict_[stack.pop()]:
                        flag = 'Не сбалансирован'
                        break
    return flag


if __name__ == '__main__':
    examples = ['',
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]']

    for ex in examples:
        print(f'Список "{ex}" - {brackets_check(ex)}')
