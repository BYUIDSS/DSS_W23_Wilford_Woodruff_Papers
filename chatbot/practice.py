x = None
placeholder = None
for i in data:
    if i == "|":
        x = i
        while x != "]":
            placeholder = placeholder.add(x)