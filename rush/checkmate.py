def checkmate(board):
    if not board:
        return

    rows = board.splitlines()
    n = len(rows)

    if any(len(row) != n for row in rows):
        print("ตารางไม่เป็นสี่เหลี่ยมจตุรัส")
        return
    valid_pieces_name = {"K", "Q", "R", "P", "B", "."}

    for row in rows:
        for ch in row:
            if ch not in valid_pieces_name:
                print("ตัวอักษรไม่ถูกต้อง")
                return

    king_positions = []

    for row in range(n):
        for col in range(n):
            if rows[row][col] == "K":
                king_positions.append((row, col))

    if len(king_positions) == 0:
        print("ไม่มี King ในตาราง")
        return

    if len(king_positions) > 1:
        print("จำนวน King มากกว่า 1")
        return
    Kingrow, Kingcol = king_positions[0]
    
    p_count = 0
    for row in rows:
        for ch in row:
            if ch == "P":
                p_count += 1
    if p_count > 8:
        print("จำนวน Pawn มากกว่า 8")
        return
    b_count = 0
    for row in rows:
        for ch in row:
            if ch == "B":
                b_count += 1
    if b_count > 2:
        print("จำนวน Bishop มากกว่า 2")
        return
    r_count = 0
    for row in rows:
        for ch in row:
            if ch == "R":
                r_count += 1
    if r_count > 2:
        print("จำนวน Rook มากกว่า 2")
        return 
    q_count = 0
    for row in rows:
        for ch in row:
            if ch == "Q":
                q_count += 1
    if q_count > 1:
        print("จำนวน Queen มากกว่า 1")
        return

    def scan_direction(row, col, Moverow, Movecol):
        row += Moverow
        col += Movecol
        while 0 <= row < n and 0 <= col < n:
            piece = rows[row][col]
            if piece != ".":
                return (row, col, piece)
            row += Moverow
            col += Movecol
        return None
    
    pawn_attacks = [(1, -1), (1, 1)]
    for Moverow, Movecol in pawn_attacks:
        row = Kingrow + Moverow
        col = Kingcol + Movecol
        if 0 <= row < n and 0 <= col < n:
            if rows[row][col] == "P":
                print("Success")
                return

    straight_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for Moverow, Movecol in straight_dirs:
        hit = scan_direction(Kingrow, Kingcol, Moverow, Movecol)
        if hit and hit[2] in ("R", "Q"):
            print("Success")
            return

    diagonal_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for Moverow, Movecol in diagonal_dirs:
        hit = scan_direction(Kingrow, Kingcol, Moverow, Movecol)
        if hit and hit[2] in ("B", "Q"):
            print("Success")
            return

    print("Fail")
