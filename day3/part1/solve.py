# Advent of Code | Day 3

INPUT_FILENAME = "input.txt"

def get_inputs():
  out = []
  with open(INPUT_FILENAME, "r") as f:
    out = f.readlines()
    f.close()
  return out

def get_priority(c):
  charCode = ord(c)
  if charCode in range(97, 123):
    return charCode - 96
  elif charCode in range(65, 91):
    return charCode - 38
  

def parse_inputs(inputs):
  out = []
  for line in inputs:
    clean_line = line.replace("\n", "")
    half = int(len(clean_line) / 2)
    out.append(
      [
        list(map(get_priority, list(clean_line[:half]))), 
        list(map(get_priority, list(clean_line[half:])))
      ]
    )
  return out

def compare_arrays(inputs):
  out = 0
  for array in inputs:
    out += list(set(array[0]) & set(array[1]))[0]
  return out

def main():
  input_lines = get_inputs()
  inputs = parse_inputs(input_lines)
  sum = compare_arrays(inputs)
  print(sum)

main()

