t = int(input())
results = []
    
for _ in range(t):
    n, target_x, target_y = map(int, input().split())
    moves = input()
        
    curr_x, curr_y = 0, 0
    positions = [(0, 0)] 
    for move in moves:
        if move == 'N': curr_y += 1
        elif move == 'S': curr_y -= 1
        elif move == 'E': curr_x += 1
        elif move == 'W': curr_x -= 1
        positions.append((curr_x, curr_y))
        

    if (target_x, target_y) in positions:
        results.append("YES")
        continue
            
        # Calculate net movement per sequence
    dx = curr_x  # Net x movement per sequence
    dy = curr_y  # Net y movement per sequence
        
        # If no net movement (cycle in place)
    if dx == 0 and dy == 0:
        results.append("NO")
        continue
            
        # At this point, Alice moves in a pattern with net displacement (dx, dy)
        # We need to check if target can be reached in future sequences
        
        # For target to be reachable:
        # 1. If moving mainly in x direction (|dx| > |dy|):
        #    - After some sequences, x should be able to reach target_x
        #    - y displacement should allow reaching target_y
        # 2. Similar for y direction
        
    can_reach = False
        
    if abs(dx) > 0 or abs(dy) > 0:
            # Check if we can reach target_x and target_y with the net movement pattern
            # We allow for up to 1000 sequences to handle various patterns
        for k in range(1000):
            base_x = dx * k
            base_y = dy * k
                
                # Check all positions in the sequence starting from this base position
            for pos_x, pos_y in positions:
                curr_pos_x = base_x + pos_x
                curr_pos_y = base_y + pos_y
                    
                if curr_pos_x == target_x and curr_pos_y == target_y:
                    can_reach = True
                    break
                
            if can_reach:
                break
                
                # Optimization: if we're moving away from target in both directions, stop
            if abs(base_x) > abs(target_x) + abs(dx) and abs(base_y) > abs(target_y) + abs(dy):
                break
        
    results.append("YES" if can_reach else "NO")
    
    # Print results
for result in results:
    print(result)
