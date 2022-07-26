Packages Used:
    copy

How to run the code:

    Step1:
        1) python3 eight_puzzle.py
                 (or)
        2) python eight_puzzle.py
(depends on the configuration of your system)

    Step2:
    You will be prompted to enter the initial state as string (column-wise)
    Example:
        if the initial state is:
            -         -
            | 1  5  2 |
            | 4  0  3 |
            | 7  8  6 |
            -         -
           enter the input as 147508236  (no space)

    Step3:
    You will be prompted to enter the final state as string (coumn-wise)
    Example:
        if the initial state is:
            -         -
            | 1  2  3 |
            | 4  5  6 |
            | 7  8  0 |
            -         -
           enter the input as 147258360 (no space)

    Step 4:
    The output is displayed on the console as well as in the files generated.
    If the given puzzle is not solvable, then the nodePath will be empty and the output on the console will display the total number of nodes explored.

Note:
    The explored state is the one which has been explored with all the possible actions (A child itself is not considered as an explored state when it is generated).
    This algorithm doesn't generate the repetitive cases.
    The search exists when a child is a goal state and performs back tracking.
