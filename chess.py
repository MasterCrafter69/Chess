def value(pawn, knight, bishop, rook, queen):
    score = 0
    if pawn > 0:
        c = 0
        while pawn > c:
            score += 1
            c += 1
    if knight > 0:
        c = 0
        while knight > c:
            score += 3
            c += 1
    if bishop > 0:
        c = 0
        while bishop > c:
            score += 3
            c += 1
    if rook > 0:
        c = 0
        while rook > c:
            score += 5
            c += 1
    if queen > 0:
        c = 0
        while queen > c:
            score += 9
            c += 1
    return score

def main():
    pawn = int(input("how many pawns did you capture?"))
    knight = int(input("how many knights did you capture?"))
    bishop = int(input("how many bishops did you capture?"))
    rook = int(input("how many rooks did you capture?"))
    queen = int(input("how many queens did you capture?"))
    print("your score is:", value(pawn, knight, bishop, rook, queen))

main()