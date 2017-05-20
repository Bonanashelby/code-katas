"""Grasshopper if/else syntax debug. 

Best Practices jmeridth & others

def checkAlive(health):
    return health > 0
"""


def checkAlive(health):
  if health > 0:
      return True
  else:
      return False
  print(health)