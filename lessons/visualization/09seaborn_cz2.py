import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATA_PATH = Path(__file__).parents[2] / "data" / "raw" / "Pokemon.csv"
PROCESSED_PATH = DATA_PATH.parents[1] / "processed"


def load_pokemon() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH, index_col=0, encoding="latin")


def zadanie_1(df: pd.DataFrame) -> None:
    """Analiza danych Pokemon z użyciem Pandas."""
    data = df.copy()
    print(data.head(4))
    print(data.groupby("Type 1")["Defense"].mean())
    data["Srednia obrona wg. Typu 1"] = data.groupby("Type 1")["Defense"].transform("mean")
    data["Ulubiony"] = (
        ((data["Type 1"] == "Rock") | (data["Type 2"] == "Rock"))
        .map({True: "Tak", False: "Nie"})
    )
    data["Dwa typy"] = data["Type 1"] + "-" + data["Type 2"].fillna("Brak")
    print(data.head(10))
    print(f"Liczba Pokemonow: {len(data)}")
    data = data[data["Legendary"] != True]
    print(f"Liczba zwyklych Pokemonow: {len(data)}")
    print(f"Brak drugiego typu: {data['Type 2'].isna().sum()}")
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
    data.to_csv(PROCESSED_PATH / "modified_pokemon.csv", index=False)


def zadanie_2(df: pd.DataFrame) -> None:
    """Tworzy zestaw wykresow porownujacych statystyki Pokemon."""
    data = df[df["Legendary"] != True].copy()
    rodzaje = data[data["Type 1"].isin(["Dragon", "Normal", "Fire"])]
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Analiza statystyk Pokemonow regionu Kanto", fontsize=20)

    axes[0, 0].bar(
        ["Atak", "Obrona"],
        [data["Attack"].mean(), data["Defense"].mean()],
        color=["red", "skyblue"],
    )
    axes[0, 0].set_title("Srednie wartosci ataku i obrony")

    percentages = data["Type 1"].value_counts(normalize=True) * 100
    axes[0, 1].pie(
        percentages,
        labels=percentages.index,
        autopct="%1.1f%%",
        pctdistance=0.85,
        startangle=140,
    )
    axes[0, 1].set_title("Rozklad Pokemonow wedlug typu")

    palette = {"Dragon": "red", "Normal": "green", "Fire": "orange"}
    sns.scatterplot(
        data=rodzaje, x="Sp. Atk", y="Sp. Def", hue="Type 1", palette=palette,
        s=30, ax=axes[1, 0],
    )
    axes[1, 0].set_title("Zaleznosc Sp. Def od Sp. Atk")

    sns.boxplot(
        data=rodzaje, x="Type 1", y="Speed", hue="Type 1",
        palette=palette, legend=False, ax=axes[1, 1],
    )
    axes[1, 1].set_title("Rozklad predkosci Pokemona")
    fig.tight_layout()
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
    output = PROCESSED_PATH / "wykresy.png"
    fig.savefig(output, dpi=300, bbox_inches="tight")
    plt.show()


TASKS = {1: zadanie_1, 2: zadanie_2}


def main() -> None:
    parser = argparse.ArgumentParser(description="Zadania z Seaborn cz. 2")
    parser.add_argument("--task", type=int, choices=[1, 2], default=1)
    args = parser.parse_args()
    TASKS[args.task](load_pokemon())


if __name__ == "__main__":
    main()
