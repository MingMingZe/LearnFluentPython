import collections

stu_table = collections.namedtuple('stu_table', 'group number'.split())


class Students:
    number = [str(x) for x in range(10)]
    group = 'group1 group2 group3'.split()

    def __init__(self):
        self._student = [stu_table(grp, num) for grp in self.group for num in self.number]

    def __len__(self):
        return len(self._student)

    def __getitem__(self, item):
        return self._student[item]

    def __setitem__(self, key, value):
        self._student[key] = value

    def __delitem__(self, key):
        del self._student[key]

    def insert(self, index, value):
        self._student.insert(index, value)


if __name__ == '__main__':
    from random import shuffle
    students = Students()
    # shuffle(students)
    # TypeError: 'Students' objectdoesnot support item assignment

    # 🐒猴子补丁
    def set_student(std, num, item):
        std._student[num] = item

    Students.__setitem__ = set_student
    shuffle(students)
    # 检查insert
    # students.insert(0, "hhhhhhhhhhhhh")
    # print(students[1])
    for stu in students:
        print(stu)
