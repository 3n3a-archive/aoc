# Advent of Code | Day 11

import re
import math

INPUT_FILENAME = "input.txt"

DEBUG_MODE = False

DIVIDE_BY = True

monkey_regex = regex = r"Monkey.(.*):\n.*Starting.items:.(.*)\n.*Operation:.new.=.(.*)\n.*Test:.divisible.by.(.*)\n.*If.true:.throw.to.monkey.(.*)\n.*If.false:.throw.to.monkey.(.*)"


def get_inputs():
  text = ""
  with open(INPUT_FILENAME, "r") as f:
    text = f.read()
    f.close()

  out = []
  matches = re.finditer(regex, text, re.MULTILINE)
  for match in matches:
    out.append(
        {
            "start_items": list(map(int, match.group(2).split(", "))),
            "operation": match.group(3),
            "test": int(match.group(4)),
            "test_true": int(match.group(5)),
            "test_false": int(match.group(6)),
            "inspected_items_count": 0,
        }
    )
  return out

def print_monkeys(monkeys):
    for index, monkey in enumerate(monkeys):
        count = monkey['inspected_items_count']
        print(f"Monkey {index} inspected items {count} times.")

        # items = monkey["start_items"]
        # print(f"Monkey {index}: {items}")
    print()

def do_rounds(monkeys, times):
    print(monkeys)
    print()
    for round_time in range(1, times + 1):
        for monkey_index, monkey in enumerate(monkeys, 0):
            # print(f"## Monkey {monkey_index} ##")
            items = monkey["start_items"]

            while len(items) != 0:
                item = items[0]
                operation = monkey["operation"].replace("old", str(item))
                old = item
                monkey["start_items"].pop(0)

                result = eval(operation)
                if DIVIDE_BY == True:
                    result = math.floor(result / 3)
                # print(f"operation: {operation} = {result}")

                move_to_monkey = 0
                test_number = monkey["test"]
                if (result % test_number) == 0: # is divisible
                    move_to_monkey = monkey["test_true"]
                    # print(f"is divisible by {test_number} -> {move_to_monkey}")
                else:
                    move_to_monkey = monkey["test_false"]
                    # print(f"NOT divisible by {test_number} -> {move_to_monkey}")

                # move to new monkey
                monkeys[move_to_monkey]["start_items"].append(result)

                monkeys[monkey_index]["inspected_items_count"] += 1

                # print(monkeys[monkey_index]["start_items"])
            print()

        print(f"== After round {round_time} ==")
        print_monkeys(monkeys)

def extract_inspected_counts(monkeys):
    counts = []
    for monkey in monkeys:
        counts.append(monkey["inspected_items_count"])

    return sorted(counts, reverse=True)[:2]

def main():
  monkeys = get_inputs()
  do_rounds(monkeys, 20)
  first, second = extract_inspected_counts(monkeys)
  print(first * second)

main()
