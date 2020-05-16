import utils.utils as utils
import logging

class Scale:
    def __init__(self, scale):
        # first initial scanning: ensure no wrong notes
        self.numerals = [i.strip() for i in scale.split(',')]
        self.indexes = [utils.rom2num[i] for i in self.numerals]    
    
    def set_tonic(self, tonic):
        self.tonic = tonic
        self.index2tone, self.tone2numeral, self.tone2index = self._gen_tones()
        self._gen_dic4all_octaves()
    
    def change_scale(self,scale):
        self.numerals = [i.strip() for i in scale.split(',')]
        self.indexes = [utils.rom2num[i] for i in self.numerals]

    
    def _gen_dic4all_octaves(self):
        values = [tone+str(level) for level in range(2,6) for tone in self.index2tone.values()]
        indexes = [i+1 for i in range(len(values))]
        self.odict_val2index = dict(zip(values, indexes))
        self.odict_index2val = dict(zip(indexes, values))
    
    def _gen_tones(self):
        _tonic_indx = utils.notes2num[self.tonic]        
        indexes = [(_tonic_indx + i) for i in self.indexes]
        return self._gen_dict(indexes)
           
    def _gen_dict(self, indxlist):
        notes = [utils.num2notes[(i%12)] for i in indxlist]
        comm_index = [i for i in range(1,8)]
        #returns if raised an occtave
        return (dict(zip(comm_index, notes)), dict(zip(notes, self.numerals)), dict(zip(notes, comm_index)))
    
    def ret_notes(self):
        return list(self.index2tone.values())
        
    def construct_chord(self,intervals, root_index, octave):
        note = self.index2tone[int(root_index)]+str(octave)
        _cum = self.odict_val2index[note]
        out = list()
        for i in intervals:
            _cum += i
            out.append(self.odict_index2val[_cum])
        return (out, root_index)
        
    def interval(self, num):
        return self.index2tone[num]

        
  

