import argparse

import matplotlib.pyplot as plt
import numpy as np


def zadanie_1() -> None:
    t = np.linspace(0, 2 * np.pi, 100)
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot(np.sin(t), 2 * np.cos(t), t, label="zadanie 1")
    ax.legend()
    plt.show()


def zadanie_2() -> None:
    markers = ["o", "s", "^", "D", "P"]
    colors = ["red", "green", "blue", "orange", "purple"]
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    for marker, color in zip(markers, colors):
        ax.scatter(np.random.rand(10), np.random.rand(10), np.random.rand(10),
                   marker=marker, color=color)
    plt.show()


def zadanie_3() -> None:
    x, y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
    z = np.sin(np.sqrt(x**2 + y**2))
    for colormap in ["viridis", "plasma", "inferno", "cividis", "coolwarm"]:
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        ax.plot_surface(x, y, z, cmap=colormap, edgecolor="none")
        ax.set_title(colormap)
    plt.show()


def zadanie_4() -> None:
    x, y = np.meshgrid(np.arange(4), np.arange(5))
    x, y = x.ravel(), y.ravel()
    top = x + y
    fig = plt.figure(figsize=(12, 8))
    axes = [fig.add_subplot(221, projection="3d"), fig.add_subplot(222, projection="3d"),
            fig.add_subplot(223, projection="3d"), fig.add_subplot(224, projection="3d")]
    for ax, shade, color, title in zip(
        axes,
        [True, False, True, False],
        ["red", "blue", "yellow", "orange"],
        ["Czerwony zacieniony", "Niebieski bez cieniowania",
         "Zolty zacieniony", "Pomaranczowy bez cieniowania"],
    ):
        ax.bar3d(x, y, np.zeros_like(top), 1, 1, top, shade=shade, color=color)
        ax.set_title(title)
    plt.show()


TASKS = {1: zadanie_1, 2: zadanie_2, 3: zadanie_3, 4: zadanie_4}


def main() -> None:
    parser = argparse.ArgumentParser(description="Zadania z Matplotlib cz. 2")
    parser.add_argument("--task", type=int, choices=TASKS, default=1)
    args = parser.parse_args()
    TASKS[args.task]()


if __name__ == "__main__":
    main()
