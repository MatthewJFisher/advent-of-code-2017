test = False

startA = 289
startB = 629

if test:
    startA = 65
    startB = 8921

factorA = 16807
factorB = 48271
n = 40000000

def gen(n, startA, factorA, startB, factorB):

    num = 0
    divisor = 2147483647
    outA = startA * factorA % divisor
    outB = startB * factorB % divisor
    while num < n:
        yield outA,outB
        outA = outA * factorA % divisor
        outB = outB * factorB % divisor
        num += 1

total = 0
num = 0
for a,b in gen(n, startA, factorA, startB, factorB):
    num += 1
    if num%1000000==0:
        print('cycle ' + str(num))
    # print(a)
    # print(b)
    # print('\n')
    bin_a = "{0:032b}".format(a)
    bin_b = "{0:032b}".format(b)
    # print(bin_a)
    # print(bin_b)
    # print('\n')
    if bin_a[-16:] == bin_b[-16:]:
        total+=1
print(total)
