# version12

Trying to reuse the pattern established in version11 - so was easily able to add the landing and bedroom, as well as the hammer, bottle and candle.

## new game concepts
* The stairs are a corridor; you pass through them without visiting.
* You can only read a book if you have a lit candle.

## new coding concepts
* `hasattr` used to determine if a room is a corridor or not; by whether it has the `pass_through` method. In this game there are only a few rooms, but in a larger map it'd be harder to tell if you were upstairs or downstairs without some additional attributes.
* The candle has to affect the internal state of the matches (by reducing the match count by 1)
