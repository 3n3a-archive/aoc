# Advent of Code | Day 5

import re

INPUT_FILENAME = "input.example.txt"

def get_inputs():
  out = []
  with open(INPUT_FILENAME, "r") as f:
    out = f.read()
    f.close()
  return out

def parse_inputs(inputs):
  parsed_instructions = []

  parts = inputs.split("\n\n")
  containers = parts[0]
  # todo

  instructions = parts[1]
  for instruction in instructions:
    cleaned = instruction.replace("\n", "")
    regex = r"move.(.*).from.(.*).to.(.*)"
    matches = re.search(regex, cleaned, re.MULTILINE)
    g = list(matches.groups())
    parsed_instructions.append({
      "amount": g[0],
      "from": g[1],
      "to": g[2]
    })
  return (, parsed_instructions)

def compare_arrays(inputs):
  out = 0
  for (elf_one, elf_two) in inputs:
    if elf_one.issubset(elf_two) or elf_two.issubset(elf_one):
      out += 1

  return out

def main():
  input_lines = get_inputs()
  inputs = parse_inputs(input_lines)
  #sum = compare_arrays(inputs)
  print(inputs)

main()

