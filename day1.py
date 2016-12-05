import collections

possible_directions = ['N', 'E', 'S', 'W']
current_direction=0
northing = 0
easting = 0
positions = []

components = raw_input("Enter directions:").replace(" ", "")
seperated_components = components.split(',')

for individual_component in seperated_components:
    old_northing = northing
    old_easting = easting
    #print(old_northing)
    #print(old_easting)

    if individual_component[0] == "R":
        current_direction = (current_direction + 1) % len(possible_directions)
    else:
        current_direction = (current_direction - 1) % len(possible_directions)

    if possible_directions[current_direction] == 'N':
        northing += int(individual_component[1:])
    elif possible_directions[current_direction] == 'E':
        easting += int(individual_component[1:])
    elif possible_directions[current_direction] == 'S':
        northing -= int(individual_component[1:])
    elif possible_directions[current_direction] == 'W':
        easting -= int(individual_component[1:])

    #print(northing)
    #print(easting)
    #print range(old_northing, northing, -1 if northing  < old_northing else 1)[1:]
    #print range(old_easting, easting, -1 if easting < old_easting  else 1)[1:]

    for a_northing in range(old_northing, northing, -1 if northing  < old_northing else 1)[1:]:
        positions.append((a_northing, easting))

    for a_easting in range(old_easting, easting, -1 if easting < old_easting  else 1)[1:]:
        positions.append((northing, a_easting))

    positions.append((northing, easting))

c = collections.Counter(positions)

been_there_before = [p for p in positions if c[p] > 1]
print(str(been_there_before))

print("Northing: " + str(northing))
print("Easting: " + str(easting))
print("Total: " + str(abs(northing) + abs(easting)) )

print("New have be there before end")
northing, easting = been_there_before[0]
print("Northing: " + str(northing))
print("Easting: " + str(easting))
print("Total: " + str(abs(northing) + abs(easting)) )

