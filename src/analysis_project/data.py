from __future__ import annotations

from pathlib import Path

import pandas as pd


NAMES_COLUMNS = {"Rok", "Imie", "Liczba", "Plec"}
ORDERS_COLUMNS = {"Kraj", "Sprzedawca", "Data zamowienia", "idZamowienia", "Utarg"}
POKEMON_COLUMNS = {"Name", "Type 1", "Attack", "Defense", "Speed", "Legendary"}


def _validate_columns(frame: pd.DataFrame, required: set[str], source: Path) -> None:
    missing = required.difference(frame.columns)
    if missing:
        missing_names = ", ".join(sorted(missing))
        raise ValueError(f"{source} is missing required columns: {missing_names}")


def load_names(path: str | Path) -> pd.DataFrame:
    source = Path(path)
    frame = pd.read_excel(source)
    _validate_columns(frame, NAMES_COLUMNS, source)
    frame["Rok"] = pd.to_numeric(frame["Rok"], errors="raise").astype("int64")
    frame["Liczba"] = pd.to_numeric(frame["Liczba"], errors="raise")
    if frame[list(NAMES_COLUMNS)].isna().any().any():
        raise ValueError(f"{source} contains missing values in required columns")
    return frame


def load_orders(path: str | Path) -> pd.DataFrame:
    source = Path(path)
    frame = pd.read_csv(source, sep=";")
    _validate_columns(frame, ORDERS_COLUMNS, source)
    frame["Data zamowienia"] = pd.to_datetime(frame["Data zamowienia"], errors="raise")
    frame["Utarg"] = pd.to_numeric(frame["Utarg"], errors="raise")
    if frame[["Kraj", "Sprzedawca", "Data zamowienia", "Utarg"]].isna().any().any():
        raise ValueError(f"{source} contains missing values in required columns")
    return frame


def load_pokemon(path: str | Path) -> pd.DataFrame:
    source = Path(path)
    frame = pd.read_csv(source, encoding="latin1")
    _validate_columns(frame, POKEMON_COLUMNS, source)
    for column in ("Attack", "Defense", "Speed"):
        frame[column] = pd.to_numeric(frame[column], errors="raise")
    if frame[["Name", "Type 1", "Attack", "Defense", "Speed"]].isna().any().any():
        raise ValueError(f"{source} contains missing values in required columns")
    return frame


def births_by_year_and_sex(names: pd.DataFrame) -> pd.DataFrame:
    _validate_columns(names, NAMES_COLUMNS, Path("names"))
    return (
        names.groupby(["Rok", "Plec"], as_index=False)["Liczba"]
        .sum()
        .pivot(index="Rok", columns="Plec", values="Liczba")
        .fillna(0)
        .sort_index()
    )


def orders_by_year(orders: pd.DataFrame) -> pd.DataFrame:
    _validate_columns(orders, ORDERS_COLUMNS, Path("orders"))
    return (
        orders.assign(Rok=orders["Data zamowienia"].dt.year)
        .groupby("Rok")["Utarg"]
        .agg(Suma="sum", Srednia="mean")
        .sort_index()
    )
