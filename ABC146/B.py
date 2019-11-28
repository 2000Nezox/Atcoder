
N = int(input())

encryptionStr = input()

excludeStr = ""

result = ""

SHIFT_COUNT = N

for c in encryptionStr :

    if excludeStr.find(c) != -1 :
        result = result + c
        continue


    if ord('a') <= ord(c) <= ord('z') :
        result = result + chr(abs(((ord(c) + SHIFT_COUNT - ord('a')) % 26)) + ord('a'))
    else :
        result = result + chr(abs(((ord(c) + SHIFT_COUNT - ord('A')) % 26)) + ord('A'))

print (result)