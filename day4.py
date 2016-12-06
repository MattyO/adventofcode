import re
import collections
import itertools
import functools

#361012
input = []
with open('day4.input', 'r') as f:
    input = f.readlines()

#for line in input:
#input = ['aaaa-bbb-z-y-x-123[abxyz]',
#'a-b-c-d-e-f-g-h-987[abcde]',
#'not-a-real-room-404[oarel]',
#'totally-real-room-200[decoy]',]

Letter = collections.namedtuple("Letter", ["letter", "count"])

sum =0
for line in input:
    result = re.search("^([a-z\-]*)([0-9]*)\[(.*)\]$", line)
    name = result.group(1)
    sector_id = result.group(2)
    checksum   = result.group(3)

    c = collections.Counter(name.replace('-', ''))
    counts = [Letter(l,c) for l,c in c.most_common()]
    groups = {k: sorted(g, key=lambda x: x.letter) for k, g in itertools.groupby(counts, lambda c: c.count)}
    temp_group = reversed([(i, j) for i, j in groups.items()])
    #print(list(temp_group))

    ranked_letter = functools.reduce(lambda sum, x: sum + x, map(lambda lst: functools.reduce(lambda sum, l: sum + l.letter, lst, ""), [letters for count, letters in list(temp_group)]), "")

    if(ranked_letter[:5] == checksum):
        sum += int(sector_id)
    else:
        print('********')
        print(ranked_letter[:5])
        print(checksum)
        print('********')

print(sum)
