from collections import Counter


def one_away(str1, str2):

    def find_shorter(str1, str2):
        if len(str1) < len(str2):
            return (str1, str2)
        else:
            return (str2, str1)

    sl = find_shorter(str1, str2)
    shorter = sl[0]
    longer = sl[1]
    count = 0

    if (abs(len(str1) - len(str2))) > 1:
        return False

    counter_s = Counter(shorter)
    counter_l = Counter(longer)

    for char in shorter:
        if char in counter_s and char in counter_l:
            count += 1
            counter_s[char] -= 1
            counter_l[char] -= 1

    if count < len(longer) - 1 or count > len(longer) + 1:
        return False

    return True


print(one_away('pale', 'ple'))
print(one_away('pale', 'bale'))
print(one_away('pal', 'plaa'))
print(one_away('pales', 'pale'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bake'))
