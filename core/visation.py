
#setup the vistor methods basee and abstract classmethod
#i want this to visit entities, be ussable for animation updates!

class visitor:
    def __init__(self):
        pass

class component:

    @abstractmethod
    def accept(self, visitor: visitor) -> None:
        pass
