import itertools
rows = 3
columns = 3
start = (2,2)
commands = { 'U': (-1, 0), 'D': (1, 0),'L': (0, -1),'R': (0, 1) }

#keypad = { coordinates:i+1 for i, coordinates in enumerate(sorted(list(set(itertools.permutations(range(rows) + range(columns), 2)))))}
keypad = {(0,2): 1, (1,1): 2,  (1,2): 3, (1,3): 4, (2,0): 5, (2,1): 6,(2,2): 7,(2,3): 8,(2,4): 9,(3,1): 'A', (3,2): 'B',(3,3): 'C', (4,2): 'D'}

input = []
current_input = list(raw_input("Enter Code:"))
while(current_input != ''):
    input.append(list(current_input))
    current_input = raw_input("Enter Code:")


code = []
current_position = start

for line in input:
    for character in line:
        next_position = tuple(map(sum, zip(current_position , commands[character])))
        if next_position in keypad.keys():
            current_position = next_position

    code.append(keypad[current_position])

print(code)
