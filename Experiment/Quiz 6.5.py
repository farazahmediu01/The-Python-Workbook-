text  = "X-DSPAM-Confidence:    0.8475"
itext = text.find(" ")
subtext = text[19:]#.lstrip()
ftext = float(subtext)
chop = subtext.lstrip()

print(itext)
print(subtext)
print(chop)
print(subtext)
print(ftext)