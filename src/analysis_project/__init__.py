"""Reusable data loading and aggregation helpers for the project."""

from .data import (
    load_names,
    load_orders,
    load_pokemon,
    orders_by_year,
    births_by_year_and_sex,
)

__all__ = [
    "load_names",
    "load_orders",
    "load_pokemon",
    "orders_by_year",
    "births_by_year_and_sex",
]
