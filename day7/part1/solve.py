# Advent of Code | Day 7

import re
import copy

INPUT_FILENAME = "input.example.txt"

def get_inputs():
  out = []
  with open(INPUT_FILENAME, "r") as f:
    out = f.read()
    f.close()
  return out

def preprocess(inputs):
    blocksOfCommands = inputs.split("\n$ ")
    out = []
    for block in blocksOfCommands:
        out.append(block.split("\n"))
    return out

def find_sub_dict(dicti, path, key):
    if path[0] == key and key in dicti.keys():
        return dicti
    elif path[0] in dicti.keys():
        return find_sub_dict(dicti[path[0]]["children"], path[1:], key)

def walk_dirs(inputs):
    dirPath = []
    tree = {}
    currentTree = tree
    for cmdSet in inputs:

        if cmdSet[0] != "ls":
            cmd, directory = cmdSet[0].replace("$ ", "").split(" ")
        else:
            cmd = "ls"
            directory = ""

        if cmd == "cd":
            if directory == "..":
                print("is going back")
                dirPath = dirPath[:-1]
                directory = dirPath[-1]
                currentTree = find_sub_dict(tree, dirPath, directory)
            else:
                dirPath.append(directory)
                print("created dir", directory)
                currentTree[directory] = {
                    "size": 0,
                    "type": "dir",
                    "children": {}
                }

            currentTree = currentTree[directory]["children"]
        elif cmd == "ls":
            for elem in cmdSet[1:]: # all but first
                sizeOrType, fileName = elem.split(" ")
                
                if sizeOrType == "dir":
                    currentTree[fileName] = {
                        "size": 0,
                        "type": "dir",
                        "children": {}
                    }
                else:
                    currentTree[fileName] = {
                        "size": int(sizeOrType),
                        "type": "file",
                        "children": {}
                    }        
    return tree

def calculate_folder_size(tree):
    size = 0
    for key in tree.keys():
        element = tree[key]
        if element["type"] == "dir":
            size += calculate_folder_size(element["children"])
        else:
            size += element["size"]
    return size


def main():
  inputs = get_inputs()
  inputs = preprocess(inputs)
  inputs = walk_dirs(inputs)
  print(inputs)
  print("=====================")
  print("CALCULATION BEGINS")
  print("=====================")

  size = calculate_folder_size(inputs)
  print(size)
  print("Test if example correct", size == 48381165)

main()

