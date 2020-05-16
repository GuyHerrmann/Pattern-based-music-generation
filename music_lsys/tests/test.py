import pytest
import ../scales
from ../lsys_music_drawer import Drawer
import utils.utils

@pytest.fixture
def majorScale():
    majorscale = 'I,II,III,IV,V,VI,VII'
    scale = scales.Scale(majorscale)
    scale.initiate_with_tonic('C')
    return scale
    
def test_ret_maj(majorScale):
    scale = majorScale
    notes = scale.ret_notes()
    print(notes)
   
def test_chord_creation(majorScale):
    scale = majorScale
    assert scale.construct_chord([0,2,2, 3], 1, 4) == ['C4', 'E4', 'G4', 'C5']
    
def test_drawer():
    scale = utils.mode['ionian']
    octave = 4
    
