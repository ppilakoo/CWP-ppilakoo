def checkmate(board):
    rows = board.split('\n')
    if rows and rows[-1] == '':
        rows.pop()
    
    n = len(rows)
    if n == 0:
        print("Error")
        return
        
    for row in rows:
        if len(row) != n:
            print("Error")
            return

    k_row, k_col = -1, -1
    k_count = 0
    for r in range(n):
        for c in range(n):
            if rows[r][c] == 'K':
                k_row, k_col = r, c
                k_count += 1
    
    if k_count != 1:
        print("Error")
        return

    pieces = ['P', 'B', 'R', 'Q', 'K']

    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_dirs:
        r, c = k_row + dr, k_col + dc
        while 0 <= r < n and 0 <= c < n:
            char = rows[r][c]
            if char in pieces:
                if char in ['R', 'Q']:
                    print("Success")
                    return
                else:
                    break
            r += dr
            c += dc

    diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_dirs:
        r, c = k_row + dr, k_col + dc
        distance = 1 
        while 0 <= r < n and 0 <= c < n:
            char = rows[r][c]
            if char in pieces:
                if char in ['B', 'Q']:
                    print("Success")
                    return
                elif char == 'P' and distance == 1 and dr == 1:
                    print("Success")
                    return
                else:
                    break
            r += dr
            c += dc
            distance += 1
            
    print("Fail")