from Stack import *
from typing import List
import random

def getIndex(stack_letter: str) -> int:
    return ord(stack_letter) - 65

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

def MoveDisk(stacks: List[Stack], from_stack: str, to_stack: str) -> bool:
    """
    Moves a disk from stack (from_stack) to stack (to_stack). Returns boolean
    indicating whether or not the disk could be moved.

    :param stacks: List of stacks to be modified in place.
    """
    from_index = getIndex(from_stack)
    to_index = getIndex(to_stack)

    if from_index == to_index:
        return False
    else:
        if stacks[from_index].isEmpty():
            return False
        elif not stacks[to_index].isEmpty():
            if stacks[from_index].top.val > stacks[to_index].top.val:
                return False
        value = stacks[from_index].pop()
        stacks[to_index].push(value)
        return True


def main():
    print("TOWER OF HANOI")

    # Displays Instructions:
    print("\nINSTRUCTIONS:")
    print("1. You have three stacks (A, B, and C) and a number of disks of different sizes, initially stacked in decreasing order of size on stack A.")
    print("2. The goal is to move all disks from stack A to stack C.")
    print("3. A disk can only be placed on top of a larger disk or an empty stack.")
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

    # Keeps prompting user to move stacks until the problem is solved:
    move_count = 0
    min_moves = (2 ** (stack_size)) - 1
    print("\nThis game can be completed in " + str(min_moves) + " moves.")
    while not ProblemSolved(stacks, stack_size):
        displayStacks(stacks)
        from_stack = input("Which stack would you like to move from? ")
        to_stack = input("Which stack would you like to move to? ")
        moved = MoveDisk(stacks, from_stack, to_stack)
        if moved:
            move_count += 1
    
    # Displays that stacks one final time and indicates that the problem is solved:
    displayStacks(stacks)
    print("\nCongratulations! You completed the game.")
    if (move_count - min_moves) == 0:
        print("You took the minimum number of moves to complete the game.")
    else:
        print("You took " + str(move_count - min_moves) + " more moves than the minimum to complete the game.")


    

if __name__ == "__main__":
    main()