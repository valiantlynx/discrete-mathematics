# # validate_regex.py

# import re

# def validate_regex(pattern, positive_cases, negative_cases):
#     regex = re.compile(pattern)
#     results = {
#         'matches': [case for case in positive_cases if regex.fullmatch(case)],
#         'non_matches': [case for case in negative_cases if not regex.fullmatch(case)]
#     }
#     return results

# # Example usage
# if __name__ == "__main__":
#     pattern = r"g+ x* o s?"
#     positive_cases = ["gggggo", "ggggxxo", "gggo", "ggxxxo"]
#     negative_cases = ["g", "gggxoooss", "gooo", "o"]

#     print(validate_regex(pattern, positive_cases, negative_cases))

import re
import regex  # External library

def validate_regex(pattern, positive_cases, negative_cases):
    # Compile pattern with both libraries
    regex_standard = re.compile(pattern)
    regex_extended = regex.compile(pattern)
    
    # Results from re module
    re_results = {
        'matches': [case for case in positive_cases if regex_standard.fullmatch(case)],
        'non_matches': [case for case in negative_cases if not regex_standard.fullmatch(case)]
    }

    # Results from regex module
    regex_results = {
        'matches': [case for case in positive_cases if regex_extended.fullmatch(case)],
        'non_matches': [case for case in negative_cases if not regex_extended.fullmatch(case)]
    }

    # Ensure consistency between the two libraries' results
    if re_results != regex_results:
        print("Warning: Inconsistency between re and regex results.")
    else:
        print("Results are consistent between re and regex libraries.")

    # Return both results for comparison
    return {'re_results': re_results, 'regex_results': regex_results}

# Example usage
if __name__ == "__main__":
    pattern = r"g+ x* o s?"
    positive_cases = ["gggggo", "ggggxxo", "gggo", "ggxxxo"]
    negative_cases = ["g", "gggxoooss", "gooo", "o"]

    results = validate_regex(pattern, positive_cases, negative_cases)
    print("Results from re library:", results['re_results'])
    print("Results from regex library:", results['regex_results'])
