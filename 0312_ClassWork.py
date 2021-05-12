class Student:
    def __init__(self,name ,school,work,grade,number):
        self.studentName = name
        self.studentSchool = school
        self.studentWork = work
        self.studentGrade = grade
        self.studentNumber = number
    def showinfo(x):
        print(x.studentName,"\t",x.studentSchool,"\t",x.studentWork,"\t",x.studentGrade,"\t",x.studentNumber,"\t")

x1 = Student("張祐瑋","亞洲","資工",1,85)
x1.showinfo()


class Chess:
    def __init__(self, name, color, level, step, cost):
        self.chessName = name
        self.chessColor = color
        self.chessLevel = level
        self.chessStep = step
        self.chessCost = cost
    def showinfo(y):
        print(y.chessName,"\t", y.chessColor,"\t", y.chessLevel, "\t", y.chessStep, "\t", y.chessCost)

y1 = Chess("將", "Black", 100, 1, 10)
y2 = Chess("帥", "Red", 100, 1, 10)
y3 = Chess("車", "Black", 80, 10, 7)


y1.showinfo()
y2.showinfo()
y3.showinfo()