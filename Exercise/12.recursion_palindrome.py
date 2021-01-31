def palindrome(word, i=0, last_i=-1):
    if len(word) // 2 == i:
        return f"{word} is a palindrome"

    if word[i] == word[last_i]:
        return palindrome(word, i + 1, last_i - 1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
