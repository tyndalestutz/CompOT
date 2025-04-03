from ipa_utils import loader

# constraints.py


class Constraint:
    """
    Base class for all constraints. Each constraint should implement the `evaluate` method.
    """
    def evaluate(self, input_data):
        raise NotImplementedError("Subclasses must implement the evaluate method.")

class AgreeConstraint(Constraint):
    """
    Implements the AGREE constraint in Optimality Theory.
    Assigns a violation mark for adjacent consonants that do not share the same 'voice' feature.
    """
    def evaluate(self, input_data):
        """
        Evaluates the input for violations of the AGREE constraint.

        Args:
            input_data (str): The input string to evaluate.

        Returns:
            int: The number of violations found.
        """
        violations = 0
        current_feature = 'voice'
        features = loader.get_single_feature_string(current_feature, input_data)

        for i in range(len(features) - 1):
            current = features[i]
            next_char = features[i + 1]

            # Check if both are consonants and their 'voice' features differ
            if current[0] == 'consonant' and next_char[0] == 'consonant':
                if current[1] != next_char[1]:
                    violations += 1

        return violations

# Example usage
if __name__ == "__main__":
    # Example input string (replace with actual input)
    input_data = "tʃ"

    # Create an instance of the AGREE constraint
    agree_constraint = AgreeConstraint()

    # Evaluate the input string
    violation_count = agree_constraint.evaluate(input_data)
    print(f"Number of violations: {violation_count}")