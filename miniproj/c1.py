def check_K(board):
    position_K = []
    for r in range(len(board)):
        for c in range(len(r)):
            if board[r][c] == "K":
                position_K.append((r,c))
                
    if len(position_K) == 0:
        print("Error,No king found")
        return
            
    if len(position_K) != 1:
        print("Error,There is more than one king.")
        return 
    
    kx,ky = position_K

    def check_direction(dx,dy,enemy):
        x,y = kx + dx,ky + dy
        while 0 <= x < r and 0 <= y < c:
            point = board[x][y]
            if point != ".":
                if point in enemy:
                    return True
                else:
                    return False
            x += dx
            y += dy
        return False
    
    straight = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx , dy in straight:
        if check_direction(dx,dy,["R","Q"]):
            print("Succes")
            return
    
    diagonals = [(-1,-1),(-1,1),(1,-1),(1,1)]
    for dx , dy in diagonals:
        if check_direction(dx,dy,["B","Q"]):
            print("Success")
            return
        
    pawn = [(-1,1),(-1,1)]
    for dx , dy in pawn:
        sx,sy = kx + dx , ky + dy
        if 0 <= sx < r and 0 <= sy < c:
            if board[sx][sy] == "P":
                print("Success")
                return
            
    print("Fail")

    
              
        
         



    

    
    
    
   

