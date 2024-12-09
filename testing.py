from adfa import adfa

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
'''

accepting_valid_empty_input = '''
{
    "states": ["q0", "q1", "q2"],
    "alphabet": ["a", "b"],
    "transition": {
        "('q0', 'a')": "q1",
        "('q1', 'b')": "q2",
        "('q2', 'a')": "q1"
    },
    "start_state": "q0",
    "accept_states": ["q0"]
}###
'''

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

rejecting_valid_empty_input = '''
{
    "states": ["q0", "q1", "q2"],
    "alphabet": ["a", "b"],
    "transition": {
        "('q0', 'a')": "q1",
        "('q1', 'b')": "q2",
        "('q2', 'a')": "q1"
    },
    "start_state": "q0",
    "accept_states": ["q1", "q2"]
}###
'''

invalid_input_1 = 123  # Non-string input

invalid_input_2 = '''
{
    "states": ["q0", "q1", "q2"],
    "alphabet": ["a", "b"],
    "transition": {
        "('q0', 'a')": "q1",
        "('q1', 'b')": "q2",
        "('q2', 'a')": "q1"
    },
    "start_state": "q0",
    "accept_states": ["q0"]
}
'''  # No delimiter + input string

invalid_input_3 = '''
{
    "states": ["q0", "q1", "q2"],
    "transition": {
        "('q0', 'a')": "q1",
        "('q1', 'b')": "q2",
        "('q2', 'a')": "q1"
    },
    "start_state": "q0",
    "accept_states": ["q0", "q1", "q2"]
}###aba
'''  # Missing "alphabet" part of formal definition


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
