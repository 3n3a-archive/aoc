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

def get_top_three(list_of_calories):
  ascending_list = sorted(list_of_calories, reverse=True)
  return ascending_list[0:3]

def main():
  inputs = read_inputs()
  parsed = parse_inputs(inputs)
  top3_elves = get_top_three(parsed)
  total3 = sum(top3_elves)
  print(top3_elves)
  print(total3)

main()
