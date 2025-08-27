# version13

Some small adjustments to the game, the addition of a fire being the main change.

## new game concepts
* Opening the book while holding the candle starts a fire, which runs in the background to your actions.

## new coding concepts
* As the game gets larger manually testing it gets more time consuming. Using the 'unittest' module to run end-to-end automation allow checking all the game scenarios.
* Renaming the 'game' folder as 'base', as otherwise it makes importing 'game.py' hard to import into tests
* `take_item` now returns a boolean if successful, to allow locations/things to extend it
* Adding a separate `reset_map` - as the Location objects are only created once, their 'items' are not correctly reset between games. This probably means a bug in earlier versions.

