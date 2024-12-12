def dec_to_bin(cislo):
    # Funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int)
    # Pokud cislo je retezec, prevede ho na int
    if isinstance(cislo, str):
        cislo = int(cislo)
    # Pouziva built-in funkci bin() a odstrani prefix "0b"
    return bin(cislo)[2:]

# Testovaci funkce
def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"
    assert dec_to_bin(167) == "10100111"

# Spusteni testu
try:
    test_bin_to_dec()
    print("Vsechny testy probehly uspesne.")
except AssertionError:
    print("Test selhal.")
