
# 1_counting_vowels.py
#
# ssume s is a string of lower case characters.
#
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#

c = 0
for v in 'aeiou':
    c += s.count(v)
print 'Number of vowels: %(c)d' % {'c': c}
