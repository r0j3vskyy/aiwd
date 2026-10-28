import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_PATH = Path(__file__).parents[2] / "data" / "raw" / "imiona.xlsx"


def load_data() -> pd.DataFrame:
    return pd.read_excel(DATA_PATH)


def zadanie_1(df: pd.DataFrame) -> None:
    data = df.groupby("Rok")["Liczba"].sum() / 1000
    data.plot(xticks=data.index, rot=45, figsize=(8, 6), grid=True,
              title="Liczba narodzin [tys.]", ylabel="Liczba [tys.]")
    plt.show()


def zadanie_2(df: pd.DataFrame) -> None:
    data = df.groupby("Plec")["Liczba"].sum() / 1000
    data.plot(kind="bar", rot=0, ylabel="Liczba osob [tys.]")
    plt.show()


def zadanie_3(df: pd.DataFrame) -> None:
    data = df[df["Rok"] >= 2012].groupby("Plec")["Liczba"].sum()
    data.plot(kind="pie", autopct="%1.1f%%",
              title="Urodzeni chlopcy i dziewczynki od 2012 roku")
    plt.show()


def zadanie_4() -> None:
    path = DATA_PATH.parent / "zamowienia.csv"
    df = pd.read_csv(path, sep=";")
    data = df["Sprzedawca"].value_counts()
    data.plot(kind="barh", title="Liczba zamowien wedlug sprzedawcy")
    plt.show()


TASKS = {1: zadanie_1, 2: zadanie_2, 3: zadanie_3, 4: zadanie_4}


def main() -> None:
    parser = argparse.ArgumentParser(description="Zadania z Pandas cz. 2")
    parser.add_argument("--task", type=int, choices=TASKS, default=1)
    args = parser.parse_args()
    if args.task == 4:
        TASKS[args.task]()
    else:
        TASKS[args.task](load_data())


if __name__ == "__main__":
    main()
