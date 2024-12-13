def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    pozice = figurka["pozice"]
        
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    
    if cilova_pozice in obsazene_pozice:
        return False

    
    if typ == "pěšec":
        
        if pozice[1] == cilova_pozice[1]:  
            if cilova_pozice[0] == pozice[0] + 1 and (pozice[0] + 1, pozice[1]) not in obsazene_pozice:
                return True  
            if pozice[0] == 2 and cilova_pozice[0] == pozice[0] + 2:
                return (pozice[0] + 1, pozice[1]) not in obsazene_pozice  

    elif typ == "jezdec":
        
        radkovy_rozdil = abs(pozice[0] - cilova_pozice[0])
        sloupcovy_rozdil = abs(pozice[1] - cilova_pozice[1])
        return (radkovy_rozdil, sloupcovy_rozdil) in [(2, 1), (1, 2)]

    elif typ == "věž":
        
        if pozice[0] == cilova_pozice[0]:  
            for y in range(min(pozice[1], cilova_pozice[1]) + 1, max(pozice[1], cilova_pozice[1])):
                if (pozice[0], y) in obsazene_pozice:
                    return False
            return True
        elif pozice[1] == cilova_pozice[1]:  
            for x in range(min(pozice[0], cilova_pozice[0]) + 1, max(pozice[0], cilova_pozice[0])):
                if (x, pozice[1]) in obsazene_pozice:
                    return False
            return True

    elif typ == "střelec":
        
        if abs(pozice[0] - cilova_pozice[0]) == abs(pozice[1] - cilova_pozice[1]):
            dx = 1 if cilova_pozice[0] > pozice[0] else -1
            dy = 1 if cilova_pozice[1] > pozice[1] else -1
            for i in range(1, abs(pozice[0] - cilova_pozice[0])):
                if (pozice[0] + i * dx, pozice[1] + i * dy) in obsazene_pozice:
                    return False
            return True

    elif typ == "dáma":
        
        if pozice[0] == cilova_pozice[0] or pozice[1] == cilova_pozice[1]:
            return je_tah_mozny({"typ": "věž", "pozice": pozice}, cilova_pozice, obsazene_pozice)
        elif abs(pozice[0] - cilova_pozice[0]) == abs(pozice[1] - cilova_pozice[1]):
            return je_tah_mozny({"typ": "střelec", "pozice": pozice}, cilova_pozice, obsazene_pozice)

    elif typ == "král":
        
        return max(abs(pozice[0] - cilova_pozice[0]), abs(pozice[1] - cilova_pozice[1])) == 1

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
