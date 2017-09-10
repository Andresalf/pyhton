from abc import ABCMeta, abstractmethod

class BinaryTree(metaclass = ABCMeta):
    @abstractmethod
    def insert(self, data):
        pass
