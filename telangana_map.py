# telangana_map.py

districts = ['A', 'B', 'C', 'D', 'E']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

colors = ['Red', 'Green', 'Blue']

def is_valid(district, color, assignment):
    for neighbor in neighbors[district]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    for d in districts:
        if d not in assignment:
            for color in colors:
                if is_valid(d, color, assignment):
                    assignment[d] = color
                    result = backtrack(assignment)
                    if result:
                        return result
                    del assignment[d]
            return None

solution = backtrack({})
print("Telangana Map Coloring:")
print(solution)
