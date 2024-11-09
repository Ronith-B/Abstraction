
from abc import ABC, abstractmethod


class Absclass(ABC):
    
 
    def print(self, Hello):
        print("Passed value:", Hello)

   
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")


class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)
