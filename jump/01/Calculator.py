class Calculator:
  
  def __init__(self):
    pass
  def add(self, a, b):
    return a+b
  def sub(self, a, b):
    return a-b
  def mul(self, a, b):
    return a*b
  def div(self, a, b):
    return a/b
  
class SafeCalulator(Calculator):
  def __init__(self):
    pass
  def div(self, a, b):
    if(b>0):
      return a/b
    else:
      return -1

cal = SafeCalulator()
print(cal.add(1,2))
print(cal.mul(3,4))
print(cal.div(4,0))

try:
  cal2 = Calculator()
  print(cal2.div(10,0))
except ZeroDivisionError:
  print("영으로 나눌수 없습니다.")
finally:
  print("작업종료")