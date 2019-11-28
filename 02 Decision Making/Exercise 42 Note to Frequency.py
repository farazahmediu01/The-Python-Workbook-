#Note Frequency (Hz)
C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88


note = input("Enter note based only on two characters, for example C4: ")

letter = note[0]
octave = int(note[1])

if letter == "A" :
    freq = A4_FREQ
elif letter == "B" :
    freq = B4_FREQ
elif letter == "C" :
    freq = C4_FREQ
elif letter == "D" :
    freq = D4_FREQ
elif letter == "E" :
    freq = E4_FREQ
elif letter == "F" :
    freq = F4_FREQ
elif letter == "G" :
    freq = G4_FREQ

freq = freq / 2 ** (4 - octave)

print("Frequency =",freq)




