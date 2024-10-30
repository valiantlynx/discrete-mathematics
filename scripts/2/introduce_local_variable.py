# introduce_local_variable.py

def introduce_local_variable(spec_statement, var_name, var_type, initial_value):
    refined_statement = f"VAR {var_name}:{var_type} . {var_name}:={initial_value}; {spec_statement}"
    return refined_statement

# Example usage
if __name__ == "__main__":
    spec_statement = "{ n > p } n,p:=n',p' | n' < 11 and p' < n"
    var_name = "W"
    var_type = "Nat"
    initial_value = 1

    print(introduce_local_variable(spec_statement, var_name, var_type, initial_value))
