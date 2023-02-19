class Tree:
  leaves = 193829812931
  height = 10
  age = 10

  def __init__(self):
    print("")
  def get_older(self):
    self.age += 1
    self.leaves -= 10
    self.height += 10

my_tree = Tree()
print(my_tree.age, my_tree.leaves, my_tree.height)
my_tree.get_older()
print(my_tree.age, my_tree.leaves, my_tree.height)
