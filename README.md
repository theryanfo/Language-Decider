# DFA Acceptance Problem Solver
This Python project provides a solution for solving the Acceptance Problem for DFA (Deterministic Finite Automaton). Given a DFA and an input string, it determines whether the DFA accepts or rejects the string.

## Features
Parse a DFA: The DFA is provided as a JSON-like string representation containing key information about the DFA, such as states, alphabet, transitions, start state, and accept states.

Test input strings: The program evaluates input strings by simulating the DFA’s transitions, determining whether the string is accepted or rejected based on whether the DFA ends in an accepting state.

Error Handling: The program detects various types of input errors, such as missing or malformed DFA definitions and incorrect transition representations.
Project Structure

adfa.py: Contains the main functionality for parsing the DFA and input strings, and determining whether the string is accepted or rejected.

testing.py: Contains a suite of test cases to validate the functionality of the adfa function.

README.md: This file, which provides an overview of the project and usage instructions.

## Requirements
This project is written in Python 3. To run it, ensure that Python 3 is installed on your machine.

## Usage
### adfa.py
The adfa.py file contains the function adfa() that accepts a string containing the DFA definition and the input string. The string should be in the following format:

`<dfa_definition>###<input_string>`

### Example Input Format:
```
'''
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
}###ababa
'''
```

### Running the Tests
To run the tests and check if the DFA acceptance solver works correctly, use the testing.py script. This file contains multiple test cases that simulate various valid and invalid DFA inputs.

`python testing.py`

The test cases include:

Valid inputs: Check if the DFA correctly accepts strings.

Rejecting inputs: Check if the DFA correctly rejects strings.

Invalid input formats: Test the program’s error handling for malformed DFA definitions or invalid input.
