
class BaseLSystem:

    def __init__(self, axiom, transform_rules, alphabet):
        self.axiom = axiom
        self.current_state = axiom
        self.iteration = 0
        self.rules_dict = self.compile_rules(transform_rules, alphabet)
        self.transform_rules = transform_rules
        self.state_history = list()
        self.alphabet = alphabet
        self.update_state_history(axiom)
        
    def iterate_for(self, iterations, return_values=True):
        for _ in range(iterations):
            self._iterate()
        if return_values:
            return self.current_state
        
    def reset(self, return_history = False):
        self.current_state = self.axiom
        self.iteration = 0
        if return_history:
            return self.state_history
       
    
    def _iterate(self):
        self.iteration = self.iteration+1
        output = str()
        for i in self.current_state:
            output += self.rules_dict[i]
        self.current_state = output
        self.update_state_history(output)
    
    def update_state_history(self, new_state):
        self.state_history.append((new_state, self.iteration))
        
    def compile_rules(self, rules_dict, alphabet):
        assert (type(rules_dict) == dict)
        dic = rules_dict
        alphabet = set(alphabet) # remove duplicates
        for i in alphabet:
            try:
                dic[i]
            except KeyError:
                dic[i] = i
        return dic

    def ret_state_history(self):
        return self.state_history
    
    def ret_state(self):
        return self.current_state
        
    def rules(self):
        return self.transform_rules
    
        
