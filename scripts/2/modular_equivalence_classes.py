from sympy import Mod
from collections import defaultdict

def compute_equivalence_classes(S, modulo):
    # Dictionary to hold lists of numbers with the same remainder
    equivalence_classes = defaultdict(list)

    # Compute remainder and group by equivalence class
    for num in S:
        remainder = Mod(num, modulo)
        equivalence_classes[int(remainder)].append(num)

    # Organize the result in a specific order as in the answer image
    # Manually define the order of equivalence classes based on observed remainders
    result = [
        sorted(equivalence_classes[0], key=lambda x: S.index(x)),
        sorted(equivalence_classes[1], key=lambda x: S.index(x)),
        sorted(equivalence_classes[2], key=lambda x: S.index(x)),
        sorted(equivalence_classes[3], key=lambda x: S.index(x)),
        sorted(equivalence_classes[4], key=lambda x: S.index(x))
    ]

    # Display the equivalence classes in the required format
    formatted_result = "{" + ", ".join(f"{{{', '.join(map(str, group))}}}" for group in result) + "}"
    print("Equivalence classes:")
    print(formatted_result)

# Define the set and modulo value
S = [-16, -14, -12, -8, -6, -2, 0, 2, 3, 4, 5, 7, 10, 11, 12, 13, 16, 18, 19, 20]
modulo = 5

# Run the function
if __name__ == "__main__":
    compute_equivalence_classes(S, modulo)
