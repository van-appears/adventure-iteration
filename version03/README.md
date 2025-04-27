# version03

Adding one more item to interact with, a box containing the key. This is really now showing how quickly the 'if' statements expand as we need to track different descriptions based on a number of different states. Added a 'synonym' dictionary as a very simplistic language parsing mechanism with a function to interogate it. Also added a 'describe' function to repeat the room description.

## new game concepts
* actions `take`, `open`, `close` and synonyms of those
* multiple states; we now also have `chest_open` and `chest_opened`
* context-specific descriptions - the room is decribed differently depending on the state of the chest, and the chest needs different descriptions depending on whether you have the key.

## new coding concepts
* a dictionary called `synonyms` containing arrays
* a function `is_synonym_of` for determining if an action matches an entry in the synonym dictionary
* scoping issues; the `is_synonym_of` function has to call its variable `action_string` so that it is different from `action` variable in the while loop.
