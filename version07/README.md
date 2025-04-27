# version07

Added first new python concept in a while, an import of "os" in order to clear the console before playing the game.
Added 'instructions', 'inventory', 'quit' and 'move to' commands - mildly interesting coding lesson from testing is that 'go to' check must come before 'go' check, as the latter would always be found first given it is a substring of the former.
Also added an outer loop for replay should the player die. Another small coding lesson - in order to replay we must reset anything we previously set, which is easy for the STATE but not so easy for the MAP. Perhaps that shows storing the 'visited' values in the map is a bad idea?
And eating honey only in the the kitchen bug is still there too.

## new game concepts
* `instructions` command that gives basic instructions
* `inventory` command that shows what the player is carrying
* `quit` as a way to exit the game early
* `move to` to allow easier moving between named locations
* 'play again' option if you finish or die

## new coding concepts
* import of `os.system` in order to clear the screen
* `is` keyword for exact boolean matching
* dictionary `clear` method
* outer gaming loop
