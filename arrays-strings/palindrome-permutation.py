from collections import Counter

def palindrome_permutation(phrase):
	phrase = phrase.lower().replace(' ', '')
	counter = Counter(phrase)
	one_count = 0

	print(counter)

	for char in phrase:
		if counter[char] % 2 == 0:
			continue
		elif counter[char] == 1:
			one_count += 1 
		else:
			return False
	
	if one_count > 1:
		return False

	return True


print(palindrome_permutation('Tact Coa'));