# Define the truth values for p and q for each row
truth_values = [
    (0, 0),  # Row 1: p is false, q is false
    (0, 1),  # Row 2: p is false, q is true
    (1, 0),  # Row 3: p is true, q is false
    (1, 1),  # Row 4: p is true, q is true
]

# Define a function to evaluate the implication
def implies(p, q):
    return not p or q

# List to hold the truth value of the whole statement for each row
statement_truth_values = []

# Evaluate the statement for each row
for p, q in truth_values:
    p_implies_q = implies(p, q)
    first_part = p and p_implies_q
    whole_statement = implies(first_part, q)
    statement_truth_values.append(whole_statement)

print(statement_truth_values)
