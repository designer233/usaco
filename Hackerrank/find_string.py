def count_substring(string, sub):
    count = 0
    string_len = len(string)

    for x in range(string_len):
        for y in range(len(sub)):
            if ((x+y) >= string_len or string[x+y] != sub[y]):
                break
        else: count += 1

    return count
