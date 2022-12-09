# Advent of Code | Day 9

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

def create_field(width, height):
    out = []
    for i, hf in enumerate(range(height)):
        out.append([])
        for j, wf in enumerate(range(width)):
            out[i].append(".")
    return out

def print_field(field, head, tail):
    for i, row in enumerate(field):
        for j, column in enumerate(row):
            head_x, head_y = head
            tail_x, tail_y = tail

            if DEBUG_MODE:

                if head_x == j and head_y == i:
                    print("H", end=" ")
                elif tail_x == j and tail_y == i:
                    print("T", end=" ")
                else:
                    print(column, end=" ")

            else:
                print(column, end=" ")
        print("")

def move(direction, pointer):
    X = 0
    Y = 1
    if direction == "D":
        pointer[Y] += 1

    elif direction == "R":
        pointer[X] += 1

    elif direction == "U":
        pointer[Y] -= 1

    elif direction == "L":
        pointer[X] -= 1

def move_behind_head(head, tail, direction):
    if direction == "R":
        tail[0] = head[0] - 1
        tail[1] = head[1]
    elif direction == "U":
        tail[0] = head[0]
        tail[1] = head[1] + 1
    elif direction == "L":
        tail[0] = head[0] + 1
        tail[1] = head[1]
    elif direction == "D":
        tail[0] = head[0]
        tail[1] = tail[1] - 1

def get_distance(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail

    x_diff = abs(head_x - tail_x)
    y_diff = abs(head_y - tail_y)
    return x_diff + y_diff

def is_diagonal(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail

    x_diff = abs(head_x - tail_x)
    y_diff = abs(head_y - tail_y)
    return x_diff >= 1 and y_diff >= 1

def execute_instructions(instructions, field, head, tail):
    field[head[1]][head[0]] = "#"

    for instruction_index, instruction in enumerate(instructions):
        print(f"=== {instruction} ===")
        
        direction, amount = instruction
        amount = int(amount)

        for i in range(amount):
            move(direction, head)

            diag = is_diagonal(head, tail)

            print("diagonal", diag)

            if get_distance(head, tail) == 2 and not diag:
                move_behind_head(head, tail, direction)
            elif get_distance(head, tail) >= 3 and diag:
                move_behind_head(head, tail, direction)

            x, y = tail

            print("tail", tail)
            print("head", head)
            field[y][x] = "#"

            if DEBUG_MODE:
                print_field(field, head, tail)
            print()
        print()
    print_field(field, head, tail)

def count_visited_positions(field):
    counter = 0
    for row in field:
        for column in row:
            if column == "#":
                counter += 1
    return counter

def get_dimensions(instructions):
    left = 0
    right = 0
    up = 0
    down = 0

    for direction, amount in instructions:
        amount = int(amount)
        if direction == "U":
            up += amount
        elif direction == "D":
            down += amount
        elif direction == "R":
            right += amount
        elif direction == "L":
            left += amount

    width = left + right
    height = up + down
    return width, height

def main():
  instructions = get_inputs()
  width, height = get_dimensions(instructions)
  print(f"Dimensions w: {width} h: {height}")

  half_height = int(height/2)
  half_width = int(width/2)
  head = [half_width, half_height]
  tail = [half_width, half_height]

  field = create_field(width, height)
  execute_instructions(instructions, field, head, tail)
  count = count_visited_positions(field)
  print(f"Visited at least once: {count}")

main()

