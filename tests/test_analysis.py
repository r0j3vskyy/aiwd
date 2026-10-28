from pathlib import Path
import tempfile
import unittest

import pandas as pd

from analysis_project import (
    births_by_year_and_sex,
    load_names,
    load_orders,
    load_pokemon,
    orders_by_year,
)


ROOT = Path(__file__).parents[1]
RAW = ROOT / "data" / "raw"


class AnalysisDataTests(unittest.TestCase):
    def test_load_names_and_aggregate_births(self) -> None:
        names = load_names(RAW / "imiona.xlsx")
        summary = births_by_year_and_sex(names)

        self.assertEqual({"K", "M"}, set(summary.columns))
        self.assertGreater(len(names), 1000)
        self.assertTrue((summary >= 0).all().all())

    def test_load_orders_and_aggregate_by_year(self) -> None:
        orders = load_orders(RAW / "zamowienia.csv")
        summary = orders_by_year(orders)

        self.assertIn("Suma", summary.columns)
        self.assertIn("Srednia", summary.columns)
        self.assertEqual({2003, 2004, 2005}, set(summary.index))
        self.assertTrue((summary["Suma"] > 0).all())

    def test_load_pokemon(self) -> None:
        pokemon = load_pokemon(RAW / "Pokemon.csv")

        self.assertEqual(151, len(pokemon))
        self.assertIn("Legendary", pokemon.columns)

    def test_invalid_orders_schema_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.csv"
            pd.DataFrame({"value": [1]}).to_csv(path, index=False, sep=";")

            with self.assertRaises(ValueError):
                load_orders(path)


if __name__ == "__main__":
    unittest.main()
