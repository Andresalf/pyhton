from abc import ABCMeta, abstractmethod

class BinaryTree(metaclass = ABCMeta):
    def __init__(self):
        self.root = None

    @abstractmethod
    def insert(self, data):
        pass

