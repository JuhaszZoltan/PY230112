class Versenyzo:
    nev:str
    kategoria:str
    egyesulet:str
    pontszamok:list[int]


def osszpontszam_szamitas(pontszamok:list[int]) -> int:
    pontszamok.sort(reverse=True)
    osszpontszam:int = 0
    for pontszam in pontszamok[:-2]:
        osszpontszam += pontszam
    if pontszamok[-2] > 0: osszpontszam += 10
    if pontszamok[-1] > 0: osszpontszam += 10
    return osszpontszam