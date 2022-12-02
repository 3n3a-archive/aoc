INPUT_FILENAME = "input.txt"

def read_inputs():
  out = []
  with open(INPUT_FILENAME, "r") as f:
    out = f.read()
    f.close()
  return out

def parse_inputs(inputs):
  out = []
  each_elf = inputs.split("\n\n")
  for elf in each_elf:
    if elf != '':
      split_elf = elf.split("\n")
      inner_out = 0
      for calory in split_elf:
        if calory != "":
          calories = int(calory)
          inner_out += calories
      out.append(inner_out)
  return out

def get_biggest(list_of_calories):
  biggest = max(list_of_calories)
  return (biggest, list_of_calories.index(biggest) + 1)

def main():
  inputs = read_inputs()
  parsed = parse_inputs(inputs)
  elf_most_calories = get_biggest(parsed)
  print(elf_most_calories)

main()
