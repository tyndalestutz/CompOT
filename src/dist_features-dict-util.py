# For the sake of interfacing while troubleshooting, 
# this file will remain as a utility script for now.


import csv

def load_distinctive_features(csv_filename):
    # Initialize an empty dictionary for all symbols
    features_dict = {}
    
    # Read the CSV file
    with open(csv_filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # Assuming your CSV has columns like 'IPA', 'Feature1', 'Feature2', etc.
            ipa_symbol = row['IPA']
            features = {key: row[key] for key in row if key != 'IPA'}
            
            # Add the IPA symbol and its features to the dictionary
            features_dict[ipa_symbol] = features
            
    return features_dict

# Example of usage
csv_filename = '../data/distinctive_features.csv'  # Replace with your CSV file path
features_dict = load_distinctive_features(csv_filename)

# Accessing the features of a particular IPA symbol
ipa_example = 'ð'
if ipa_example in features_dict:
    print(f"Features for '{ipa_example}': {features_dict[ipa_example]}")
else:
    print(f"IPA symbol '{ipa_example}' not found.")