# version03

Adding one more item to interact with, a box containing the key. This is really now showing how quickly the 'if' statements expand as we need to track different descriptions based on a number of different states. Added a 'synonym' dictionary as a very simplistic language parsing mechanism with a function to interogate it. Also added a 'describe' function to repeat the room description.

This also introduces scoping issues; the `is_synonym_of` function has to call its variable `action_string` so that it is different from `action` variable in the while loop. In the next iteration that while loop may need to be moved into a 'main' function.
