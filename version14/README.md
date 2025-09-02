# version14

After making the chest useless in the last version, this version reintroduces a use for it.

## new game concepts
* The chest has a combination lock, so needs an interactive prompt
* There are now good and bad endings, where if you escape the house when the bear is spooked you still lose!

## new coding concepts
* Both the cupboard key and front door key can be collected using the simple 'take key', which required changes to the container and location objects
* The 'input' method is now held in state, to allow the chest to access the same method as the rest of the game - hence allowing automated tests to also enter the combination
