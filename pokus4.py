# 1 ukol nasli jaccardovu vydalenost
# def jaccardova_vzdalenost_mnozin(mnozina1, mnozina2):
#     set1 = set(mnozina1)
#     set2 = set(mnozina2)
    
#     prunik = set1.intersection(set2)
#     sjednoceni =  set1.union(set2)
    
#     jaccard_index= len(prunik) / len(sjednoceni)  
    
#     jaccard_distance = 1 - jaccard_index
#     return jaccard_distance

# if __name__ == "__main__":
#     serp1 = ["https://www.seznam.cz", "https://www.google.com", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
#     serp2 = ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
#     serp3 = ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]

#     print(jaccardova_vzdalenost_mnozin(serp1, serp2))
#     print(jaccardova_vzdalenost_mnozin(serp2, serp3))
#     print(jaccardova_vzdalenost_mnozin(serp1, serp3))



def levensteinova_vzdalenost(dotaz1, dotaz2):

    length = max(len(dotaz1),len(dotaz2))
    i=0
    levenstein = 0
    while i < length:
        if  i < len(dotaz1) and i < len(dotaz2):
            if dotaz1[i] != dotaz2[i]:
                levenstein += 1
            else: 
                levenstein += 1
            i += 1
    return levenstein

if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))