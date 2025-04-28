# version08

Split code into multiple files, again for readability, then importing them into other files.
Also adding one more room; though to be honest the main issue with this game is that the basic happy path is the one that wins!

## new game concepts
* One more room, a library

## new coding concepts
* __init.py__ needed to separate code into separate files
* also worth noting that 'parser' is already a python module, so here we use 'action_parser' instead.
* importing multiple functions from a file
* `if __name__ == "__main__":` in the main game file
* aside: also needs adding __pycache__ to .gitignore!
