def flippingBits(n):
    # Write your code here
    bi = bin(n)[2:].rjust(32,'0')
    res = str(int('1'*32) - int(bi))
    return int(res, 2)

result = flippingBits(4)

print(str(result) + '\n')
