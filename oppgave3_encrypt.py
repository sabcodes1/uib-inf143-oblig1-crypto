



import sys

plaintext_file = sys.argv[1]
key_file = sys.argv[2]
cipher_file = sys.argv[3]


with open(plaintext_file, "r") as bro: 
    text = bro.read().strip() 
    if len(text) < 16: 
        print("bit-strengen er for kort.")
        exit()  # Avslutter programmet hvis strengen er for kort


with open(key_file, "r") as dude: 
    nøkkelfrafil = dude.read().strip() 
    if len(nøkkelfrafil) < 32: 
        print("bit-strengen er for kort.")
        exit()  # Avslutter programmet hvis strengen er for kort


    hel_nøkkel = nøkkelfrafil
    nøkkel = [hel_nøkkel[:8], hel_nøkkel[8:16], hel_nøkkel[16:24], hel_nøkkel[24:32]]
    liste = [text[:8], text[8:16]]  
    Left = liste[0]
    Right = liste[1]
    print("Start Left:", Left, "Start Right:", Right)

def encrypt(Left, Right): 

    for key in range(4):  # 4 runder som spesifisert i oppgaven
        # Beregn F(R, nøkkel) med Right (den nåværende høyresiden)
        left = list(Left)
        s1 = list(Left)  
        s5 = list(Left)
        s2 = list(Left)
        length = len(s1)
        # H er en kopi av den opprinnelige Right (før rotasjon)
        H = list(Right)  

        new_s1 = s1[:]  # Kopierer listen
        new_s5 = s5[:]
        new_s2 = s2[:]

        # Utfør venstre syklisk rotasjon på Right:
        for i in range(length):
            new_index = (i - 1) % length  # Rotasjon med 1
            new_s1[new_index] = s1[i]

        for i in range(length): 
            new_index = (i - 5) % length  # Rotasjon med 5
            new_s5[new_index] = s5[i]

        for i in range(length):
            new_index = (i - 2) % length  # Rotasjon med 2
            new_s2[new_index] = s2[i]

        # Konverter de roterte listene til heltall
        right_Shift1_int = int("".join(new_s1), 2)
        right_Shift5_int = int("".join(new_s5), 2)
        right_Shift2_int = int("".join(new_s2), 2)
        left_correct = int("".join(left), 2)
        right_int = int("".join(H), 2)  # Original Right som tall

        left_int = int(Left, 2)  # Venstre del som tall
        nøkkel_int = int(nøkkel[key], 2)

        print(f"Round {key+1}")
        print(f"Right after shift (1): {format(right_Shift1_int, '08b')}")
        print(f"Right after shift (5): {format(right_Shift5_int, '08b')}")
        print(f"Right after shift (2): {format(right_Shift2_int, '08b')}")
        print(f"Original Right value: {format(right_int, '08b')}")
        print(f"Key value: {format(nøkkel_int, '08b')}")

        # Beregn F(R, nøkkel):
        # F(R, K) = (((S1(R) AND S5(R)) XOR R) XOR S2(R)) XOR nøkkel
        and_result = right_Shift1_int & right_Shift5_int
        print("Bitvis AND-resultat:", format(and_result, '08b'))

        first_xor_value = and_result ^ right_int
        print("Bitvis XOR-resultat:", format(first_xor_value, '08b'))

        second_xor_value = first_xor_value ^ right_Shift2_int
        print("Bitvis XOR-resultat (andre):", format(second_xor_value, '08b'))

        third_xor_value = second_xor_value ^ nøkkel_int
        print("Bitvis XOR2-resultat (F):", format(third_xor_value, '08b'))

        # Oppdatering av blokkene:
        # Ifølge Feistel-strukturen:
        # L_{i+1} = R (den gamle høyresiden)
        # R_{i+1} = F(R, nøkkel)  (uten at den gamle venstresiden XOR'es)
        new_L = format(third_xor_value, '08b')
        new_R = format(left_correct,  '08b')
        
        print(f"Updated Left: {new_L}, Updated Right: {new_R}\n")

        # Oppdater for neste runde
        Left = new_L
        Right = new_R
    
    print(f"Updated Left: {new_R}, Updated Right: {new_L}\n")

    return Right + Left 

final= encrypt(Left, Right)

with open(cipher_file, "w") as kis: 
    kis.write(final)