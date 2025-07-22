SYNONYMS = {
    "move to": ["move to", "head to", "go to", "walk to", "run to"],
    "move": ["move", "head", "go", "walk", "run"],
    "take": ["take", "get", "collect", "pick up"],
    "open": ["open", "unlock"],
    "close": ["close"],
    "attack": ["attack", "kick", "punch", "fight"],
    "pet": ["pet", "stroke", "cuddle", "pat"],
    "consume": ["consume", "eat", "drink"],
    "give": ["give", "throw", "drop"],
    "read": ["read"],
    "find": ["find", "locate"],
    "describe": ["describe", "look"],
    "quit": ["quit", "exit"]
}

def parse_action(action_string):
    action_string = action_string.strip().lower()
    for parent_verb in SYNONYMS:
        for synonym in SYNONYMS[parent_verb]:
            if action_string.startswith(f"{synonym} ") or action_string == synonym:
                noun = action_string[len(synonym)::].strip()
                if len(noun) == 0:
                    return (parent_verb, None)
                else:
                    return (parent_verb, noun)
    return (action_string, None)
