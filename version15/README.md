# version15

Final iteration (for now)

## new game concepts
* The combination and the book in the library are now taken at random from small lists, so you can't shortcut the game by just memorising values.

## new coding concepts
* 'Earthsea' has been replaced by a generic 'Book' - this only gets initialised at the point of reading, as otherwise it causes a circular import error (state -> rooms -> library -> book -> state)

# Final thoughts

Is the game perfect? No. There's lots more could be done here e.g.
- the bear is stationary, could be mobile and lead to more interesting puzzles about scaring it off.
- the 'long_description' and 'short_description' methods would probably be better returning strings than printing them, in order to aid unit testing.
- the game could be extended with NPC or conversation trees, and multiple locations
- 'verb noun' is limited, and relies a lot on context
but then this was just meant to be a thought experiment, about whether coding ideas be introduced bit by bit in a way that would be extending but still 'fun' to learn.
