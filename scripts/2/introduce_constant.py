from sympy import symbols, Eq

def apply_introduce_constant():
    # Define the constant to be introduced using SymPy
    Z = symbols("Z", integer=True)
    Z_value = 6

    # Define other variables
    r, i, p, i_prime, p_prime, r_prime = symbols("r i p i' p' r'", integer=True)

    # Define the original specification statement components
    precondition = Eq(r < i, True)
    assignment = f"p,i,r := {p_prime},{i_prime},{r_prime}"
    postcondition = Eq(i_prime >= p, True) | Eq(p_prime >= i, True)

    # Apply the refinement rule "Introduce Constant"
    refined_precondition = Eq(Z, Z_value) & precondition
    refined_statement = (
        f"CON Z:Nat | Z={Z_value} . {{ {refined_precondition} }} "
        f"{assignment} | {postcondition}"
    )

    # Output the refined specification
    print("Refined Specification Statement:")
    print(refined_statement)

# Execute the function
if __name__ == "__main__":
    apply_introduce_constant()
