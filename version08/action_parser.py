SYNONYMS = {
    "move": ["move", "head", "go", "walk", "run"],
    "move to": ["move to", "head to", "go to", "walk to", "run to"],
    "take": ["take", "get", "collect", "pick up"],
    "open": ["open", "unlock"],
    "close": ["close"],
    "attack": ["attack", "kick", "punch", "fight"],
    "pet": ["pet", "stroke", "cuddle", "pat"],
    "consume": ["consume", "eat", "drink"],
    "give": ["give", "throw", "drop"]
}

def starts_with_synonym(action_string, verb):
    for synonym in SYNONYMS[verb]:
        if action_string.startswith(f"{synonym} "):
            return True
    return False

def is_synonym_of(action_string, verb, noun):
    for synonym in SYNONYMS[verb]:
        if action_string == f"{synonym} {noun}":
            return True
    return False
