# INF143A – Oblig 1 (Applied Cryptography, UiB)

Dette repoet inneholder løsningene til obligatorisk oppgave 1 i **INF143A – Anvendt kryptografi**.

## Innhold
- **Oppgave 1 (LFSR):** LFSR med periode `2^28 - 1`, skriver ut første 500 bits fra gitt starttilstand.
- **Oppgave 2 (GF(2^6) truth table):** Genererer oppslagstabell for funksjonen `F(x,k) = x^3 + (x+k)^3 + k` i `GF(2^6)` basert på gitt primitivt polynom.
- **Oppgave 3 (Block cipher):** Implementasjon av et 4-runders Feistel/SIMON-inspirert blokkchiffer (16-bit blokk, 32-bit nøkkel) med både kryptering og dekryptering.
- **Oppgave 4 (MITM 2-DES):** Meet-in-the-Middle-angrep for å finne ukjente nøkkelbiter gitt kjent klartekst/kryptotekst-par.

## Kjøring
Se filnavn og argumenter i oppgaveteksten (PDF i `report/`).

## Teknologi / konsepter
- Python
- LFSR, finite fields (GF(2^n))
- Feistel-nettverk / lightweight blokkchiffer
- Meet-in-the-Middle (2-DES)
