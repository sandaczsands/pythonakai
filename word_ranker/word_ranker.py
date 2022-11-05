# coding=utf-8

from operator import itemgetter

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        word= word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

holder=""
maks=""
N= 3

for i in sentences:
    i=i.strip()
    holder=holder+" "+i

tab=word_count(holder)


for i in sorted(tab,key=tab.get, reverse = True)[:N]:
    print(i,tab[i])
