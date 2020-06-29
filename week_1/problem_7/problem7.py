#! /usr/bin/python3


class Polygon:
	def __init__(self, no_of_edges, len_of_edges):
		self.no_of_edges = no_of_edges
		self.len_of_edges = list()
		self.len_of_edges = len_of_edges
		self.s = 0.0
		self.p = 0.0

	def area(self):
		return 'area() method of polygon'

	def perimeter(self):
		return 'perimeter() method of Polygon'


class Triangle(Polygon):
	def __init__(self, len_of_edges):
		super().__init__(3, len_of_edges)
		self.p = sum(self.len_of_edges)

	def area(self):
		wk1 = self.p / 2
		wk2 = wk1
		for it in self.len_of_edges:
			wk2 *= (wk1 - it)
		self.s = wk2 ** (0.5)

		return self.s

	def perimeter(self):
		return self.p


class Quadrilateral(Polygon):
	def __init__(self,  len_of_edges):
		super().__init__(4, len_of_edges)

	def area(self):
		return 'area() method of Quadrilateral'

	def perimeter(self):
		return 'perimeter() method of Quadrilateral'


class Pentagol(Polygon):
	def __init__(self,  len_of_edges):
		super().__init__(5, len_of_edges)

	def area(self):
		return 'area() method of Pentagol'

	def perimeter(self):
		return 'perimeter() method of Pentagol'


class Hexagol(Polygon):
	def __init__(self,  len_of_edges):
		super().__init__(6, len_of_edges)

	def area(self):
		return 'area() method of Hexagol'

	def perimeter(self):
		return 'perimeter() method of Hexagol'


print('Start....')
t1 = Triangle([3,4,5])
print('t1: area is {:.2f}, perimeter is {:.2f}'.format(t1.area(), t1.perimeter()))
