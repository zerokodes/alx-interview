#!/usr/bin/python3
"""A python module that determines if all boxes can be opened
   from a list of lists
"""


def canUnlockAll(boxes=[]):
    """A function that returns True of all box in
    boxes can be opend
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True

    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]

        for key in keys:
            if key >= 0 and key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
