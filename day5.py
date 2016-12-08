import hashlib

input = "abbhdwsy"
#input = "abc"
code = ""

i = 0
while True:
    md5_output = hashlib.md5(input + str(i)).hexdigest()
    if md5_output.startswith("00000"):
        code += md5_output[5]
        print(i)
        if len(code) == 8:
            break;
    i +=1
print code
