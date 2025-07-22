# version11

Another refactor iteration. Items that you can interact with, even immovable ones, are now instances of a Thing.
This was again another big refactor and possibly breaks the original 'thought experiment' of a learner slowly adding little bits to a project. All of this coould have been done, probably, by having individual method files same as there were in `version08` - but would mean repeating blocks of code for taking and describing things, as could already be seen in version08/kitchen.py.

## new game concepts
* You can now eat the honey in any room!

## new coding concepts
* First example of recursion in the Container `find_item_with_key` method
* Multiple types of polymorphism - Location and Thing both extend Container
