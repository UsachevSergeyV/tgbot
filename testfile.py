l = [1,2,3,4,"ds",6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(l[10:22])

print("____________________________")

def fundam(numba):
    return numba*2,l[1:3]

ret = fundam(12345)

print(ret)
print("end")
