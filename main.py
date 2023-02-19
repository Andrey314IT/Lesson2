class Tree:
  leaves = 193829812931
  height = 10
  age = 10

  def __init__(self, type):
    self.type = type
  def get_older(self):
    self.age += 1
    self.leaves -= 10
    self.height += 10

my_tree = Tree("Akacia")
print(my_tree.age, my_tree.leaves, my_tree.height)
print(my_tree.type)
my_tree.get_older()
print(my_tree.age, my_tree.leaves, my_tree.height)
