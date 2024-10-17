def cislo_text(cislo):
        cislo = int(cislo)
    
jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
nepravidelne_desitky = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    # Обработка чисел
    if cislo < 0 or cislo > 100:
        return "Číslo mimo rozsah"  # Проверка на диапазон
    elif cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        return nepravidelne_desitky[cislo - 10]  # Исправление индекса
    elif cislo < 100:
        des = cislo // 10
        jedn = cislo % 10
        if jedn == 0:
            return desitky[des]
        else:
            return desitky[des] + " " + jednotky[jedn]
    elif cislo == 100:
        return "sto"
          
cislo = int(input("Zadejte cislo: "))  
print(cislo_text(cislo))


