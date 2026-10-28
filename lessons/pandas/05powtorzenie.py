import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


OUTPUT = Path(__file__).parents[2] / "data" / "processed" / "new_data.csv"


def create_students() -> pd.DataFrame:
    data = {
        "Student": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank",
                    "Grace", "Hannah", "Isaac", "Jack"],
        "Punktacja [%]": [85, 90, 78, np.nan, 88, 76, 92, np.nan, 80, 84],
        "Frekwencja [%]": [95, 85, np.nan, 75, 88, 92, 89, 80, np.nan, 91],
        "Zaj_dodatkowe": [True, True, False, True, False, False, False, True, False, False],
    }
    return pd.DataFrame(data)


def zadanie_1() -> None:
    grades = pd.DataFrame(
        np.random.randint(0, 101, size=(30, 5)),
        columns=["Matematyka", "Chemia", "Fizyka", "Biologia", "Informatyka"],
    )
    grades["Srednia"] = grades.mean(axis=1).round(2)
    print(grades)


def zadanie_2() -> None:
    students = create_students()
    students.loc[len(students)] = ["Maria", 93.0, 75.0, True]
    students.loc[students["Student"] == "Frank", "Zaj_dodatkowe"] = True
    students = students.fillna(100)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    students.to_csv(OUTPUT, index=False)
    print(students[students["Punktacja [%]"] > 85])
    print(f"Srednia: {students['Frekwencja [%]'].mean():.2f}")
    print(students.sort_values(
        by=["Punktacja [%]", "Frekwencja [%]"], ascending=[False, True]
    ))
    print(students.groupby("Zaj_dodatkowe")["Frekwencja [%]"].median())

    scores = students["Punktacja [%]"].to_numpy()
    normalized = (scores - scores.min()) / (scores.max() - scores.min())
    fig, ax = plt.subplots()
    ax.plot(students["Student"], normalized)
    ax.set_title("Znormalizowana punktacja")
    ax.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


TASKS = {1: zadanie_1, 2: zadanie_2}


def main() -> None:
    parser = argparse.ArgumentParser(description="Powtorzenie Pandas")
    parser.add_argument("--task", type=int, choices=TASKS, default=1)
    args = parser.parse_args()
    TASKS[args.task]()


if __name__ == "__main__":
    main()
