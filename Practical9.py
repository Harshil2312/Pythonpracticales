#!/usr/bin/env python
# coding: utf-8

# # Practical 9

# Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. The Student class has data members such as those representing rollNumber, Name, etc. Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects. Derive Result from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this relationship.

# In[1]:


from threading import Thread
import threading

class Test1(Thread):

    # set the name of thread
    def __init__(self, thread_name):
        Thread.__init__(self, name=thread_name)

    # The run method is overridden to define the thread body
    def run(self):
        print(f"{Thread.getName(self)} is started:")
        for _ in range(1, 6):
            print(f"{_}")
        print(f"{Thread.getName(self)} is ended.")


print(f"{threading.currentThread().getName()} is starting")
# Creating The object of test class
t1 = Test1("child_thread_1")
t2 = Test1("child_thread_2")

# invoking or stating the threads
t1.start()
t2.start()

# join method called.
# Here join method called form main thread so main thread until t1 and t2 complete
t1.join()
t2.join()

# after completing t1 and t2 main thread continue its execution
for _ in range(1, 6):
    print(_)
print(f"{threading.currentThread().getName()} is ended")


# In[ ]:





# In[ ]:





# In[ ]:




