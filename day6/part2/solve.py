# Advent of Code | Day 6

import re
import copy

INPUT_FILENAME = "input.txt"

def get_inputs():
  out = []
  with open(INPUT_FILENAME, "r") as f:
    out = f.read()
    f.close()
  return out.replace("\n", "")

def fourteen_unique_letters(inputs):
  processed_letters = []
  for index, letter in enumerate(list(inputs)):
    processed_letters.append(letter)
    if index >= 14:
      last_four_letters = processed_letters[-14:] # slices 4 letters off the end
      print(last_four_letters)
      if is_unique_combo(last_four_letters):
        return ("".join(last_four_letters), index + 1)
  return ""

def is_unique_combo(string):
  char_array = list(string)
  for index, letter in enumerate(char_array):
    temp_char_array = copy.copy(char_array)
    temp_char_array.pop(index)
    print(letter, index, temp_char_array)
    if letter in temp_char_array:
      return False
  return True

def main():
  inputs = get_inputs()
  found_letters = fourteen_unique_letters(inputs)
  print(found_letters)

main()

