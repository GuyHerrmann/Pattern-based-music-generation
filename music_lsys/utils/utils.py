dictionary = ['I', 'bII', 'II', 'bIII', 'III', 'IV', 'bV', 'V', 'bVI', 'VI', 'bVII', 'VII']
alphabet = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
num2notes = {}
notes2num = {}
rom2num = {}
num2rom = {}
for i, sign in enumerate(dictionary):
    rom2num[sign] = i
    num2rom[i] = sign

for i, letter in enumerate(alphabet):
    num2notes[i] = letter
    notes2num[letter] = i
    
relative_mode = {
    1: 'ionian',
    2: 'dorian',
    3: 'phrygian',
    4: 'lydian',
    5: 'mixolydian',
    6: 'aeolian',
    7: 'locrian'
    }    
mode = {
    'major': 'I,II,III,IV,V,VI,VII',
    'ionian': 'I,II,III,IV,V,VI,VII',
    'dorian': 'I,II,bIII,IV,V,VI,bVII',
    'phrygian': 'I,bII,bIII,IV,V,bVI,bVII',
    'lydian': 'I,II,III,bV,V,VI,VII',
    'mixolydian': 'I,II,III,IV,V,VI,bVII',
    'aeolian': 'I,II,bIII,IV,V,VI,bVII',
    'locrian': 'I,bII,bIII,IV,bV,bVI,bVII'
    }
    

