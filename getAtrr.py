"""
不打开注释的情况下，输出结果：
name: mingming
number: {'class': 'two', 'number': '002'}
打开全部注释的输出结果：
name: only entrance
number: only entrance
dormitory: only entrance
"""

class Student:
    def __init__(self, name, grade, info):
        self.name = name
        self.grade = grade
        self.number = info

    def __getattr__(self, item):
        return self.info[item]

    # def __getattribute__(self, item):
    #     return 'only entrance'

if __name__ == '__main__':
    mingming = Student('mingming', 'two', {'class': 'two', 'number': '002'})
    print("name:", mingming.name)
    print("number:", mingming.number)
    # print("dormitory:", mingming.dormitory)
