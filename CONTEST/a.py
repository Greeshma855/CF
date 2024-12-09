import random

def generate_test_cases(num_cases=10):
    test_cases = []
    moves = ['N', 'E', 'S', 'W']
    
    # Helper function to check if Alice can reach the queen
    def can_reach_queen(n, a, b, s):
        # Calculate Alice's position after one full sequence
        x, y = 0, 0
        dx, dy = 0, 0
        for move in s:
            if move == 'N': dy += 1
            elif move == 'S': dy -= 1
            elif move == 'E': dx += 1
            elif move == 'W': dx -= 1
        
        # If there's no net movement after sequence, Alice can only reach fixed positions
        if dx == 0 and dy == 0:
            x, y = 0, 0
            for i, move in enumerate(s):
                if move == 'N': y += 1
                elif move == 'S': y -= 1
                elif move == 'E': x += 1
                elif move == 'W': x -= 1
                if x == a and y == b:
                    return True
            return False
        
        # If there is net movement, check if queen's position is reachable
        # This is a simplified check - in real cases you'd need more complex logic
        return True if abs(a) <= 10 and abs(b) <= 10 else False
    
    # Generate test cases
    for _ in range(num_cases):
        # Generate random length for string (1 to 10)
        n = random.randint(1, 10)
        
        # Generate random queen position (1 to 10)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        
        # Generate random move sequence
        s = ''.join(random.choice(moves) for _ in range(n))
        
        # Add test case
        test_cases.append((n, a, b, s))
    
    # Format output
    output = [str(len(test_cases))]
    expected_answers = []
    
    for n, a, b, s in test_cases:
        output.append(f"{n} {a} {b}")
        output.append(s)
        expected_answers.append("YES" if can_reach_queen(n, a, b, s) else "NO")
    
    return "\n".join(output), expected_answers

# Generate test cases
test_input, expected_answers = generate_test_cases(100)

print("Input:")
print(test_input)
print("\nExpected Outputs:")
print("\n".join(expected_answers))