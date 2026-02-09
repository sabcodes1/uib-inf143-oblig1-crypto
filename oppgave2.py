import sys
import galois

# Les argumenter
polynom_input = sys.argv[1]  # Input polynom i binær form (f.eks. "110000" for x^6 + x + 1)
resultatfil = sys.argv[2]    # Filnavn for output

# Definer kroppen GF(2^6) med riktig irreduktibelt polynom
GF = galois.GF(2**6, irreducible_poly="x^6 + x + 1")

# Funksjonen F(x, k) som definert i oppgaven
def F(x, k):
    x, k = GF(x), GF(k)
    return x**3 + (x + k)**3 + k  # Riktig formel!

# Beregn og skriv resultater i riktig format
with open(resultatfil, 'w') as f:
    for x in range(64):  # 6-bit -> 2^6 = 64 mulige verdier
        for k in range(64):
            output = int(F(x, k))  # Konverter feltverdien til en integer
            f.write(f"{format(x, '06b')},{format(k, '06b')} -> {format(output, '06b')}\n")
