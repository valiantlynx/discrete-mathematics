# modular_equivalence_classes.py

def modular_equivalence_classes(S, modulo):
    classes = {}
    for num in S:
        remainder = num % modulo
        if remainder not in classes:
            classes[remainder] = set()
        classes[remainder].add(num)
    return [list(eq_class) for eq_class in classes.values()]

# Example usage
if __name__ == "__main__":
    S = [-13, 0, 13, 1, 2, 15, 3, 16, 19, 6, -6, 7, -18, -5, 8, -4, 9, 10, -2, 11]
    modulo = 5

    print(modular_equivalence_classes(S, modulo))
