def is_prime(num):
    val = True
    for x in range(2, int(num**(0.5))+1):
        if num % x == 0:
            val = False
            break
    return val

b = 106500
c = 123500
h = 0

while b <= c:
    if not is_prime(b):
        h += 1
    b+=17

print(h)
