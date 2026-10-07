def add(a,b):
    return a+b
def max_of(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c
def greet(name="同学"):
    return "你好"+name

print(greet("大金"))
print(greet())
print(add(2,3))
print(max_of(99,66,77))