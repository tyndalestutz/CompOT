from ipa_utils import parse_ipa, format_ipa
from eval import eval_candidate, generate_violation_profile
from candgen import generate_candidates
from level_sets import compute_level_sets
from constraints import constraints_library

def main():
    # Step 1: Load dictionary inputs
    dictionary = load_dictionary("path/to/dictionary.json")  # Input dictionary
    input_ipa = dictionary["input"]  # Example input
    output_ipa = dictionary["output"]  # Example output

    # Step 2: Parse IPA
    fully_faithful_candidate = parse_ipa(input_ipa)
    winning_candidate = parse_ipa(output_ipa)

    # Step 3: Evaluate initial candidates
    ff_violation_profile = generate_violation_profile(fully_faithful_candidate, constraints_library)
    wc_violation_profile = generate_violation_profile(winning_candidate, constraints_library)

    # Step 4: Generate candidates iteratively
    candidates = generate_candidates(fully_faithful_candidate, constraints_library)

    # Step 5: Evaluate final OT tableaux
    level_sets = compute_level_sets(candidates)
    selected_winner = select_winner(level_sets)

    # Step 6: Output results
    if selected_winner == winning_candidate:
        print("Winning candidate correctly selected!")
    else:
        print(f"Error: {selected_winner} selected instead of {winning_candidate}")

if __name__ == "__main__":
    main()
