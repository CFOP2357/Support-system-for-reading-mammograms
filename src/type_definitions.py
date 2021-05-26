import typing
from collections.abc import Iterable

import PIL

PilImage = typing.NewType("PilImage", PIL.Image.Image)
TkImage = typing.NewType("TkImage", PIL.ImageTk.PhotoImage)
Coord = typing.NewType("Coord", Iterable[float])
