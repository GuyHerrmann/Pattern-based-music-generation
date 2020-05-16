#ok, waitasec, How do the root indexes work?
# [eithnote, quaternote, halfnote, fullnote] [sustain, half, q]
# representation: 8n, 4n, 2n,1n then: s/h/r ->for timeing
# Yay this works.. now for adding rests @YEay;.
import numpy as np

chorddist = {}
chorddist[1] = [0.25, 0.25, 0.25, 0.25]
chorddist[2] = [0.25, 0.25, 0.25, 0.25]
chorddist[3] = [0.25, 0.25, 0.25, 0.25]
chorddist[4] = [0.25, 0.25, 0.25, 0.25]
chorddist[5] = [0.25, 0.25, 0.25, 0.25]
chorddist[6] = [0.25, 0.25, 0.25, 0.25]
chorddist[7] = [0.25, 0.25, 0.25, 0.25]
chorddist[8] = [0.125] # This represent a rest :)


durations = [0.125, 0.25, 0.5, 1]



def calculateTimings(chords):
    timingList = list()
    for _, index in chords:
        dist = chorddist[int(index)]
        duration = np.random.choice(durations, 1, p=dist)[0]
        timingList.append(duration)
    return timingList

    
