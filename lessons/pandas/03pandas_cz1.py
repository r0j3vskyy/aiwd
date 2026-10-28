import argparse
from pathlib import Path

import pandas as pd


DATA = Path(__file__).parents[2] / "data" / "raw"
PROCESSED = DATA.parent / "processed"


def zadanie_1(df: pd.DataFrame) -> None:
    print(df.head())


def zadanie_2(df: pd.DataFrame) -> None:
    results = {
        "a": df[df["Liczba"] > 1000],
        "b": df[df["Imie"] == "DAMIAN"],
        "c": df["Liczba"].sum(),
        "d": df.groupby("Rok")["Liczba"].sum(),
        "e": df[df["Rok"] <= 2005].groupby("Rok")["Liczba"].sum(),
        "f": df.groupby("Plec")["Liczba"].sum(),
    }
    by_name = df.groupby(["Plec", "Imie"])["Liczba"].sum()
    results["g"] = (by_name.loc["M"].idxmax(), by_name.loc["K"].idxmax())
    results["h"] = df.loc[df.groupby(["Rok", "Plec"])["Liczba"].idxmax()]
    for label, result in results.items():
        print(f"{label}:\n{result}\n")


def zadanie_3(df: pd.DataFrame) -> None:
    data = df.copy()
    data["Rok"] = pd.to_datetime(data["Data zamowienia"]).dt.year
    results = {
        "a": data["Sprzedawca"].unique(),
        "b": data["Utarg"].nlargest(5),
        "c": data["Sprzedawca"].value_counts(),
        "d": data.groupby(["Kraj", "Sprzedawca"]).size(),
        "e": data[(data["Rok"] == 2005) & (data["Kraj"] == "Polska")]["Utarg"].sum(),
        "f": data[data["Rok"] == 2004]["Utarg"].mean(),
    }
    for label, result in results.items():
        print(f"{label}:\n{result}\n")
    PROCESSED.mkdir(parents=True, exist_ok=True)
    data[data["Rok"] == 2004].to_csv(PROCESSED / "zamowienia_2004.csv", index=False)
    data[data["Rok"] == 2005].to_csv(PROCESSED / "zamowienia_2005.csv", index=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Zadania z Pandas cz. 1")
    parser.add_argument("--task", type=int, choices=[1, 2, 3], default=1)
    args = parser.parse_args()
    names = pd.read_excel(DATA / "imiona.xlsx")
    if args.task == 1:
        zadanie_1(names)
    elif args.task == 2:
        zadanie_2(names)
    else:
        zadanie_3(pd.read_csv(DATA / "zamowienia.csv", sep=";"))


if __name__ == "__main__":
    main()
