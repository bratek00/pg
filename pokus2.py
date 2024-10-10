# funkce vrati treti prvek ze seznamu, pokud ma mene nez 3 prvky, vrati None
#def vrat_treti(seznam):
# kolik je prvku ve promennne a co checeme abych nam program vratil
    #if len(seznam) < 3:            
     #  return None
    #else: 
     #  return seznam[2]                              
    

# funkce spocita prumer z hodnot v seznamu, pouzivejte sum(), len()
#def udelej_prumer(seznam):
   #return sum(seznam) / len(seznam)
    #print(udelej_prumer([9,8,7,6,5]))

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    jmeno = slovnik["jmeno"]        #rikame jake slovo je ve slovniku
    prijmeni = slovnik["prijmeni"]
    vek = slovnik["vek"]
     
    znamky = slovnik["znamky"]
    znamky = round(sum(znamky) / len(znamky),2)    #dva zobrazi na jake des. cisla zaokruhlim 
    return f"Jmeno: {jmeno}, Prijmeni: {prijmeni}, Vek: {vek}, Prumerna znamka: {znamky}" 
    


if __name__ == "__main__":
    #seznam = [9, 8, 5]
    #vysledek = vrat_treti(seznam)
    #print(vysledek)

  #  obalka = [9,8,7,6,50]
  #  vysledek = udelej_primer(obalka)
   # print(vysledek)
 
                   
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    
    
    vysledek = naformatuj_text(student)
    print(vysledek)
    student["vek"] # -> 21
    student["znamky"]  # -> [1,2,1,1,3,2]
    student["znamky"] [2]   #-> 1
    
    a=1
    f"Nafarmatovany retez s hodnotou {a}" # " Nafarmatovany retezec s godnotou 1"