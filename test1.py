
class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self):
        print(f"{self.name}的分数是：{self.score}分")


b = Student("涛GG", 66)
b.say_score()
