from synthesizer import Player, Synthesizer, Waveform
from threading import Thread


first = Thread()
second = Thread()

def first(player):
    t1 = time.time()
    while True:
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
        player.play_wave(synthesizer.generate_chord(['D5', 'A5', 'F#5'], 1))
    
def second(player):
    while True:
        synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
        player.play_wave(synthesizer.generate_chord(['D6'], 0.1))

player = Player()
player.open_stream()
first = Thread(target=first, args=[player,])
second = Thread(target=second, args=[player,])
first.start()
second.start()
while True:
    None
