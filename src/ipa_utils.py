import csv
from collections import namedtuple

# Define a named tuple for features
FeatureSet = namedtuple('FeatureSet', ['syllabic', 'stress', 'long', 'consonantal', 'sonorant', 
                                       'continuant', 'delayed_release', 'approximant', 'tap', 'trill', 
                                       'nasal', 'voice', 'spread_gl', 'constr_gl', 'labial', 'round', 
                                       'labiodental', 'coronal', 'anterior', 'distributed', 'strident', 
                                       'lateral', 'dorsal', 'high', 'low', 'front', 'back', 'tense'])

class DistinctiveFeaturesLoader:
    def __init__(self, csv_filename='../data/distinctive_features.csv'):
        self.csv_filename = csv_filename
        self.features_dict = self.load_distinctive_features()

    def load_distinctive_features(self):
        """Loads the distinctive features from the CSV file and stores them in a dictionary."""
        features_dict = {}
        try:
            with open(self.csv_filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    ipa_symbol = row['IPA']
                    features = FeatureSet(
                        syllabic=row['syllabic'],
                        stress=row['stress'],
                        long=row['long'],
                        consonantal=row['consonantal'],
                        sonorant=row['sonorant'],
                        continuant=row['continuant'],
                        delayed_release=row['delayed release'],
                        approximant=row['approximant'],
                        tap=row['tap'],
                        trill=row['trill'],
                        nasal=row['nasal'],
                        voice=row['voice'],
                        spread_gl=row['spread gl'],
                        constr_gl=row['constr gl'],
                        labial=row['LABIAL'],
                        round=row['round'],
                        labiodental=row['labiodental'],
                        coronal=row['CORONAL'],
                        anterior=row['anterior'],
                        distributed=row['distributed'],
                        strident=row['strident'],
                        lateral=row['lateral'],
                        dorsal=row['DORSAL'],
                        high=row['high'],
                        low=row['low'],
                        front=row['front'],
                        back=row['back'],
                        tense=row['tense']
                    )
                    features_dict[ipa_symbol] = features
        except FileNotFoundError:
            print(f"Error: The file '{self.csv_filename}' was not found.")
        except KeyError as e:
            print(f"Error: Missing column in CSV file: {e}")
        
        return features_dict

    def get_features(self, ipa_symbol):
        """Retrieves the distinctive features for a given IPA symbol."""
        return self.features_dict.get(ipa_symbol, None)
    
    def get_single_feature(self, ipa_symbol, feature_name):
        """Retrieves the value of a single feature for a given IPA symbol."""
        features = self.get_features(ipa_symbol)
        if features:
            return getattr(features, feature_name)
        return None

    '''
    def get_single_feature_two_symbols(self, ipa_symbol1, ipa_symbol2, feature_name):
        """Retrieves the value of a single feature for two given IPA symbols."""
        features1 = self.get_features(ipa_symbol1)
        features2 = self.get_features(ipa_symbol2)
        if features1 and features2:
            return getattr(features1, feature_name), getattr(features2, feature_name)
        return None, None
    '''

    def get_single_feature_string(self, feature_name, ipa_string):
        """Retrieves the value of a single feature for each character in the given IPA string."""
        feature_values = []
        for char in ipa_string:
            feature_value = self.get_single_feature(char, feature_name)
            feature_values.append((char, feature_value))
        return feature_values


# Create an instance of the loader
loader = DistinctiveFeaturesLoader()

# Test the loader
# print(loader.get_features('t'))
# print(loader.get_single_feature('t', 'voice'))
# print(loader.get_single_feature_two_symbols('t', 'd', 'voice'))

class IPACharacterExtractor:
    def __init__(self, ipa_string):
        self.ipa_string = ipa_string.strip('/')

    def get_last_character(self):
        """Returns the last character of the IPA string before the closing '/'."""
        return self.ipa_string[-1] if self.ipa_string else None

    def get_last_two_characters(self):
        """Returns the last two characters of the IPA string before the closing '/'."""
        return self.ipa_string[-2:] if len(self.ipa_string) >= 2 else None

    def get_second_to_last_character(self):
        """Returns the second to last character of the IPA string before the closing '/'."""
        return self.ipa_string[-2] if len(self.ipa_string) >= 2 else None

    def get_first_character(self):
        """Returns the first character of the IPA string after the opening '/'."""
        return self.ipa_string[0] if self.ipa_string else None

# Example usage
ipa_input = "/ˈfɫaɪz/"
extractor = IPACharacterExtractor(ipa_input)

# Extract characters
last_char = extractor.get_last_character()
last_two_chars = extractor.get_last_two_characters()
second_to_last_char = extractor.get_second_to_last_character()

# Use the distinctive features loader with extracted characters
# print(loader.get_features(last_char))
# print(loader.get_features(last_two_chars))
# print(loader.get_features(second_to_last_char))