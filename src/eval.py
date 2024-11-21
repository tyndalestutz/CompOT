def eval_candidate(candidate, constraint):
    """Evaluates a candidate against a single constraint."""
    return constraint(candidate)

def generate_violation_profile(candidate, constraints_library):
    """Generates a violation profile for a candidate."""
    profile = {}
    for constraint_name, constraint_func in constraints_library.items():
        profile[constraint_name] = eval_candidate(candidate, constraint_func)
    return profile
