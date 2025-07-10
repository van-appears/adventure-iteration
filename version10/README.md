# version10

Again, another refactor iteration - 'inventory' and locations now are two types of the same thing - a 'Container'. This allows a common 'take' method for locations. It is a step towards make items classes too.

## new game concepts
* None

## new coding concepts
* Using a tuple for the verb and noun and passing those around rather than having to keep using is_synonym_of
