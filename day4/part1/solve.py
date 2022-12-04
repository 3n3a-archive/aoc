# Advent of Code | Day 4

INPUT_FILENAME = "input.txt"

def get_inputs():
  out = []
  with open(INPUT_FILENAME, "r") as f:
    out = f.readlines()
    f.close()
  return out

def parse_inputs(inputs):
  out = []
  for line in inputs:
    clean_line = line.replace("\n", "")
    elf_pair = clean_line.split(",")

    elf_one = list(map(int, elf_pair[0].split("-")))
    elf_two = list(map(int, elf_pair[1].split("-")))

    elf_one_range = range(elf_one[0], elf_one[1] + 1)
    elf_two_range = range(elf_two[0], elf_two[1] + 1)

    out.append(
      [
        set(list(elf_one_range)),
        set(list(elf_two_range))
      ]
    )
  return out

def compare_arrays(inputs):
  out = 0
  for (elf_one, elf_two) in inputs:
    if elf_one.issubset(elf_two) or elf_two.issubset(elf_one):
      out += 1

  return out

def main():
  input_lines = get_inputs()
  inputs = parse_inputs(input_lines)
  sum = compare_arrays(inputs)
  print(sum)

main()

