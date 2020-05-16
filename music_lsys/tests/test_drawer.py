#test_drawer
# Current state/ update: These tests all work fine. Time to create the Lsystem
import pytest
import itertools
from ... import utils
from ... import lsys_music_drawer
from lsys_music_drawer import Drawer


@pytest.fixture
def drawer():
    scale = utils.mode['ionian']
    octave = 4
    key_init = 'C'
    intervals = [0,2,2]
    return Drawer(scale, key_init, octave)
   
@pytest.fixture
def Data2Test():
    totest = {}
    totest['154'] = [['C4','E4','G4'], ['G4', 'B4', 'D5'], ['F4', 'A4', 'C5']]
    totest['1o1O1'] = [['C4', 'E4', 'G4'], ['C3', 'E3', 'G3'],['C4', 'E4', 'G4']]
    totest['1O1o1'] = [['C4', 'E4', 'G4'], ['C5', 'E5', 'G5'],['C4', 'E4', 'G4']]
    totest['1a1a1'] = [['C4', 'E4', 'G4'], ['C4', 'D#4', 'G4'], ['C4', 'E4', 'G4']]
    totest['1S1ss1'] = [['C4', 'E4', 'G4'], ['D4', 'F#4', 'A4'],  ['C4', 'E4', 'G4']]
    totest['1[S1ss]1'] = [['C4', 'E4', 'G4'], ['D4', 'F#4', 'A4'], ['C4', 'E4', 'G4']]
    
    #add more tests here
    return totest
    
def test_drawer(Data2Test, drawer):
    for seq, chords in Data2Test.items():
        chordseq = dotest(drawer, seq)
        try:
            assert chords == chordseq
        except:
            raise Exception('Error with seq {}, expected {}, given {}'.format(seq, chords, chordseq))
        
def dotest(drw, seq):
    chords = drw.draw(seq)
    return chords
