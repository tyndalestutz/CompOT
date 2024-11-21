def no_final_consonant(candidate):
    """Example simple constraint: No final consonants."""
    if candidate.endswith("C"):  # Simplified check
        return 1  # Violation
    return 0  # No violation

def constraints_library():
    """Returns a dictionary of all constraints."""
    return {
        "NoFinalConsonant": no_final_consonant,
        # Add more constraints here
    }
