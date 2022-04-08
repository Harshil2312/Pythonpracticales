#!/usr/bin/env python
# coding: utf-8

# # Stack 

# In[1]:


# script to implement Stack data structure
class Stack:
    __stack = []

    # push method to add element to stack
    def push(self, value):
        self.__stack.append(value)

    # pop method to remove element from stack
    def pop(self):
        return self.__stack.pop()

    # peek method to return top element of stack
    def peek(self):
        return self.__stack[-1]

    # is_empty method to check if stack is empty
    def is_empty(self):
        return self.__stack == []

    # is_full method to check if stack is full(assume stack size is 10)
    def is_full(self):
        return len(self.__stack) == 10

    # size method to return size of stack
    def size(self):
        return len(self.__stack)

    #  print_stack method to print stack
    def print_stack(self):
        print(self.__stack)


# In[2]:


# Test
# Creating Object
s = Stack()

# Pushing elements
s.push(23)
s.push(99)
s.push(89)
s.push(45)
s.push(11)
s.push(67)

# Performing Different operation
print(s.pop())
print(s.size())
print(s.is_empty())
print(s.is_full())
print(s.pop())
print(s.peek())
print(s.print_stack())

