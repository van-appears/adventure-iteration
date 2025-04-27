# version05

Adding another room and a few other items creates a lot of extra states. Tracking all the states is quite hard; especially since most of them probably wouldn't ever even get actioned; there may be branches I've missed (including ones I've deliberately ignored at present, like taking the honey and eating it in a different room to the kitchen).
Instructions, inventory and a 'go to' command would be useful.
As well as the 'room' handlers, each item should probably have its own handler too. That might need much better parsing logic to split verb and noun parts of the sentence.

## new game concepts
* third room added
* additional actions `consume`, `pet`, `give`, `attack`, `describe`
* rooms only show their description the first time they are visited
* jeopardy! attacking the bear leads to death - game over without escaping

## new coding concepts
* compound `if` statements
* a dictionary of `state` rather than individual variables
* using a `set` for recording the inventory of items the player holds
* additional methods `add_item` and `has_item` for updating the inventory
