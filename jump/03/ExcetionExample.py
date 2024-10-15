class MyError(Exception):
  def __init__(self):
    self.message = "양수만 가능"
  def __init__(self,message):
    self.message = message
  def __str__(self):
    return self.message
  

def check_positive(num):
  if(num < 0):
    raise MyError("음수 입력불가")
  else:
    print(f"{num}은 양수입니다.")

try:
  check_positive(-10)
except MyError as e:
  print(f"에러발생: {e}")
