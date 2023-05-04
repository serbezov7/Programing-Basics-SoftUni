def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    left = word[index]
    right = word[- index - 1]

    if left != right:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
