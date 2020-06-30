def isSubstring(string, potential_substring):
    return potential_substring in string


def string_rotation(s1: str, s2: str) -> bool:
    s1s1 = s1 + s1
    return isSubstring(s1s1, s2)


print(string_rotation('waterbottle', 'erbottlewat'))