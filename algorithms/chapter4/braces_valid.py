def braces_valid(string):
  opens = []
  braces_map = {
    "}": "{",
    "]": "[",
    ")": "("
  }
  for char in string:
    if char == "{" or char == "(" or char == "[":
      opens.append(char)
    elif char == "}" or char == ")" or char == "]":
      try:
        latest_open = opens.pop()
      except IndexError:
        return False

      if latest_open != braces_map[char]:
        return False
  return not opens

print braces_valid("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!") # True
print braces_valid("D(i{a}l[ t]o)n{e") # False
print braces_valid("A(1)s[O (n]0{t) 0}k") # False
print braces_valid("]]]]]]]]") # False
print braces_valid("") # True