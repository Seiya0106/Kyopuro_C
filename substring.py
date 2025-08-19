def get_all_substrings(string):
    substrings = []
    for start in range(len(string)):
        for end in range(start + 1, len(string) + 1):
            substrings.append(string[start:end])
    return substrings

# 使用例
text = "abc"
result = get_all_substrings(text)
print(result)  # ['a', 'ab', 'abc', 'b', 'bc', 'c']

def get_unique_substrings(string):
    substrings = set()
    for start in range(len(string)):
        for end in range(start + 1, len(string) + 1):
            substrings.add(string[start:end])
    return list(substrings)

text = "abca"
result = get_unique_substrings(text)
print(result)  # ['a', 'ab', 'abc', 'b', 'bc', 'c', 'ca']
