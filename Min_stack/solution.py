class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack1 = []
        self.minStack = []

    def push(self, number):
        # write yout code here
        self.stack1.append(number)
        if self.minStack:
            curMin = self.minStack[-1]
            if number <= curMin:
                self.minStack.append(number)
        else:
            self.minStack.append(number)

    def pop(self):
        # pop and return the top item in stack
        c = self.stack1.pop()
        curMin = self.minStack[-1]
        if c == curMin:
            self.minStack.pop()
        return c

    def min(self):
        # return the minimum number in stack
        return self.minStack[-1]
