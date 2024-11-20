def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    start_pozice = figurka["pozice"]
    typ_figury = figurka["typ"]

    def je_v_rozsahu(pozice):
        return 1 <= pozice[0] <= 8 and 1 <= pozice[1] <= 8
    
    if not je_v_rozsahu(cilova_pozice):
        return False
    
    if typ_figury != 'pěšec' and cilova_pozice in obsazene_pozice:
        return False

    x1, y1 = start_pozice
    x2, y2 = cilova_pozice

    if typ_figury == 'pěšec':
        if y2 == y1 + 1 and x1 == x2 and cilova_pozice not in obsazene_pozice:
            return True  
        if y1 == 2 and y2 == y1 + 2 and x1 == x2 and (x2, y1 + 1) not in obsazene_pozice and cilova_pozice not in obsazene_pozice:
            return True  
        if abs(x2 - x1) == 1 and y2 == y1 + 1 and cilova_pozice in obsazene_pozice:
            return True  
        return False

    elif typ_figury == 'jezdec':
        return (abs(x2 - x1), abs(y2 - y1)) in [(1, 2), (2, 1)]

    elif typ_figury == 'věž':
        if x1 == x2 or y1 == y2:
            return je_cesta_volna(start_pozice, cilova_pozice, obsazene_pozice)
        return False

    elif typ_figury == 'střelec':
        if abs(x2 - x1) == abs(y2 - y1):
            return je_cesta_volna(start_pozice, cilova_pozice, obsazene_pozice)
        return False

    elif typ_figury == 'dáma':
        if x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
            return je_cesta_volna(start_pozice, cilova_pozice, obsazene_pozice)
        return False

    elif typ_figury == 'král':
        return max(abs(x2 - x1), abs(y2 - y1)) == 1
    
    return False

def je_cesta_volna(start, cil, obsazene):
    x1, y1 = start
    x2, y2 = cil
    if x1 == x2:
        for y in range(min(y1, y2) + 1, max(y1, y2)):
            if (x1, y) in obsazene:
                return False
    elif y1 == y2:
        for x in range(min(x1, x2) + 1, max(x1, x2)):
            if (x, y1) in obsazene:
                return False
    elif abs(x2 - x1) == abs(y2 - y1):
        x_step = 1 if x2 > x1 else -1
        y_step = 1 if y2 > y1 else -1
        for i in range(1, abs(x2 - x1)):
            if (x1 + i * x_step, y1 + i * y_step) in obsazene:
                return False
    return True


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (3, 3), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False
