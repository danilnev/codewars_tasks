def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if abs(ord(chars[i]) - ord(chars[i + 1])) != 1:
            return chr(ord(chars[i]) + 1)
