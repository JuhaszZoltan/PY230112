from module import Versenyzo, osszpontszam_szamitas

versenyzok:list[Versenyzo] = []

for sor in open('fob2016.txt'):
    drbk:list[str] = sor.strip().split(';')
    v:Versenyzo = Versenyzo()
    v.nev = drbk[0]
    v.kategoria = drbk[1]
    v.egyesulet = drbk[2]
    v.pontszamok = []
    for pontszam in drbk[3:]:
        v.pontszamok.append(int(pontszam))
    versenyzok.append(v)
print(f'3. feladat: Versenyzők száma: {len(versenyzok)}')

nok_szama:int = 0
for versenyzo in versenyzok:
    if versenyzo.kategoria == 'Noi':
        nok_szama += 1
arany:float = nok_szama / len(versenyzok) * 100
print(f'4. feladat: Női versenyzők aránya: {round(arany, 2)}%')

maxi:int = -1
for i in range(1, len(versenyzok)):
    if maxi == -1 and versenyzok[i].kategoria == 'Noi':
        maxi = i
    elif versenyzok[i].kategoria == 'Noi':
        if osszpontszam_szamitas(versenyzok[i].pontszamok) > osszpontszam_szamitas(versenyzok[maxi].pontszamok):
            maxi = i

print(f'6. feladat: A bajnok női versenyző')
print(f'\tNév: {versenyzok[maxi].nev}')
print(f'\tEgyesület: {versenyzok[maxi].egyesulet}')
print(f'\tÖsszpontszám: {osszpontszam_szamitas(versenyzok[maxi].pontszamok)}')

f = open('osszpontFF.txt', mode='w')
for versenyzo in versenyzok:
    if versenyzo.kategoria != 'Noi':
        f.write(f'{versenyzo.nev};{osszpontszam_szamitas(versenyzo.pontszamok)}\n')

egyesuletek:dict[str, int] = { }

for versenyzo in versenyzok:
    if versenyzo.egyesulet not in egyesuletek.keys():
        egyesuletek[versenyzo.egyesulet] = 1
    else: egyesuletek[versenyzo.egyesulet] += 1

print('8. feladat: Egyesület statisztika')
for nev, letszam in egyesuletek.items():
    if nev != 'n.a.' and letszam > 2:
        print(f'\t{nev} - {letszam} fő')