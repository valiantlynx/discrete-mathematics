from automata.fa.dfa import DFA
import pprint  # For pretty-printing the dictionary
import frozendict  # Import frozendict to check for this type

# Define DFA
dfa = DFA(
    states={'D', 'I', 'N', 'Y', 'B', 'A'},
    input_symbols={'Z', 'H'},
   transitions = {
    'D': {'Z': 'D', 'H': 'A'},
    'I': {'Z': 'Y', 'H': 'D'},
    'N': {'Z': 'I', 'H': 'D'},
    'Y': {'Z': 'I', 'H': 'B'},
    'B': {'Z': 'A', 'H': 'Y'},
    'A': {'Z': 'B', 'H': 'Y'}
}
,
    initial_state='I',  # Assuming 'O' as the initial state from the image
    final_states={'D', 'B', 'A'}  # Assuming 'O' and 'Y' as accepting states based on double circles
)

# Minimize DFA
minimized_dfa = dfa.minify()

# Recursive function to convert frozendict to dict
def convert_to_dict(data):
    if isinstance(data, frozendict.frozendict):
        return {k: convert_to_dict(v) for k, v in data.items()}
    elif isinstance(data, dict):
        return {k: convert_to_dict(v) for k, v in data.items()}
    else:
        return data

# Convert the minimized DFA transitions to a readable format
minimized_transitions = convert_to_dict(minimized_dfa.transitions)

# Print minimized transitions to check which states need mapping
print("Minimized transitions:", minimized_transitions)

# Example mapping based on observed states in minimized output
# Update this mapping as needed based on the minimized DFA structure
numeric_to_label_mapping = {
    0: 'D',
    1: 'I',
    2: 'N',
    3: 'Y',
    4: 'B',
    5: 'A'
}

# Apply the mapping to the minimized transitions
labeled_transitions = {
    numeric_to_label_mapping[state]: {input_symbol: numeric_to_label_mapping[target]
                                      for input_symbol, target in transitions.items()}
    for state, transitions in minimized_transitions.items()
}

# Pretty-print the labeled transitions
pprint.pprint(labeled_transitions)
