# Each number in the sequence is the sum of the two numbers that precede it.
# So, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
a, b, i = 0, 1, 1
print(b, end=" ")
while i < 10:
    i += 1
    c = a + b # c = 0 + 1 => c = 1
    print(c, end=" ")
    a = b # a = 1
    b = c # b = 1


