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