def generate_candidates(initial_candidate, constraints_library):
    """Generates candidates until all constraints are violated."""
    candidates = [initial_candidate]
    violated_constraints = set()

    while len(violated_constraints) < len(constraints_library):
        for constraint_name, constraint_func in constraints_library.items():
            if constraint_name not in violated_constraints:
                # Generate a candidate that violates this constraint
                new_candidate = generate_violation_candidate(initial_candidate, constraint_func)
                candidates.append(new_candidate)
                # Update violated constraints
                violation_profile = generate_violation_profile(new_candidate, constraints_library)
                if violation_profile[constraint_name] > 0:
                    violated_constraints.add(constraint_name)
                break
    return candidates
