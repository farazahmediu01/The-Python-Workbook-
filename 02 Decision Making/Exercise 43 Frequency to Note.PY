#Note Frequency (Hz)
C4_FREQ = 261.63
D4_FREQ = 293.66
E4_FREQ = 329.63
F4_FREQ = 349.23
G4_FREQ = 392.00
A4_FREQ = 440.00
B4_FREQ = 493.88


freq = float(input("Enter frequency to determin the note of octave: "))

if freq == A4_FREQ :
    print("A4")
elif freq == B4_FREQ :
    print("B4")
elif freq == C4_FREQ :
    print("C4")
elif freq == D4_FREQ :
    print("D4")
elif freq == E4_FREQ :
    print("E4")
elif freq == F4_FREQ :
    print("F4")
elif freq == G4_FREQ :
    print("G4")
else:
    print("note not found.")
#freq = freq / 2 ** (4 - octave)

#print("Frequency =",freq)




