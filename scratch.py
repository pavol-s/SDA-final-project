"""
1. Stwórz funkcję która przyjmuje jeden argument który ma być stringiem, funkcja powinna policzyć których znaków w
stringu były najwięcej i zwrócić znak oraz liczbę powtórzeń.
Np. dla stringa 'ala ma kota' wynikiem powinno być a, 4

2. (z gwiazdką) Stworzyć funkcję która przyjmie listę w liście elementem może być kolejna lista, lub liczba całkowita, zadaniem
funkcji jest 'spłaszczenie listy' i podanie wyniku, czyli, jeśli funkcja przyjmie listę [1, 2, [3, [4, 5]], 6, [[[7]]], 8, 9, 10]
to wynik powinien wynosić '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', liczba zagnieżdżeń w liście może być nieskończona, nie możemy zakładać
konkretnej liczby.
"""

def letter_count(x: str):
    all_freq = {}
    for letter in x:
        if letter in all_freq:
            all_freq[letter] += 1
        else:
            all_freq[letter] = 1
    max_letter = max(all_freq, key=all_freq.get)
    print(f"{max_letter}, {all_freq[max_letter]}")


letter_count("The regional capital of Silesian voivodeship is Katowice")