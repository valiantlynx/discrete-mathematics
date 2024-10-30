# # introduce_local_variable.py

# def introduce_local_variable(spec_statement, var_name, var_type, initial_value):
#     refined_statement = f"VAR {var_name}:{var_type} . {var_name}:={initial_value}; {spec_statement}"
#     return refined_statement

# # Example usage
# if __name__ == "__main__":
#     spec_statement = "{ n > p } n,p:=n',p' | n' < 11 and p' < n"
#     var_name = "W"
#     var_type = "Nat"
#     initial_value = 1

#     print(introduce_local_variable(spec_statement, var_name, var_type, initial_value))

from sympy import symbols, Eq

def introduce_local_variable(spec_statement, var_name, var_type, initial_value):
    # Define the variable symbolically
    var = symbols(var_name, integer=True if var_type == "Nat" else None)
    
    # Construct the variable introduction as a symbolic expression
    intro_var_statement = f"VAR {var_name}:{var_type} . {var_name}:={initial_value}; {spec_statement}"
    
    return intro_var_statement

# Example usage
if __name__ == "__main__":
    # Original specification statement
    spec_statement = "{ n > p } n,p:=n',p' | n' < 11 and p' < n"
    var_name = "W"
    var_type = "Nat"  # Here, Nat indicates a natural number
    initial_value = 1

    # Print the refined specification with the introduced local variable
    refined_spec = introduce_local_variable(spec_statement, var_name, var_type, initial_value)
    print("Refined Specification Statement:")
    print(refined_spec)
