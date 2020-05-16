from synthesizer import Player, Synthesizer, Waveform
import time
from threading import Thread
import numpy as np


import Tempo.tempo as tempo
from LSys import BaseLSystem
from utils.config import Config
from lsys_music_drawer import Drawer
from lsysGrouper import LsystemGrouper

import utils.utils as utils

RATE = 1
dur_dict = {1:0.125, 2:0.25, 3:0.5,  4:0.75, 5: 1}

def simalt_notesplay(player, chord, time, synthesizer):
    player.play_wave(synthesizer.generate_chord(chord,time))

def play_progression(chords, timings):
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=True,
                    osc2_waveform=Waveform.sawtooth, osc2_freq_transpose=2.0)
    #play all notes :)
    for (i, _),duration  in zip(chords, timings):
        if i == 'rest':
            time.sleep(RATE/8)
            print('rest')
        else:
            print('chord : {} timing : {}'.format(i, duration*RATE))
            simalt_notesplay(player, i, duration, synthesizer)
   
def play_beat(t):
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
    for i in range(int(t/RATE)):
        player.play_wave(synthesizer.generate_chord(['A3'], 0.1))
        time.sleep(float(RATE-0.1))
        
        
def prepare_prog(prog_seq):
    prog_seq = np.array(list(prog_seq))
    index2del = np.where(prog_seq == '.')
    prog = np.delete(prog_seq, index2del)
    index2del = np.where(prog == 'A')
    prog = np.delete(prog, index2del)
    index2del = np.where(prog == '[')
    prog = np.delete(prog, index2del)
    index2del = np.where(prog == ']')
    prog = np.delete(prog, index2del)
    mapped = list(map(lambda x: dur_dict[int(x)], prog))
    return mapped



if __name__ == '__main__':

#declaration of rules for duration: 1 = 1/8, 2 = 1/4, 3 = 2/4, 4 = 3/4, 5 = 4/4, . does nothing (filler)
    duration = {'axiom' : '13A44', 'transrules' : {'A': '32[1.22A.5.3]'}}
    duration_lsys = BaseLSystem(duration['axiom'], duration['transrules'], Config['alphabet'])

    progression = {'axiom' : '72A12', 'transrules': {'A': '15[1^2A3^52]'}}
    progression_lsys = BaseLSystem(progression['axiom'], progression['transrules'], Config['alphabet'])
    #sequence = lsys.iterate_for(5, True)
    
    lsysgroups = [progression_lsys, duration_lsys]
    
    grouper = LsystemGrouper(lsysgroups)
    prog_seq, dur_seq = grouper.iterate_for(4)
    
    print('prog seq : {}, dur_seq : {}'.format(prog_seq, dur_seq))
    
    drawer = Drawer(scale=utils.mode['ionian'], key_init='C', octave=4)
    chords = drawer.draw(prog_seq)
    
    progression_timings = prepare_prog(dur_seq)
    
  #  timings = tempo.calculateTimings(chords)
    total_time = sum(progression_timings)
    assert (len(chords) == len(progression_timings))
    

    
    progression_thread = Thread(target=play_progression, args=(chords, progression_timings,))
    beat_thread = Thread(target=play_beat, args=(total_time,))
    
    progression_thread.start()
    #beat_thread.start()
    progression_thread.join()
    #beat_thread.join()


    # initiate threads
