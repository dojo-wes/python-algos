def parens_valid(string):
    parens_open = 0
#     print(list(string))

    for char in string:
        # print(char)
        if char is "(":
            parens_open += 1
        elif char is ")":
            parens_open -= 1
        if parens_open < 0:
            # print(parens_open)
            return False
        # print(parens_open)

    return parens_open == 0
    # if parens_open == 0:
    #     validity = True
    # else:
    #     validity = False

    # return validity

print(parens_valid("()")) # True
print(parens_valid("(")) # False
print(parens_valid("(jghjhd))(")) # False
print(parens_valid("a")) # True

# print parens_valid("(")

