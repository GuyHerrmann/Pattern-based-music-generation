import scales
import re
import utils.utils as utils
# THe main function of this class is to 
class Drawer:
    def __init__(self, scale, key_init, octave):
        self.chords = list()
        self.cursor = {'key': key_init, 'scale' : scale, 'octave' : octave}
        self.scale = scales.Scale(scale)
        self._set_scale_key()
        self.store = list()
        
    def draw(self, lsys, ret=True):
        self.chords = list()
        for i in lsys:
            if re.match('[0-7]', i):
                chord = self.scale.construct_chord([0,2,2], i, self.cursor['octave'])
                self.chords.append(chord)
            elif i == 'r':
                chord = ('rest', '8')
                self.chords.append(chord)
            elif i == '[':
                self.store.insert(0, self.cursor)
            elif i == ']':
                self.cursor = self.store.pop()
            elif i =='a':
            #Change: major -> minor
                if self.cursor['scale'] == utils.mode['ionian']:
                    self.cursor['scale'] = utils.mode['aeolian']
                elif self.cursor['scale'] == utils.mode['aeolian']:
                    self.cursor['scale'] = utils.mode['ionian']
                self._set_scale()
            elif i == 'O':
                self.cursor['octave'] += 1
            elif i =='o':
                self.cursor['octave'] -= 1
            elif i == '^':
                self.cursor['key'] = self.scale.interval(5)
                self._set_key()
            elif i == 'S':
                self.cursor['key'] = self.scale.interval(2) # 1 is the tonic
                self._set_key()
            elif i == 's':
                self.cursor['key'] = self.scale.interval(7)
                self._set_key()
        if ret:
            return self.chords
              
    def _set_scale_key(self):
        self.scale.change_scale(self.cursor['scale'])
        self.scale.set_tonic(self.cursor['key'])
        
    def _set_key(self):
        self.scale.set_tonic(self.cursor['key'])
    
    def _set_scale(self):
        self.scale.change_scale(self.cursor['scale'])
        self.scale.set_tonic(self.cursor['key'])
    
    def cursor(self):
        return self.cursor



                
