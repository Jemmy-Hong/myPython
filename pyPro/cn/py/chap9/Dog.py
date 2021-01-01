class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """小狗模拟被命令式时蹲下"""
        print(self.name.title() + " is now sittint.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


myDog = Dog('willie', 6)

print("My dog's name is " + myDog.name.title() + ".")
print("My dog is " + str(myDog.age) + " years old.")

print("\n")

myDog.sit()
myDog.roll_over()
