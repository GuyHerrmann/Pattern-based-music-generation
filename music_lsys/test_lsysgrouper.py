import numpy as np
from utils.config import Config
import lsysGrouper
from lsysGrouper import LsystemGrouper  

import pytest
from LSys import BaseLSystem

#@pytest.fixture
def lsys_grouping():
    axiom1 = '251A512'
    axiom2 = '323A343'
    axiom3 = '222A111'
    transrules1 = {'A': '[^251A]111[ss14A]'}
    transrules2 = {'A': '[^422A]111[ss17A]'}
    transrules3 = {'A': '[^321A]111[ss15A]'}
    lsys1 = BaseLSystem(axiom1, transrules1, Config['alphabet'])
    lsys2 = BaseLSystem(axiom2, transrules2, Config['alphabet'])
    lsys3 = BaseLSystem(axiom3, transrules3, Config['alphabet'])
    return [lsys1, lsys2, lsys3]

def test_initgrouper(lsys_grouping):
    grouper = LsystemGrouper(lsys_grouping)
    lsys1, lsys2, lsys3 = grouper.iterate_for(3)
    assert (len(lsys1) == len(lsys2) == len(lsys3))
    return lsys1, lsys2, lsys3
    
if __name__ == '__main__':
    lsyses = lsys_grouping()
    iterated = test_initgrouper(lsyses)
    print(iterated)
    
