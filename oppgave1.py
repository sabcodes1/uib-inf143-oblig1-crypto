import sys

if len(sys.argv) < 2:
    sys.exit("Feil: Du må oppgi en 28-bit binær streng som starttilstand.")

starttilstand = sys.argv[1]

if len(starttilstand) != 28 or any(c not in "01" for c in starttilstand):
    sys.exit("Feil: Starttilstanden må være en 28-bit binær streng.")

state = int(starttilstand, 2)

output = []  
for _ in range(500): 
    output.append(str(state & 1)) 
    newbit = (state ^ (state >> 3) ^ (state >> 5) ^ (state >> 9) ^ (state >> 11) ^ (state >> 13) ^ (state >> 28)) & 1
    state = (state >> 1) | (newbit << 27)

print("".join(output))
