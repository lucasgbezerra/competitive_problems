cases  = int(input())

while cases > 0:
    chessboard = []
    _ = input()
    for i in range(8):
        chessboard.append(input())
    for i in range(7):
        if chessboard[i].find("#.#") != -1 and chessboard[i+1].find(".#.") != -1:
            x = chessboard[i+1].find("#") + 1
            y = i + 2
            break
    
    print(y, x)
    cases -= 1
