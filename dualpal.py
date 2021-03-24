
'''
ID: smaylni1
LANG: PYTHON3
TASK: dualpal
'''

def divine(number, base):
    global num
    if (number // base == 0):
        num = str(number % base)
        return number % base
    else:
        divine(number // base, base)
        num += str(number % base)
        return number % base

def ispalindrome(num):
    if len(num) <= 1:
        return True
    else:
        return num[0] == num[-1] and ispalindrome(num[1:-1])

f = open('dualpal.in', 'r')
inp = list(map(int, f.read().split(' ')))
f.close()

f = open('dualpal.out', 'a')
r = 0

while (r < inp[0]):
    k = 0
    inp[1] += 1
    for i in range(2, 11):
        divine(inp[1], i)
        if ispalindrome(num):
            k += 1
        else:
            continue
    if (k >= 2):
        r += 1
        f.write(str(inp[1]) + '\n')

f.close()