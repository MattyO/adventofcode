input = []
with open('day3.input', 'r') as f:
    input = f.readlines()

not_triangles = 0
for line in input:
    #legs = sorted(map(lambda x: int(x), line.split()))
    legs = sorted(map(lambda x: int(x), line.split()))
    print(str(legs) + str(legs[-1] > sum(legs[:-1])))
    if sum(legs[:-1]) > legs[-1]:
        not_triangles += 1
print(not_triangles)


