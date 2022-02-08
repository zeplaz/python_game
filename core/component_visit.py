
#setup the vistor methods basee and abstract classmethod
#i want this to visit entities, be ussable for animation updates!

class visitor:
    def __init__(self):
        pass

class componatable:
	def __init__():
		self.components = []

	def add_component(self, incomp):
		lastorder = 0
        if self.components:
    		for x in self.components:
    			lastorder +=1
    			if self.update_order < x.update_order:
    				break;
		self.components.insert(lastorder,incomp)

	def remove_compoent(self,outcomp):
		if outcomp in self.components:
			self.components.remove(outcomp)

class component:
    def __del__(self):
        self.myowner.remove_compoent(self)

    def __init__(self, priory, owner):
        self.update_order = -1
        self.myowner = owner
        self.myowner.add_component(self)

    @property
    def update_order(self):
        return self.mupdate_order

    @update_order.setter
    def update_order(self, uo):
        self.mupdate_order = uo

    @abstractmethod
    def Update( dt):
        pass

    @abstractmethod
    def accept(self, visitor: visitor) -> None:
        pass
