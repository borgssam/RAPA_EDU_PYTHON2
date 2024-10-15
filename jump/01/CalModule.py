E = 2.71828 #오일러상수

class Math:
  def __init__(self):
    self.PI = 3.141592
  def areaCircle(self, r):
    return self.PI * r * r
  def aroundCircle(self,r):
    return self.PI* r*2

def add(a,b):
  return a+b

def sub(a,b):
  return a-b


# print(__name__)
if __name__ == "__main__":
  print(add(20,30))

  
  math = Math()
  print(math.areaCircle(10))