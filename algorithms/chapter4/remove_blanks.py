# Create a function that given a string, returns all of that strings contents but without blanks. If given the string " Pl ayTha tF u nkyM usi c"   return "PlayThatFunkyMusic" .

def remove_blanks(string):
  result = ""
  for char in string:
    if char != " " and char != "\n" and char != "\t":
      result += char
  return result

print remove_blanks("   Pl ayTha \ntF u \tnkyM usi \nc")