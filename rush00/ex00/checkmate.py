def checkmate(board):
    #เช็คว่าตารางถูกต้อง ไม่มีการพิมพ์บรรทัดว่าง
    rows = board.split('\n')
    if rows and rows[-1] == '':
        rows.pop()
    #เช็คว่ากระดานว่างไหม
    n = len(rows)
    if n == 0:
        print("Error")
        return
    #เช็คว่าเป็นจัตุรัสไหม
    for row in rows:
        if len(row) != n:
            print("Error")
            return
    #วนหาking
    k_row, k_col = -1, -1
    k_count = 0
    for r in range(n):
        for c in range(n):
            if rows[r][c] == 'K':
                k_row, k_col = r, c
                k_count += 1
    #ถ้ามากกว่า1หรือไม่มีให้error
    if k_count != 1:
        print("Error")
        return
    #กำหนดชื่อตัวหมาก
    pieces = ['P', 'B', 'R', 'Q', 'K']
    #ดู4ทิศทาง(ซ้าย,ขวา,หน้า,หลัง)เพราะเรือกับควีนกินได้
    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_dirs:
        r, c = k_row + dr, k_col + dc
        while 0 <= r < n and 0 <= c < n: #เช็คตำแหน่งใน4ทิศทางจนกว่าจะถึงขอบกระดาน
            char = rows[r][c] 
            if char in pieces:
                if char in ['R', 'Q']: #เจอเรือหรือควีน
                    print("Success")
                    return
                else: #ตัวอื่นกินคิงไม่ได้
                    break
            r += dr
            c += dc
    #ดูแนวทแยง4มุม
    diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_dirs:
        r, c = k_row + dr, k_col + dc
        distance = 1 
        while 0 <= r < n and 0 <= c < n: #เช็คตำแหน่งในทิศทางทั้ง4มุมจนกว่าจะถึงขอบกระดาน
            char = rows[r][c]
            if char in pieces:
                if char in ['B', 'Q']: #เจอบิชอปหรือควีน
                    print("Success")
                    return
                elif char == 'P' and distance == 1 and dr == 1: #เบี้ยโจมตีได้แค่1ช่อง และต้องมาจากด้านล่าง(dr = 1)ของคิงเท่านั้น
                    print("Success")
                    return
                else:
                    break
            r += dr
            c += dc
            distance += 1
            
    print("Fail")