def solve(s):
    vowels = "aeiou"def  
    consonant_substrings = []
    current_substring = 0

    for char in s:
        if char not in vowels:
            current_substring += ord(char) - ord('a') + 1
        else:
            consonant_substrings.append(current_substring)
            current_substring = 0

    consonant_substrings.append(current_substring)
    return max(consonant_substrings)        
