# Advent of Code | Day 7

import re
import copy

INPUT_FILENAME = "input.txt"

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

def get_folder_size(tree):
    size = 0
    for key in tree.keys():
        element = tree[key]
        if element["type"] == "file":
            size += element["size"]
        else:
            size += get_folder_size(element["children"])
    return size

def calculate_folder_size(tree):
    for key in tree.keys():
        element = tree[key]
        if element["type"] == "dir":
            element["size"] += get_folder_size(element["children"])
            element["children"] = calculate_folder_size(element["children"])
    return tree

def get_dirs_with_size(tree, size_required):
    is_under_limit = []
    for key in tree.keys():
        element = tree[key]
        if element["type"] == "dir" and element["size"] >= size_required:
            is_under_limit.append(element["size"])
        for elem in get_dirs_with_size(element["children"], size_required):
            is_under_limit.append(elem)
    return sorted(is_under_limit, reverse=True)

def main():
  inputs = get_inputs()
  inputs = preprocess(inputs)
  inputs = walk_dirs(inputs)
  inputs = calculate_folder_size(inputs)
  print(inputs)
  print("=====================")
  print("CALCULATION BEGINS")
  print("=====================")

    # total of input.txt: 46975962
    # 70000000 - 46975962
    #
    # 30000000 - 23024038
    #
    # need : 6'975'962

  # for example
#   size = get_dirs_with_size(inputs, 8381165)[-1]
#   print(size)
#   print("Test if example correct", size == 24933642)

  # for final
  dirs_ordered = get_dirs_with_size(inputs, 6975962)
  print(dirs_ordered)
  size = dirs_ordered[-1]
  print(size)

main()

