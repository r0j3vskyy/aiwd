import argparse

import numpy as np


def zadanie_1() -> None:
    print(np.arange(2, 41, 2))


def zadanie_2() -> None:
    values = [1.4, 2.4, 3.6]
    print(values)
    print(np.array(values, dtype=int))


def generuj_tablice(n: int) -> tuple[np.ndarray, str]:
    values = np.arange(1, n * n + 1)
    return values, f"Rozmiar tablicy: {values.shape}"


def zadanie_3() -> None:
    print(generuj_tablice(3))


def generuj(n: int, m: int) -> np.ndarray:
    return np.logspace(start=1, stop=m, num=m, base=n, dtype=int)


def zadanie_4() -> None:
    print(generuj(2, 4))


def wektor(x: int) -> str:
    values = np.arange(x, 0, -1)
    return f"Wektor: {values}\nMacierz:\n{np.diag(values)}"


def zadanie_5() -> None:
    print(wektor(5))


def wykreslanka(slowo_pion: str, slowo_poziom: str, slowo_tyl: str) -> np.ndarray:
    words = (slowo_pion, slowo_poziom, slowo_tyl)
    if any(not isinstance(word, str) or not word for word in words):
        raise ValueError("Wszystkie słowa muszą być niepustymi napisami.")
    size = max(len(slowo_pion), len(slowo_poziom) + 1, len(slowo_tyl) + 1, 3)
    result = np.full((size, size), " ", dtype="<U1")
    result[:, 0] = list(slowo_pion.ljust(size)[:size])
    result[size // 2, 1:len(slowo_poziom) + 1] = list(slowo_poziom)
    result[-1, 1:len(slowo_tyl) + 1] = list(slowo_tyl[::-1])
    return result


def zadanie_6() -> None:
    print(wykreslanka("malina", "lizak", "jagoda"))


def macierz(n: int) -> np.ndarray:
    result = np.zeros((n, n))
    np.fill_diagonal(result, 2)
    for i in range(1, n):
        np.fill_diagonal(result[i:], 2 * (i + 1))
        np.fill_diagonal(result[:, i:], 2 * (i + 1))
    return result


def zadanie_7() -> None:
    print(macierz(3))


def insert(tab: np.ndarray, kierunek: str = "poziom") -> np.ndarray:
    if tab.ndim < 2:
        raise ValueError("Tablica musi mieć przynajmniej dwa wymiary.")
    if kierunek not in {"poziom", "pion"}:
        raise ValueError("Kierunek musi być równy 'pion' albo 'poziom'.")
    axis = 0 if kierunek == "poziom" else 1
    if tab.shape[axis] % 2:
        raise ValueError("Liczba wierszy lub kolumn musi być parzysta.")
    return np.split(tab, 2, axis=axis)[0]


def zadanie_8() -> None:
    values = np.arange(1, 17).reshape(4, 4)
    print(values)
    print(insert(values, "poziom"))
    print(insert(values, "pion"))


def finabocci(row: int, col: int) -> np.ndarray:
    if row < 1 or col < 1:
        raise ValueError("Wymiary muszą być dodatnie.")
    values = np.zeros(row * col, dtype=int)
    values[:2] = 1
    for index in range(2, len(values)):
        values[index] = values[index - 1] + values[index - 2]
    return values.reshape(row, col)


def zadanie_9() -> None:
    print(finabocci(5, 5))


TASKS = {1: zadanie_1, 2: zadanie_2, 3: zadanie_3, 4: zadanie_4,
         5: zadanie_5, 6: zadanie_6, 7: zadanie_7, 8: zadanie_8, 9: zadanie_9}


def main() -> None:
    parser = argparse.ArgumentParser(description="Zadania z NumPy cz. 1")
    parser.add_argument("--task", type=int, choices=TASKS, default=1)
    args = parser.parse_args()
    TASKS[args.task]()


if __name__ == "__main__":
    main()
