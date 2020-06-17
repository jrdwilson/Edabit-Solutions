def longest_zero(s):
    return max(s.split('1'), key=len)

print(longest_zero("01100001011000"))
print(longest_zero("100100100"))
print(longest_zero("11111"))
