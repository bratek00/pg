def bin_to_dec(binarni_cislo):
    """
    Funkce spocita hodnotu predavaneho binarniho cisla (může být str i int).
    """
    # Pokud cislo je int, nejdrive ho prevest na str
    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)
    
    # Konverze z binarniho na desitkove
    return int(binarni_cislo, 2)


def test_funkce():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    assert bin_to_dec("10011101") == 167
    assert bin_to_dec(10011101) == 167  # přímé porovnání čísla v int formátu
    print("Všechny testy prošly!")

# Spusteni testu
test_funkce()
