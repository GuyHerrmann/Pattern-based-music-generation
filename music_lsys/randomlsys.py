from LSys import BaseLSystem
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class randomLsys(BaseLSystem):
        # tranformation rules : dict, 'KEy' : ([listofrules], [list of probabilities])d
    def __init__(self, axiom, transform_rules, alphabet):
        #super().__init__(self, axiom, transform_rules, alphabet)
        self.randomized_rules = list(transform_rules.keys())
        super().__init__(axiom, transform_rules, alphabet)


    
    def _iterate(self):
        self.iteration = self.iteration+1
        output = str()
        for i in self.current_state:
            if i in self.randomized_rules:
                output += np.random.choice(self.rules_dict[i][0],
                                        p = self.rules_dict[i][1])
            else:
                output +=  self.rules_dict[i]
        logger.debug('iteration level: {}, output: {}'.format(self.iteration, output))   
        self.current_state = output
        self.update_state_history(output)
