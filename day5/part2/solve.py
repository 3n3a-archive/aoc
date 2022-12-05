# Advent of Code | Day 5

import re

INPUT_FILENAME = "input.txt"

def get_inputs():
  out = []
  with open(INPUT_FILENAME, "r") as f:
    out = f.read()
    f.close()
  return out

def parse_inputs(inputs):
  parts = inputs.split("\n\n")

  # parse containers into temp object
  parsed_containers_tmp = {}
  containers = parts[0].split("\n")
  for line in containers:
    cleaned = line.replace("\n", "")
    regex = r"\[(.)\]"
    matches = list(re.finditer(regex, cleaned, re.MULTILINE))
    for match in matches:
      pos = match.end() - 2
      name = match.group(0).replace("[", "").replace("]", "")

      if pos in parsed_containers_tmp.keys():
        parsed_containers_tmp[pos].append(name)
      else:
        parsed_containers_tmp[pos] = [name]

  # move temp containers into object with correct keys
  parsed_containers = {}
  for i, current_key in enumerate(sorted(parsed_containers_tmp.keys()), start=1):
    parsed_containers[i] = list(reversed(parsed_containers_tmp[current_key]))

  # parse instructions into list
  parsed_instructions = []
  instructions = parts[1].split("\n")
  for instruction in instructions:
    cleaned = instruction.replace("\n", "")
    regex = r"move.(.*).from.(.*).to.(.*)"
    matches = re.search(regex, cleaned, re.MULTILINE)
    g = list(matches.groups())
    parsed_instructions.append({
      "amount": int(g[0]),
      "from": int(g[1]),
      "to": int(g[2])
    })
  return (parsed_containers, parsed_instructions)

def execute_instructions(containers, instructions):
  for instruction in instructions:
    amount = instruction["amount"]
    from_ = instruction["from"]
    to_ = instruction["to"]

    elements_from_len = len(containers[from_])

    # mutliple crates in same order
    move = []
    for i in range(elements_from_len, elements_from_len - amount, -1):
      move.append(containers[from_].pop(i-1))
    
    for moved in reversed(move):
      containers[to_].append(moved)

  return containers

def get_top_containers(containers):
  out = ""
  for container_key in sorted(containers.keys()):
    container = containers[container_key][-1:][0]
    out += container

  return out
      

def main():
  input_lines = get_inputs()
  containers, instructions = parse_inputs(input_lines)
  final_containers = execute_instructions(containers, instructions)
  top_containers = get_top_containers(final_containers)
  print(top_containers)

main()

