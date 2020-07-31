import numpy as np

class MusicalNotes():
    def __init__(self):
        self.freq_fundamental = 16.351597
    
    def get_musical_notes(self,freqs):
        notas = (12 * np.log2((freqs)/self.freq_fundamental))
        notas = np.int64(np.round(notas))
        notas = np.mod(notas,12)

        return notas