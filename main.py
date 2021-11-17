# -----------------------------------Cwiczenie1----------------------------------
# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu,
# zapisz go w zmiennej.

# datafile = open("cwiczenie1.txt")
# tresc_pliku = datafile.read()
# print(datafile)
#
# # Inaczej
# def file_read(fname):
#     with open(fname, "r") as myfile:
#         data = myfile.read()
#         print(data)
#
#
# file_read('08 Python (podstawy) - pliki i modu?y.ipynb')


# -----------------------------------Cwiczenie2----------------------------------
# Napisz program w Pythonie, który odczyta plik tekstowy wiersz po wierszu,
# zapisz go w tablicy content_array.
# content_array to lista zawieraj?ca przeczytane wiersze.

# f = open("cwiczenie2.txt")
# lista = []
# for i in f:
#     lista.append(i)
#
# print(lista)

# to samo inaczej


# -----------------------------------Cwiczenie3----------------------------------
# Napisz program w Pythonie, który znajdzie najd?u?sze s?owa w pliku tekstowym.

# najdluszyznak = open("cwiczenie3.txt")
# data = najdluszyznak.read()
#
# lista = data.split()
# print(lista)
#
# slowo = ""
# for x in lista:
#     if len(x) > len(slowo):
#         slowo = x
#
#
# print(slowo)


# -----------------------------------Cwiczenie4----------------------------------
# Napisz program w Pythonie, który zapisze listę do pliku.

# lista = ["abc", "Python", "dfg", 12345]
# nowy = open("cwiczenie4.txt", "w")
# for a in lista:
#     nowy.write(str(a) + "\n")


# -----------------------------------Cwiczenie5----------------------------------
# Napisz program w Pythonie, aby ocenić, czy plik jest zamknięty, czy nie.
#
# data_file = open("cwiczenie5.txt")
#
# print(data_file.close())
#
# print(data_file.closed)














