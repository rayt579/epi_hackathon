'''
Implement stack with a max, push, pop operations
'''
import collections

# O(N) space
class StackCached(object):
    ValueWithCachedMax = collections.namedtuple('ValueWithCachedMax', ('value','cached_max',))

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            raise Exception('Stack is empty')
        return self.stack.pop().value

    def push(self, value):
        self.stack.append(self.ValueWithCachedMax(value, value if len(self.stack) == 0 else max(value, self.max())))

    def max(self):
        if len(self.stack) == 0:
            raise Exception('Stack is empty')
        return self.stack[-1].cached_max

print('-----------------------')
print('Stack with all maxes cached')
print('-----------------------')
s = StackCached()
s.push(4)
s.push(15)
s.push(10)
s.push(16)
print('Expecting 16: {}'.format(s.max()))
s.pop()
print('Expecting 15: {}'.format(s.max()))
s.pop()
print('Expecting 15: {}'.format(s.max()))
s.pop()
print('Expecting 4: {}'.format(s.max()))
s.pop()


# Caches values greater than or equal to max value thus far

class MaxValueWithCount(object):
    def __init__(self, value):
        self.value = value
        self.count = 0

class Stack(object):
    def __init__(self):
        self.stack = []
        self.max_value_with_count = []

    def push(self, value):
        self.stack.append(value)
        if len(self.stack) == 1:
            self.max_value_with_count.append(MaxValueWithCount(value))
        else:
            if value > self.max_value_with_count[-1].value:
                self.max_value_with_count.append(MaxValueWithCount(value))
            elif value == self.max_value_with_count[-1].value:
                self.max_value_with_count[-1].count += 1

    def pop(self):
        if len(self.stack) == 0:
            raise Exception('Stack is empty!')

        if self.stack[-1] == self.max_value_with_count[-1].value:
            if self.max_value_with_count[-1].count == 0:
                self.max_value_with_count.pop()
            else:
                self.max_value_with_count[-1].count -= 1

        return self.stack.pop()

    def max(self):
        if len(self.stack) == 0:
            raise Exception('Stack is empty!')

        return self.max_value_with_count[-1].value

print('-----------------------')
print('Stack with selectively-cached maxes')
print('-----------------------')
s = Stack()
s.push(4)
s.push(15)
s.push(10)
s.push(16)
print('Expecting 16: {}'.format(s.max()))
s.pop()
print('Expecting 15: {}'.format(s.max()))
s.pop()
print('Expecting 15: {}'.format(s.max()))
s.pop()
print('Expecting 4: {}'.format(s.max()))
s.pop()
