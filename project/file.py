import pydot


class functionalStructure:
	"""docstring for functionalStructure"""
	def __init__(self):
		self.graph = pydot.Dot(graph_type='digraph')
		self.head = "CEO"
		self.director = []
		self.manager = []
		self.operationalManager = []
		self.staff = []


	def addDirector(self, lst):
	 	self.director = lst
	 	for i in range(len(self.director)):
	 		edge = pydot.Edge(self.head, self.director[i])
	 		self.graph.add_edge(edge)


	def addManager(self, lst):
	 	self.manager = lst
	 	if len(self.director) == 0:
		 	for i in range(len(self.manager)):
		 		edge = pydot.Edge(self.head, self.manager[i])
		 		self.graph.add_edge(edge)
	 	else:
		 	j = 0
		 	for i in range(len(self.manager)):
		 		if j == len(self.director):
		 			j = 0
		 		edge = pydot.Edge(self.director[j], self.manager[i])
		 		self.graph.add_edge(edge)
		 		j += 1


	def addOperationalManager(self,lst):
	 	self.operationalManager = lst
	 	if len(self.manager)== 0:
		 	j = 0
		 	for i in range(len(self.operationalManager)):
		 		if j == len(self.director):
		 			j = 0
		 		edge = pydot.Edge(self.director[j], self.operationalManager[i])
		 		self.graph.add_edge(edge)
		 		j += 1
	 	else:
		 	j = 0
		 	for k in range(len(self.operationalManager)):
		 		if j == len(self.manager):
		 			j = 0
		 		edge = pydot.Edge(self.manager[j], self.operationalManager[k])
		 		self.graph.add_edge(edge)
		 		j += 1



	def addStaff(self, lst):
		self.staff = lst
		j = 0
		if len(self.operationalManager) == 0:
			for i in range(len(self.staff)):
				if j == len(self.manager):
					j = 0
				edge = pydot.Edge(self.manager[j], self.staff[i])
				self.graph.add_edge(edge)
				j += 1
		else:
			for k in range(len(self.staff)):
				if j == len(self.operationalManager):
					j = 0
				edge = pydot.Edge(self.operationalManager[j], self.staff[k])
				self.graph.add_edge(edge)
				j += 1


	def drawGraph(self):
		self.graph.write_png('first.png')





class GeographicStructure:
	"""docstring for GeographicStructure"""
	def __init__(self):
		self.graph = pydot.Dot(graph_type='digraph')
		self.head = "President"
		self.region = []
		self.product = []
		self.manager = []
		self.operationalManager = []
		self.staff = []


	def addRegion(self, lst):
	 	self.region = lst
	 	for i in range(len(self.region)):
	 		edge = pydot.Edge(self.head, self.region[i])
	 		self.graph.add_edge(edge)


	def addManager(self, lst):
	 	self.manager = lst
	 	if len(self.product) == 0:
	 		for j in range(len(self.region)):
			 	for i in range(len(self.manager)):
			 		edge = pydot.Edge(self.region[j], self.manager[i])
			 		self.graph.add_edge(edge)
	 	else:
		 	for j in range(len(self.product)):
			 	for i in range(len(self.manager)):
			 		edge = pydot.Edge(self.product[j], self.manager[i])
			 		self.graph.add_edge(edge)


	def addProduct(self,lst):
	 	self.product = lst
	 	if len(self.region)== 0:
		 	for i in range(len(self.product)):
		 		edge = pydot.Edge(self.head, self.product[i])
		 		self.graph.add_edge(edge)
	 	else:
		 	for j in range(len(self.region)):
			 	for k in range(len(self.product)):
			 		edge = pydot.Edge(self.region[j], self.product[k])
			 		self.graph.add_edge(edge)



	def addOperationalManager(self, lst):
	 	self.operationalManager = lst
	 	if len(self.manager) == 0:
	 		for j in range(len(self.product)):
			 	for i in range(len(self.operationalManager)):
			 		edge = pydot.Edge(self.product[j], self.operationalManager[i])
			 		self.graph.add_edge(edge)
	 	else:
		 	
		 	for i in range(len(self.operationalManager)):
		 		edge = pydot.Edge(self.manager[i], self.operationalManager[i])
		 		self.graph.add_edge(edge)


	def addStaff(self, lst):
		self.staff = lst
		j = 0
		if len(self.operationalManager) == 0:
			for i in range(len(self.staff)):
				edge = pydot.Edge(self.manager[i], self.staff[i])
				self.graph.add_edge(edge)
		else:
			for k in range(len(self.staff)):
				edge = pydot.Edge(self.operationalManager[k], self.staff[k])
				self.graph.add_edge(edge)


	def drawGraph(self):
		self.graph.write_png('first.png')



		




# if "__name__" == "__main__": 
# obj = functionalStructure()
# print("heloo world")
# lst = ["director1",'director2']
# obj.addDirector(lst)
# # lst = ["manager1", "manager2", "manager3","manager4"]
# # obj.addManager(lst)
# lst = ["operationalManager1","operationalManager2", "operationalManager3"]
# obj.addOperationalManager(lst)
# obj.drawGraph()





