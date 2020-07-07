from gameboard import GameBoard

def solve(b, fr=0, to=2, ot=1, depth=1):
    if b.height == depth: #Base case
        b.movepiece(fr,to)

    else:
        solve(b, fr, ot, to, depth+1)
        b.movepiece(fr,to)
        solve(b, ot, to, fr, depth+1)


b = GameBoard(7)
solve(b)
print(b.isComplete())
print(b.height, b.movesMade)
