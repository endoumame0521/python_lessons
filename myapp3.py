# クラスの多重継承
# A, B ->

class A:
  def say_a(self):
    print("A!")
  def say_hi(self):
    print("hi! from A!")

class B:
  def say_b(self):
    print("B!")
  def say_hi(self):
    print("hi! from B!")

# class C(A, B):
class C(B, A):
  pass

c = C()
# c.say_a()
# c.say_b()
c.say_hi()