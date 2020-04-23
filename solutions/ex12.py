'''
Implement a class for a stack that supports all the regular
functions (push, pop) and an additional function of max() which returns the
maximum element in the stack (return None if the stack is empty).
Each method should run in constant time.
'''


class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxValue = [None]
        return

    def push(self, val):
        self.stack.append(val)

        if(self.maxValue[0] is None):
            self.maxValue[0] = val
        elif(val > self.maxValue[-1]):
            self.maxValue.append(val)
        else:
            self.maxValue.append(self.maxValue[-1])
        return

    def pop(self):
        del(self.stack[-1])
        del(self.maxValue[-1])
        return

    def max(self):
        return self.maxValue[-1]


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
