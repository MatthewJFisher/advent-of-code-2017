test = False

startA = 289
startB = 629

if test:
    startA = 65
    startB = 8921

factorA = 16807
factorB = 48271
multA = 4
multB = 8
n = 5000000

def gen(n, startA, factorA, multA):

    num = 0
    divisor = 2147483647
    outA = startA * factorA % divisor
    while num < n:
        if outA%multA == 0:
            yield outA
            num += 1
        outA = outA * factorA % divisor


total = 0
num = 0
for a,b in zip(gen(n, startA, factorA, multA),gen(n, startB, factorB, multB)):
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
