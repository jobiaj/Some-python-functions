import re
def collpase(string1):
  return ''.join(string1.split())
print collpase("stuff   .  // : /// more-stuff .. .. ...$%$% stuff -> DD")