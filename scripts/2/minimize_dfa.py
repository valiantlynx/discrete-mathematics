# minimize_dfa.py

def minimize_dfa(states, alphabet, transitions, start_state, accept_states):
    partitions = [set(accept_states), set(states) - set(accept_states)]
    
    def get_transition_class(state, char):
        for i, part in enumerate(partitions):
            if transitions[state].get(char) in part:
                return i
        return -1

    while True:
        new_partitions = []
        for part in partitions:
            classes = {}
            for state in part:
                key = tuple(get_transition_class(state, char) for char in alphabet)
                classes.setdefault(key, set()).add(state)
            new_partitions.extend(classes.values())
        if new_partitions == partitions:
            break
        partitions = new_partitions

    return [list(part) for part in partitions]

# Example usage
if __name__ == "__main__":
    states = {'A', 'B', 'C', 'D'}
    alphabet = {'0', '1'}
    transitions = {
        'A': {'0': 'B', '1': 'C'},
        'B': {'0': 'A', '1': 'D'},
        'C': {'0': 'D', '1': 'A'},
        'D': {'0': 'C', '1': 'B'}
    }
    start_state = 'A'
    accept_states = {'D'}

    print(minimize_dfa(states, alphabet, transitions, start_state, accept_states))

