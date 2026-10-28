import argparse

import numpy as np


def zadanie_1() -> None:
    a = np.array([1, 2, 3]).reshape(1, 3)
    b = np.array([3, 2, 1]).reshape(1, 3)
    print(f"a*b: {a * b}")


def zadanie_2() -> None:
    for size in (3, 4):
        matrix = np.random.randint(10, 50, size=(size, size))
        print(matrix)
        print(f"Minimum pionowo: {matrix.min(axis=0)}")
        print(f"Minimum poziomo: {matrix.min(axis=1)}")


def zadanie_3() -> None:
    a = np.array([1, 2, 3])
    b = np.array([3, 2, 1])
    print(np.dot(a, b))
    print(np.dot(a.reshape(1, 3), b.reshape(3, 1)))


def zadanie_4() -> None:
    print(np.array([-4, 11, -62]) * np.array([1.0e3, 3.1456, -2.718]))


def zadanie_5() -> None:
    values = np.array([7, -11, 4, 0, -2.5, 9]).reshape(2, 3)
    print(np.sin(np.radians(values)))


def zadanie_6() -> None:
    values = np.array([7, -11, 4, 0, -2.5, 9]).reshape(2, 3)
    print(np.cos(np.radians(values)))


def zadanie_7() -> None:
    values = np.array([7, -11, 4, 0, -2.5, 9]).reshape(2, 3)
    print(np.sin(np.radians(values)) + np.cos(np.radians(values)))


def zadanie_8() -> None:
    for index, row in enumerate(np.arange(1, 10).reshape(3, 3), start=1):
        print(f"{index}. {row}")


def zadanie_9() -> None:
    for value in np.arange(1, 10).reshape(3, 3).flat:
        print(value)


def zadanie_10() -> None:
    values = np.arange(1, 82).reshape(9, 9)
    for shape in ((27, 3), (3, 27), (1, 81), (81, 1)):
        print(values.reshape(shape))


def zadanie_11() -> None:
    values = np.arange(1, 13)
    for shape in ((3, 4), (4, 3), (2, 6)):
        print(values.reshape(shape).flatten())


TASKS = {number: globals()[f"zadanie_{number}"] for number in range(1, 12)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Zadania z NumPy cz. 2")
    parser.add_argument("--task", type=int, choices=TASKS, default=1)
    args = parser.parse_args()
    TASKS[args.task]()


if __name__ == "__main__":
    main()
