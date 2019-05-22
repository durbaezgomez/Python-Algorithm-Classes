from heapq import heappush, heappop, heapify
from collections import defaultdict  # domyslny slownik przechowujacy inty


def zakoduj(znakCzestosc):
    # KOPIEC [czestosc, [znak, aktualny_kod]]
    heap = [[czestosc, [znak, ""]] for znak, czestosc in znakCzestosc.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def otworzPlik():
    print("Podaj nazwe pliku do otworzenia: ")
    filename = raw_input() +".txt"
    # filename = "test.txt"
    with open(filename, "rb") as binary_file:
        data = binary_file.read()
    return data


def zliczCzestosc(data):
    znakCzestosc = defaultdict(int)
    for b in data:
        znakCzestosc[b] += 1
    return znakCzestosc


def wypiszWynik(huff):
    s1 = "Znak   Czestotliwosc Kod Huffmana"
    print(s1)
    for p in huff:
        s2 = str(p[0]) + "      " + str(znakCzestosc[p[0]]) + "             " + str(p[1])
        print(s2)

def porownajDlugosc(huff):
    sumaCzestotliwosci = 0
    iloczynCzestotliwosci = 0
    for p in huff:
        sumaCzestotliwosci += znakCzestosc[p[0]]
        iloczynCzestotliwosci += (znakCzestosc[p[0]] * len(p[1]))

    kompresja = float(iloczynCzestotliwosci)/float(sumaCzestotliwosci*8)

    print(sumaCzestotliwosci*8, iloczynCzestotliwosci)
    print ("Wykonano kompresje w stosunku procentowym: " + str(kompresja) +"%")


data = otworzPlik()
znakCzestosc = zliczCzestosc(data)
huff = zakoduj(znakCzestosc)
wypiszWynik(huff)
porownajDlugosc(huff)





