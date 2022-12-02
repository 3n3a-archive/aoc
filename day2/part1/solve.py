# Advent of Code | Day 2

# Points
# =====
# A|X|Rock => 1
# B|Y|Paper => 2
# C|Z|Scissor => 3
# Lose => 0
# Draw => 3
# Win => 6

INPUT_FILENAME = "input.txt"

inputs = []

def get_inputs():
  out = []
  with open(INPUT_FILENAME, "r") as f:
    out = f.readlines()
    f.close()
  return out

def parse_inputs(inputs):
  out = []
  for line in inputs:
     out.append(line.replace("\n", "").split(" "))
  return out

def is_draw(elf, me):
  if elf == "A" and me == "X":
    return True
  elif elf == "B" and me == "Y":
    return True
  elif elf == "C" and me == "Z":
    return True
  else:
    return False

def is_win(elf, me):
  # rock beat by paper
  if elf == "A" and me == "Y":
    return True
  # rock beats scissors
  elif elf == "A" and me == "Z":
    return False
  # paper beats rock
  elif elf == "B" and me == "X":
    return False
  # paper bneat by scissors
  elif elf == "B" and me == "Z":
    return True
  # scissors beat by rock
  elif elf == "C" and me == "X":
    return True
  # scissors beats paper
  elif elf == "C" and me == "Y":
    return False
  else:
   print(elf, me)

def rock_paper_scissors(item):
  elf = item[0]
  me = item[1]
 
  # item points
  item_point = 0
  if me == "X":
    item_point = 1
  elif me == "Y":
    item_point = 2
  elif me == "Z":
    item_point = 3

  # win, lose, draw
  if is_draw(elf, me) == True:
    return 3 + item_point
  elif is_win(elf, me) == True:
    return 6 + item_point
  else:
    return 0 + item_point

def solve_for_lines(lines):
  results_iterator = map(rock_paper_scissors, lines)
  results_tuple = tuple(results_iterator)  
  return sum(results_tuple)

def main():
  input_lines = get_inputs()
  inputs = parse_inputs(input_lines)
  results = solve_for_lines(inputs)
  print(results)

main()

