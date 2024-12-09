## 1. Computational Problem Specification

### The Acceptance Problem for DFA

The computational problem being decided is the **Acceptance Problem for DFA (Deterministic Finite Automaton)**. Given a DFA and an input string, the problem is to determine whether the input string is accepted or rejected by the DFA.

### Problem Definition

A DFA is represented by:
- A finite set of states.
- A finite alphabet.
- A transition function, which defines how the DFA moves from one state to another based on input symbols.
- A start state.
- A set of accept states.

The task is to determine if the given input string, when ran on the given DFA, ends in an accept state.

## 2. Program Documentation

### Input Parsing

The program reads the input as a string containing two parts separated by `###`. The first part defines the DFA, and the second part is the input string to be tested. The DFA part is parsed into a dictionary-like structure, including:
- `states`: A list of states in the DFA.
- `alphabet`: A list of input symbols.
- `transition`: A dictionary defining state transitions (tuples of state and symbol as keys).
- `start_state`: The initial state of the DFA.
- `accept_states`: A list of states where the DFA accepts the string.

The input string is stripped of any extra whitespace and processed symbol by symbol. The program checks if the DFA transitions from state to state correctly, ultimately determining if the string is accepted based on whether the final state is in `accept_states`.

## 3. Example Strings

### Example 1: String in the Set (Accepted by the DFA)

```
'''
{
    "states": ["q0", "q1", "q2", "q3"],
    "alphabet": ["a", "b", "$"],
    "transition": {
        "('q0', 'a')": "q1",
        "('q1', 'b')": "q2",
        "('q2', 'a')": "q1",
        "('q2', '$')": "q3"
    },
    "start_state": "q0",
    "accept_states": ["q0", "q3"]
}###ababab$
'''
```

This string is in the set because it includes all 5 parts of the formal definition for a DFA, the states, alphabet, transition function, start state, and accept states, all formatted correctly according to the program.
The delimiter `###` immediately follows with an input string to check against the DFA.


### Example 2: String not in the Set (Rejected by the DFA)

```
'''
{
    "states": ["q0", "q1", "q2", "q3"],
    "alphabet": ["a", "b", "c"],
    "transition": {
        "('q0', 'a')": "q1",
        "('q1', 'b')": "q2",
        "('q2', 'a')": "q1",
        "('q2', 'c')": "q3"
    },
    "start_state": "q0",
    "accept_states": ["q0", "q3"]
}###ababac
'''
```

This string is not in the set, though it follows a similar format to the above accepted string. This string represents a valid DFA and input string. However, the DFA end up reading the `c`
character while in `q1`, for which there is no defined transition, so the DFA rejects the input string.

## 4. The Code
```
import json

def parse_input(string_representation):
    try:
        dfa_string, input_string = string_representation.split("###", 1)
        dfa = json.loads(dfa_string)
        input_string = input_string.strip()
        
        required_keys = ['states', 'alphabet', 'transition', 'start_state', 'accept_states']
        if required_keys != list(dfa.keys()):
            raise ValueError("DFA is missing required keys.")
        
        if not isinstance(dfa['transition'], dict):
            raise ValueError("Transition function must be a dictionary.")
        
        dfa['transition'] = {eval(k): v for k, v in dfa['transition'].items()}
        
        return dfa, input_string
    
    except Exception as e:
        raise e
        
    
# Note that all trailing blankspace in the input string will not be counted as
# part of the input string
def adfa(string_representation):
    try:
        dfa, input_string = parse_input(string_representation)
        print("Input String: " + input_string)

        current_state = dfa['start_state']
        for symbol in input_string:
            print(current_state, symbol)

            if (current_state, symbol) not in dfa['transition']:
                print("Failed Transition")
                return False
            
            current_state = dfa['transition'][(current_state, symbol)]

        print(current_state, "FINAL STATE")
        return current_state in dfa['accept_states']
    
    except Exception as e:
        print(e)
        return False
```

### The Testing
```
accepting_valid_nonempty_input = '''
{
    "states": ["q0", "q1", "q2", "q3"],
    "alphabet": ["a", "b", "$"],
    "transition": {
        "('q0', 'a')": "q1",
        "('q1', 'b')": "q2",
        "('q2', 'a')": "q1",
        "('q2', '$')": "q3"
    },
    "start_state": "q0",
    "accept_states": ["q0", "q3"]
}###ababab$

rejecting_valid_nonempty_input = '''
{
    "states": ["q0", "q1", "q2", "q3"],
    "alphabet": ["a", "b", "c"],
    "transition": {
        "('q0', 'a')": "q1",
        "('q1', 'b')": "q2",
        "('q2', 'a')": "q1",
        "('q2', 'c')": "q3"
    },
    "start_state": "q0",
    "accept_states": ["q0", "q3"]
}###ababac
'''

# Other tests ommitted for brevity

# Testing function
def run_tests():
    test_cases = [
        ("Accepting valid non-empty input", accepting_valid_nonempty_input),
        # ("Accepting valid empty input", accepting_valid_empty_input),
        ("Rejecting valid non-empty input", rejecting_valid_nonempty_input),
        # ("Rejecting valid empty input", rejecting_valid_empty_input),
        # ("Invalid input 1 (non-string input)", invalid_input_1),
        # ("Invalid input 2 (no delimiter)", invalid_input_2),
        # ("Invalid input 3 (missing alphabet)", invalid_input_3)
    ]
    
    for name, case in test_cases:
        print(f"Running test: {name}")
        result = adfa(case)
        print(f"Result: {'Accepted' if result else 'Rejected'}\n")


# Call the testing function
run_tests()

'''
```

### Results
![image](https://github.com/user-attachments/assets/1fd3a546-701a-416b-bf9a-e956820ccfe3)
