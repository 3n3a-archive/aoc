# Advent of Code | Day 9

from collections import defaultdict

INPUT_FILENAME = "input.txt"
DEBUG_MODE = False

def get_inputs():
  out = []
  with open(INPUT_FILENAME, "r") as f:
    out = f.readlines()
    f.close()

  out2 = []
  for line in out:
    out2.append(
        line.replace("\n", "").split(" ")
    )
  return out2

def adjust(HEAD,TAIL):
    diff_row = (HEAD[0]-TAIL[0])
    diff_column = (HEAD[1]-TAIL[1])
    if abs(diff_row)<=1 and abs(diff_column)<=1:
        # ok
        pass
    elif abs(diff_row)>=2 and abs(diff_column)>=2:
        #2       2       2 
        # 1   ->  1   ->  .   -> 2
        #  H       .H      1H     1H
        TAIL = (HEAD[0]-1 if TAIL[0]<HEAD[0] else HEAD[0]+1, HEAD[1]-1 if TAIL[1]<HEAD[1] else HEAD[1]+1)
    elif abs(diff_row)>=2:
        # T     T       .
        #  H ->  .H  ->  TH
        TAIL = (HEAD[0]-1 if TAIL[0]<HEAD[0] else HEAD[0]+1, HEAD[1])
    elif abs(diff_column)>=2:
        TAIL = (HEAD[0], HEAD[1]-1 if TAIL[1]<HEAD[1] else HEAD[1]+1)
    return TAIL

def execute_instructions(inputs):
    HEAD = (0,0)
    TAIL = [(0,0) for _ in range(9)]
    ROW_DIFF_MAP = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
    COLUMN_DIFF_MAP = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
    P2 = set([TAIL[8]])
    for instruction in inputs:
        direction,amount = instruction
        amount = int(amount)
        for _ in range(amount):
            HEAD = (HEAD[0] + ROW_DIFF_MAP[direction], HEAD[1]+COLUMN_DIFF_MAP[direction])
            TAIL[0] = adjust(HEAD, TAIL[0])
            for i in range(1, 9):
                TAIL[i] = adjust(TAIL[i-1], TAIL[i])
            P2.add(TAIL[8])

def main():
    inputs = get_inputs()
    result = execute_instructions(inputs)
    print(len(result))
    print(len(result) == 2478)

main()

