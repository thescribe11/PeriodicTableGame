import tkinter as tk


ELEMENTS = {
    1: {
        1: 'H', 2: 'He'
    },
    2: {
        3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne',
    },
    3: {
        11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: "P", 16: 'S', 17: 'Cl', 18: 'Ar',
    },
    4: {
        19: 'K', 20: 'Ca', 21: 'Sc', 22: 'Ti', 23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co', 28: 'Ni', 29: 'Cu', 30: 'Zn', 31: 'Ga', 32: 'Ge', 33: 'As', 34:'Se', 35: 'Br', 36: 'Kr'
    },
    5: {
        37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr', 41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh', 46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn', 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe'
    },
    6: {
        55: 'Cs', 56: 'Ba', 71: 'Lu', 72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: "Os", 77: 'Lr', 78: 'Pt', 79: 'Au', 80: 'Hg', 81: 'Ti', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn'
    },
    7: {
        87: 'Fr', 88: 'Ra', 103: 'Lr', 104: 'Rf', 105: 'Db', 106: 'Sg', 107: 'Bh', 108: 'Hs', 109: 'Mt', 110: 'Uun', 111: 'Uuu', 112: 'Uub', 114: 'Uuq'
    },
    8: {
        57: 'La', 58: 'Ce', 59: 'Pr', 60: 'Nd', 61: 'Pm', 62: 'Sm', 63: 'Ue', 64: 'Gd', 65: 'Tb', 66: 'Dy', 67: 'Ho', 68: 'Er', 69: 'Tm', 70: 'Yb'
    },
    9: {
        89: 'Ac', 90: 'Th', 91: 'Pa', 92: 'U', 93: 'Np', 94: 'Pu', 95: 'Am', 96: 'Cm', 97: 'Bk', 98: 'Cf', 99: 'Es', 100: 'Fm', 101: 'Md', 102: 'No'
    }
}

ANSWERED_QUESTIONS = list()

import requests
class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self._startup()

        self.mainloop()

    def _startup(self):
        frame = html.HtmlFrame(self, vertical_scrollbar=False, horizontal_scrollbar=False)
        frame.set_content(requests.get('http://google.com').text)
        frame.grid()

if __name__ == "__main__":
    Main()