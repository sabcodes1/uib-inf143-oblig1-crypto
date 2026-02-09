from Crypto.Cipher import DES
from Crypto.Util.number import long_to_bytes

Key1 = "1" * 45
Key2 = "1" * 45 

klartext_bits = "1111100001010101111011010010011101100110010111000110001101010000"
cipher_bits = "1101111101011100101000000011011110111101101000000010010010110001"

klartext_8bytes = int(klartext_bits, 2).to_bytes(8, "big")
kryptotext_8bytes = int(cipher_bits, 2).to_bytes(8, "big")

intermediate_dict = {}

# Fase 1: Krypter klartekst med alle mulige 19-bit variasjoner av K1
for x in range(2**19):  
    combine_key1 = Key1 + format(x, '019b')

    key_bytes = long_to_bytes(int(combine_key1, 2), 8)  # Konverter direkte til bytes
    cipher = DES.new(key_bytes, DES.MODE_ECB)
    
    M = cipher.encrypt(klartext_8bytes)
    intermediate_dict[M] = key_bytes  # Lagre mellomverdi med K1

found = False

# Fase 2: Dechiffrer kryptoteksten med alle mulige 19-bit variasjoner av K2
for x in range(2**19):  
    combine_key2 = Key2 + format(x, '019b')

    key_bytes = long_to_bytes(int(combine_key2, 2), 8)  # Konverter direkte til bytes
    cipher = DES.new(key_bytes, DES.MODE_ECB)

    M_prime = cipher.decrypt(kryptotext_8bytes)  

    if M_prime in intermediate_dict:  
        K1_found = intermediate_dict[M_prime]  
        K2_found = key_bytes  

        cipher1 = DES.new(K1_found, DES.MODE_ECB)
        M_test = cipher1.encrypt(klartext_8bytes)

        cipher2 = DES.new(K2_found, DES.MODE_ECB)
        Y_test = cipher2.encrypt(M_test)


        if Y_test == kryptotext_8bytes:         
            nøkkel = f"{format(int.from_bytes(K1_found, 'big'), '064b')[-19:]}{format(int.from_bytes(K2_found, 'big'), '064b')[-19:]}"
            print(nøkkel)
        else:
            print("FEIL! Krypteringen med de funne nøklene gir IKKE riktig Y!")

        found = True
        
if not found:
    print("\n!funnet ")

