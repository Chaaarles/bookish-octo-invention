# a)


def check_equal(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

str1 = 'hei'
str2 = 'hello'
str3 = 'hello'
print(check_equal(str1, str2))
print(check_equal(str3, str2))

# b)


def reversed_word(s):
    out = ""
    for i in range(len(s)):
        out += s[-(i+1)]
    return out

string = 'star desserts'
print(reversed_word(string))

# c)


def check_palindrome(s):
    r = reversed_word(s)
    return check_equal(s, r)

str1 = 'agnes i senga'
str2 = 'hello'
print(check_palindrome(str1))
print(check_palindrome(str2))

# d)


def contains_string(s1, s2):
    if s2 in s1:
        i = len(s1.split(s2)[0])
        return i
    else:
        return -1

str1 = 'pepperkake'
str2 = 'per'
str3 = 'ola'
print(contains_string(str1, str2))
print(contains_string(str1, str3))
