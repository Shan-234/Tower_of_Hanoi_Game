from Stack import *
from typing import List
import random

def askDifficultyLevel() -> str:
    difficulty_level = str(input("Which level of difficulty would you prefer? "))
    if (difficulty_level == "E") or (difficulty_level == "M") or (difficulty_level == "H"):
        return difficulty_level
    else:
        return askDifficultyLevel()

def getStackSize(difficulty_level: str) -> int:
    if difficulty_level == "E":
        return 3
    elif difficulty_level == "M":
        return random.randint(4, 5)
    elif difficulty_level == "H":
        return random.randint(6, 8)

def createStacks(stack_size: int) -> List:
    stacks = []

    for i in range(3):
        new_stack = Stack()
        stacks.append(new_stack)

    for i in range(stack_size):
        stacks[0].push(stack_size - i)
    
    return stacks
    
def displayStacks(stacks: List[Stack]) -> None:
    print("\nYOUR STACKS:")
    print("A: " + str(stacks[0].stackToList()))
    print("B: " + str(stacks[1].stackToList()))
    print("C: " + str(stacks[2].stackToList()))

def ProblemSolved(stacks: List[Stack], stack_size: int) -> bool:
    return stacks[2].size == stack_size

def main():
    print("TOWER OF HANOI")

    print("\nINSTRUCTIONS:")
    print("1. You have three stacks (A, B, and C) and a number of disks of different sizes, initially stacked in decreasing order of size on stack A.")
    print("2. The goal is to move all disks from stack A to stack C.")
    print("3. A disk can only be placed on top of a larger disk or an empty rod.")
    print("4. No disk can be placed on top of a smaller disk.")
    print("5. Only one disk can be moved at a time.")

    # Asks user to choose level of difficulty:
    print("\nLEVEL OF DIFFICULTY:")
    print("(E) - Easy")
    print("(M) - Medium")
    print("(H) - Hard")
    difficulty_level = askDifficultyLevel()

    # Creates and displays stacks:
    stack_size = getStackSize(difficulty_level)
    stacks = createStacks(stack_size)
    displayStacks(stacks)

    

if __name__ == "__main__":
    main()