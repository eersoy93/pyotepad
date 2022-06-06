# Pyotepad main script
# Copyright (C) 2022 Erdem Ersoy (eersoy93)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import PySimpleGUI as psg

from pyotepad.version import PYOTEPAD_VERSION

def main(args):
    psg.theme("DarkBlue11")

    layout = [
        [ psg.InputText(expand_x=True) ],
        [ psg.Button("New", expand_x=True),
          psg.Button("Open", expand_x=True),
          psg.Button("Save", expand_x=True),
          psg.Button("About", expand_x=True)],
        [ psg.Multiline(size=(80, 25) )]
    ]

    window = psg.Window("Pyotepad " + PYOTEPAD_VERSION , layout)

    while True:
        event, values = window.read()
        # FIXME: Add events
        if event == psg.WINDOW_CLOSED:
            break

if __name__ == "__main__":
    sys.exit(main(sys.argv))
