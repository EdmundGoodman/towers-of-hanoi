from gameboard import GameBoard

def solve(b):
    def m1(fr, to, ot):
        b.movepiece(fr,to)

    def m2(fr, to, ot):
        m1(fr, ot, to)
        m1(fr, to, ot)
        m1(ot, to, fr)

    def m3(fr, to, ot): #0, 2, 1
        m2(fr, ot, to) #Move main pile off
        m1(fr, to, ot) #Move lowest piece
        m2(ot, to, fr) #Move main pile on

    def m4(fr, to, ot):
        m3(fr, ot, to)
        m1(fr, to, ot)
        m3(ot, to, fr)

    def m5(fr, to, ot):
        m4(fr, ot, to)
        m1(fr, to, ot)
        m4(ot, to, fr)


    if b.height == 1: #1 move
        m1(0, 2, 1)
    elif b.height == 2: #3 moves
        m2(0, 2, 1)
    elif b.height == 3: #7 moves
        m3(0, 2, 1)
    elif b.height == 4: #15 moves
        m4(0, 2, 1)
    elif b.height == 5: #31 moves
        m5(0, 2, 1)



b = GameBoard(3)
solve(b)
print(b.isComplete())
print(b.height, b.movesMade)
