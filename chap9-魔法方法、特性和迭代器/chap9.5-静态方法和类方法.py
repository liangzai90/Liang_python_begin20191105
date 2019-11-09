__metaclass__ = type

print("-------静态方法和类方法---------")
class MyClass:

    def smeth():
        print("This is a static method.")
    smeth = staticmethod(smeth)

    def cmeth(cls):
        print("This is class method of', cls")
    cmeth = classmethod(cmeth)

MyClass.smeth()  # This is a static method.
MyClass.cmeth()  # This is class method of', cls


class MyClassB:
    @staticmethod
    def smeth():
        print("this is a static method.BBB")
    @classmethod
    def cmeth(cls):
        print("This is a class method of', cls .BBB")

MyClassB.smeth()  # this is a static method.BBB
MyClassB.cmeth()  # This is a class method of', cls .BBB

