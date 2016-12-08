import hashlib

input = "abbhdwsy"
#input = "abc"
code = [ None for i in range(8)]

numbers = [ str(i) for i in  range(10)]
i = 0
while True:
    md5_output = hashlib.md5(input + str(i)).hexdigest()
    if md5_output.startswith("00000") and md5_output[5] in numbers and int(md5_output[5]) < 8 and code[int(md5_output[5])] is None :
        code[int(md5_output[5])] = md5_output[6]
        print(i)
        if None not in code:
            break;
    i +=1
print code
