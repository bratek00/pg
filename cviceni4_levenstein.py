def levensteinova_vzdalenost(dotaz1, dotaz2):
    levenstein = 0
    length = min(len(dotaz1), len(dotaz2))
    for i in range(length):
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))
    return levenstein


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))