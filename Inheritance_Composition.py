class Parent(object):
	"""docstring for Parent"""
	def overrite(seft):
		print("PARENT overrite")

	def implicit(seft):
		print("PARENT implicit")

	def altered(seft):
		print("PARENT altered")

class Child(Parent):
	def overrite(seft):
		print("CHILD overrite")

	def altered(seft):
		print("Child before altered")
		super(Child, seft).altered()
		print("Child before altered")

dad = Parent()
child = Child()

dad.implicit()
child.implicit()

dad.overrite()
child.overrite()

dad.altered()
child.altered()

class Other(object):
	def overrite(seft):
		print("Other overrite")

class TestOther(object):
	"""docstring for TestOther"""
	def __init__(self):
		self.other = Other()

	def overrite(seft):
		seft.other.overrite()
		print("Test overrite")

test = TestOther()
test.overrite()