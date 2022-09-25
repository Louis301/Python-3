
def solve(s):
    spaces_id = [0]
    words = []
    s_2 = ""

    for i in range(len(s)):
        if s[i] == " ":
            spaces_id.append(i)
    spaces_id.append(len(s))

    for i in range(len(spaces_id) - 1):
        words.append(s[spaces_id[i]:spaces_id[i + 1]])
    
    for i in range(len(words)):
        if i == 0:
            s_2 += words[i].capitalize()
        else:
            s_2 = s_2 + " " + words[i][1:].capitalize()

    return s_2


string = solve("hello world")
print(string)
