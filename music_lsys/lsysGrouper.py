import LSys
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')  
logger.debug('Hello')   

class LsystemGrouper:
    def __init__(self, lsystems):
        #takes a list of lsystems
        self._compatible(lsystems)
        logger.info('Is Compattible')
        self.lsystems = lsystems
        
    def _compatible(self, lsystems):
        _rules = [lsys.rules() for lsys in lsystems]
        #logger.debug('Type is {}'.format(type(_rules[0])))
        _keylist = np.array([list(rule.keys()) for rule in _rules])
        _keys = _keylist[0]
        self._check_equivkeylists(_keylist) #checs to see if keylists are the same
        self._checkequivtransformations(_rules, _keys)

    def iterate_for(self, numiter):
        out = list()
        for lsys in self.lsystems:
            out.append(lsys.iterate_for(numiter))
        return out
    
    def return_state(self):
        _out = [lsys.ret_state for lsys in lsystems]
        return _out
    

    def _check_equivkeylists(self, keylist):
        if not np.all(keylist[0] == keylist):
            raise Exception('Different transformation rules used in the LSystems'+
                'all transforms should use the same symbol')
                
    def _checkequivtransformations(self, rules, _keys):
        translist = list()
        for key in _keys:
            translist.append([rule[key] for rule in rules])
            
        for rulelist in translist:
            _lenlist = np.array([len(i) for i in rulelist])
            if (np.all(_lenlist[0] != _lenlist)):
                raise Exception('length of transformatins is not the same for given rule')
            
            for key_ in _keys:
                keypos = list()
                for rule in rulelist:
                    _tmprule = np.array(list(rule))
                    #logging.debug('rule : {} where is key = {}'.format(_tmprule, key_))
                    keypos.append(np.where(_tmprule == key_))
                keypos = np.array(keypos)
                #if not (np.all(keypos[0] == keypos)):
                 #   raise Exception('transformation rules do not have transformatin symbols at same place')
                
                    
                        
           
