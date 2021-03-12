class Hero:
    def __init__(self, name, atk, deff, hp, power ):
        self.heroName = name
        self.heroAtk = atk
        self.heroDef = deff
        self.heroHp = hp
        self.heroPower = power
    def showinfo(x):
        print(x.heroName, x.heroAtk, x.heroDef , x.heroHp, x.heroPower)
 
x1 = Hero("武藏", 3000, 2500, 3000, 8)
x2 = Hero("黑教徒", 1000, 1300, 500, 4)
x3 = Hero("盾兵", 1200, 2200, 2000, 6)

x1.showinfo()
x2.showinfo()
x3.showinfo()


class Chess:
    def __init__(self, name, color, level, step, cost):
        self.chessName = name
        self.chessColor = color
        self.chessLevel = level
        self.chessStep = step
        self.chessCost = cost
    def showinfo(y):
        print(y.chessName,"\t", y.chessColor,"\t", y.chessLevel, "\t", y.chessStep, "\t", y.chessCost)

y1 = Hero("將", "Black", 100, 1, 10)
y2 = Hero("帥", "Red", 100, 1, 10)
y3 = Hero("車", "Black", 80, 10, 7)


y1.showinfo()
y2.showinfo()
y3.showinfo()