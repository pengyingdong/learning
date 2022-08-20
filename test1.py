
class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self):
        print(f"{self.name}的分数是：{self.score}分")


a = Student("东G", 66)
a.say_score()
