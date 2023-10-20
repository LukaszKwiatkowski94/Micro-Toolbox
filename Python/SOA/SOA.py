# SZYFR ODWRÓCONEGO ALFABETU (SOA)
import os
array = ['A','a','Ą','ą','B','b','C','c','Ć','ć','D','d','E','e',
         'Ę','ę','F','f','G','g','H','h','I','i','J','j','K','k',
         'L','l','Ł','ł','M','m','N','n','Ń','ń','O','o','Ó','ó',
         'P','p','Q','q','R','r','S','s','Ś','ś','T','t','U','u',
         'V','v','W','w','X','x','Y','y','Z','z','Ź','ź','Ż','ż']
filepath = "dane.txt"
f = open(filepath,"r",encoding="utf-8")
m = f.read()
tmp = ''
for x in m:
    try:
        y = array.index(x)
        x = array[-y]
    except:
        continue
    finally:
        tmp+=x
f.close()
f = open(filepath,"w",encoding="utf-8")
f.write(tmp)
f.close()

'''
[PL]
Ten program jest prostym przykładem implementacji szyfru odwróconego alfabetu (SOA) w języku Python.
Szyfr ten polega na zamianie każdej litery w tekście na jej odpowiednika z odwrotnego alfabetu polskiego.
Program otwiera plik tekstowy "dane.txt" i odczytuje jego zawartość. Następnie, dla każdej litery w tekście,
program znajduje jej odpowiednik w odwrotnym alfabecie, korzystając z wcześniej zdefiniowanej tablicy liter.
Litery, które nie znajdują się w tej tablicy, takie jak spacje lub znaki interpunkcyjne, są pomijane.
Zaszyfrowane litery są gromadzone w zmiennej "tmp". Po przetworzeniu całego tekstu,
zaszyfrowany tekst jest zapisywany z powrotem do pliku "dane.txt", zastępując oryginalną zawartość.
W rezultacie, plik "dane.txt" zawiera zaszyfrowany tekst, w którym litery zostały zamienione na ich odpowiedniki
z odwrotnego alfabetu polskiego.

[EN]
This program is a simple example of implementing the Reverse Alphabet Cipher (RAC) in Python.
This cipher involves replacing each letter in the text with its counterpart from the reverse Polish alphabet.
The program opens the text file "dane.txt" and reads its content. Subsequently, for each letter in the text,
the program finds its counterpart in the reverse alphabet, using a previously defined array of letters.
Letters that are not found in this array, such as spaces or punctuation marks, are skipped.
Encrypted letters are stored in the "tmp" variable. After processing the entire text,
the encrypted text is written back to the "dane.txt" file, replacing the original content.
As a result, the "dane.txt" file contains encrypted text in which the letters have been replaced with their counterparts
from the reverse Polish alphabet.
'''
