import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATA_PATH = Path(__file__).parents[2] / "data" / "raw" / "Pokemon.csv"


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH, index_col=0, encoding="latin")


def zadanie_1(df: pd.DataFrame) -> None:
    data = df[df["Type 2"].isna()]
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=data, x="Attack", y="Defense", hue="Stage", ax=ax)
    sns.move_legend(ax, loc="upper left")
    ax.set(title="Zaleznosc ataku od obrony Pokemona", xlabel="Atak", ylabel="Obrona")
    plt.show()


def zadanie_2(df: pd.DataFrame) -> None:
    data = df[df["Type 1"].isin(["Grass", "Fire", "Water"])]
    counts = data.groupby("Type 1").size().reset_index(name="Count")
    palette = {"Fire": "#F08030", "Grass": "#78C850", "Water": "#6890F0"}
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=counts, x="Type 1", y="Count", hue="Type 1", palette=palette, legend=False, ax=ax)
    ax.set(title="Rodzaje Pokemonow", xlabel="Rodzaj", ylabel="Ilosc")
    plt.show()


def zadanie_3(df: pd.DataFrame) -> None:
    counts = df["Legendary"].map({False: "Zwykly", True: "Legendarny"}).value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(counts, labels=counts.index, autopct="%1.1f%%")
    ax.set_title("Ilosc Pokemonow legendarnych")
    plt.show()


def zadanie_4(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(8, 8))
    sns.boxplot(data=df[["HP", "Attack", "Defense"]], ax=ax)
    ax.set(title="Statystyki Pokemonow", xlabel="Statystyka", ylabel="Wartosc")
    plt.show()


def zadanie_5(df: pd.DataFrame) -> None:
    data = df[["Attack", "Defense", "Legendary"]]
    sns.jointplot(data=data, x="Attack", y="Defense", hue="Legendary", kind="scatter", palette="Set2")
    plt.show()


def zadanie_6(df: pd.DataFrame) -> None:
    sns.pairplot(df[["Attack", "Defense", "Speed"]])
    plt.show()


TASKS = {
    1: zadanie_1, 2: zadanie_2, 3: zadanie_3,
    4: zadanie_4, 5: zadanie_5, 6: zadanie_6,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Zadania z Seaborn cz. 1")
    parser.add_argument("--task", type=int, choices=TASKS, default=1)
    args = parser.parse_args()
    TASKS[args.task](load_data())


if __name__ == "__main__":
    main()
