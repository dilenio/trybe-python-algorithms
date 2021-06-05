def is_palindrome_recursive(word, low, high):
    if not word:
        return False

    if len(word) == 1:
        return True

    if word[low] == word[high]:
        substr = word[1:len(word) - 1]
        return is_palindrome_recursive(substr, 0, len(substr) - 1)

    return False
