# validate_regex.py

import re

def validate_regex(pattern, positive_cases, negative_cases):
    regex = re.compile(pattern)
    results = {
        'matches': [case for case in positive_cases if regex.fullmatch(case)],
        'non_matches': [case for case in negative_cases if not regex.fullmatch(case)]
    }
    return results

# Example usage
if __name__ == "__main__":
    pattern = r"g+ x* o s?"
    positive_cases = ["gggggo", "ggggxxo", "gggo", "ggxxxo"]
    negative_cases = ["g", "gggxoooss", "gooo", "o"]

    print(validate_regex(pattern, positive_cases, negative_cases))
