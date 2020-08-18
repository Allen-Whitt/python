# Classes in Python
class Point:
	# Self references itself in memory
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def move(self):
		print("move")
	
	def draw(self):
		print("draw")


# Inheritance
class Line(Point):
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
