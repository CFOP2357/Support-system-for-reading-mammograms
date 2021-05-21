import typing
from collections.abc import Iterator, Iterable

import PIL
import tkinter

PilImage = typing.NewType("PilImage", PIL.Image.Image)
TkImage = typing.NewType("TkImage", PIL.ImageTk.PhotoImage)
Coord = typing.NewType("Coord", Iterable[float])
