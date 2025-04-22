# version06

While no changes in the game itself this version has a lot of step-up in terms of procedures.
One useful change is to move STATE to a constant so we don't have to keep passing it around, _and_ by checking for keywords using the `in` command we can skip having to preset every state option.
The map has been moved to a constant and methods `describe_map` and `move` added as a catch-all way to get around (though would proably break again if we added staircases).

Still no instructions, inventory, 'move to' or 'quit' commands, or retry if you die, and the bug where you can only eat the honey in the kitchen still exists.
