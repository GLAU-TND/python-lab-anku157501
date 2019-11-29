try:
    a=5
    b="python"
    c=a+b
except TypeError:
    print("TypeError occur")
else:
    print("success")
try:
    print(float('python'))
except ValueError:
    print("ValueError cannot convert string into float in python")
else:
    print("success")
class Attributes(object):
    a=5
    print(a)
try:
    object=Attributes()
    print(object.Attributes)
except AttributeError:
    print("AttributeError occur")
    
