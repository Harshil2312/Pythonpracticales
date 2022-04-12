# importing Thread cass
import threading
from threading import Thread


# Creating class to create thread
class Test(Thread):
    def run(self):
        print(Thread.getName(self))


# # creating objects of class Test
# t1 = Test()
# t2 = Test()
#
# # invoking the thread t1 and t2
# t1.start()
# t2.start()


# def method1():
#     print(f"From method1, thread name: {threading.currentThread().getName()}")
#
#
# def method2():
#     print(f"From method2, thread name: {threading.current_thread().getName()}")
#
#
# t1 = Thread(name="Thread_1", target=method1)
# t2 = Thread(name="Thread_2", target=method2)
# t3 = Thread()
#
# t1.start()
# t2.start()
# t3.start()


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

print(f"Before calling join method t1 thread alive or not {Thread.is_alive(t1)}")
print(f"Before calling join method t2 thread alive or not {Thread.is_alive(t2)}")

# join method called.
# Here join method called form main thread so main thread until t1 and t2 complete
t1.join()
t2.join()

print(f"After calling join method t1 thread alive or not {Thread.is_alive(t1)}")
print(f"After calling join method t2 thread alive or not {Thread.is_alive(t2)}")

# after completing t1 and t2 main thread continue its execution
for _ in range(1, 6):
    print(_)
print(f"{threading.currentThread().getName()} is ended")
