import json
import re

with open("input.txt") as file:
    input = file.read()

print(sum(map(int, re.findall("-?[0-9]+", input))))

def hook(obj):
  if "red" in obj.values(): return {}
  else: return obj

without_red = str(json.loads(input, object_hook=hook))
print (sum(map(int, re.findall("-?[0-9]+", without_red))))
