import argparse
import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).parents[2]
DATA = ROOT / "data" / "raw"


def zadanie_1() -> None:
    x = np.arange(1, 20, 0.1)
    fig, ax = plt.subplots()
    ax.plot(x, 1 / x, label="f(x) = 1/x")
    ax.set(xlim=(0, 20), ylim=(0, 1), xlabel="x", ylabel="f(x)")
    ax.legend()
    plt.show()


def zadanie_2() -> None:
    x = np.arange(1, 21)
    fig, ax = plt.subplots()
    ax.plot(x, 1 / x, label="f(x) = 1/x", linestyle="--", marker=">", color="green")
    ax.set(xlim=(0, 20), ylim=(0, 1), xlabel="x", ylabel="f(x)")
    ax.legend()
    plt.show()


def zadanie_3() -> None:
    x = np.arange(0, 30.1, 0.1)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), label="sin(x)")
    ax.plot(x, np.cos(x), label="cos(x)")
    ax.set(xlabel="x", ylabel="f(x)")
    ax.legend()
    plt.show()


def zadanie_4() -> None:
    x = np.arange(0, 30.1, 0.1)
    fig, ax = plt.subplots()
    ax.plot(x, -np.sin(x), label="-sin(x)")
    ax.plot(x, 2 + np.sin(x), label="2 + sin(x)")
    ax.legend()
    plt.show()


def zadanie_5() -> None:
    columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    df = pd.read_table(DATA / "iris.data", sep=",", header=None, names=columns)
    fig, ax = plt.subplots()
    ax.scatter(df["sepal_length"], df["sepal_width"],
               s=np.abs(df["sepal_length"] - df["sepal_width"]))
    ax.set(xlabel="sepal length", ylabel="sepal width")
    plt.show()


def zadanie_6() -> None:
    df = pd.read_excel(DATA / "imiona.xlsx")
    fig, axes = plt.subplots(1, 3, figsize=(18, 8))
    by_sex = df.groupby("Plec")["Liczba"].sum()
    axes[0].bar(by_sex.index, by_sex.values, color=["pink", "blue"])
    axes[0].set(title="Liczba narodzin wedlug plci", xlabel="Plec", ylabel="Liczba")
    by_year_sex = df.groupby(["Rok", "Plec"])["Liczba"].sum().unstack()
    axes[1].plot(by_year_sex.index, by_year_sex["K"], label="Kobiety", color="magenta")
    axes[1].plot(by_year_sex.index, by_year_sex["M"], label="Mezczyzni", color="cyan")
    axes[1].set(title="Narodziny wedlug roku i plci", xlabel="Rok", ylabel="Liczba")
    axes[1].legend()
    by_year = df.groupby("Rok")["Liczba"].sum()
    axes[2].bar(by_year.index, by_year.values, color="green")
    axes[2].set(title="Laczna liczba narodzin", xlabel="Rok", ylabel="Liczba")
    fig.tight_layout()
    plt.show()


def zadanie_7() -> None:
    liczba_rzutow = 50
    results = [random.randint(1, 6) + random.randint(1, 6)
               for _ in range(liczba_rzutow)]
    fig, ax = plt.subplots()
    ax.hist(results, bins=range(2, 14), edgecolor="black", align="left",
            color="skyblue", rwidth=0.8)
    ax.set(title=f"Suma oczek z {liczba_rzutow} rzutow dwiema kostkami",
           xlabel="Suma oczek", ylabel="Liczba wystapien")
    ax.set_xticks(range(2, 13))
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


def zadanie_8() -> None:
    df = pd.read_csv(DATA / "zamowienia.csv", sep=";")
    totals = df.groupby("Sprzedawca")["Utarg"].sum()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(totals, labels=totals.index, autopct="%1.1f%%")
    ax.set(title="Udzial sprzedawcow w ogolnej sumie zamowien")
    ax.axis("equal")
    plt.show()


TASKS = {1: zadanie_1, 2: zadanie_2, 3: zadanie_3, 4: zadanie_4,
         5: zadanie_5, 6: zadanie_6, 7: zadanie_7, 8: zadanie_8}


def main() -> None:
    parser = argparse.ArgumentParser(description="Zadania z Matplotlib cz. 1")
    parser.add_argument("--task", type=int, choices=TASKS, default=1)
    args = parser.parse_args()
    TASKS[args.task]()


if __name__ == "__main__":
    main()
