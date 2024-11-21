def compute_level_sets(candidates):
    """Computes level sets based on the first violated constraint."""
    level_sets = {}
    for candidate in candidates:
        first_violation = find_first_violation(candidate)
        if first_violation not in level_sets:
            level_sets[first_violation] = []
        level_sets[first_violation].append(candidate)
    return level_sets
