"""
CP1404/CP5632 Practical
Band test program using Musician and Guitar classes
"""

from band import Band
from musician import Musician
from guitar import Guitar


def main():
    """Create a Band and demonstrate playing behavior."""
    band = Band("Extreme")

    # Create musicians and add guitars where appropriate
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.00))
    band.add(nuno)

    gary = Musician("Gary Cherone")  # no instruments
    band.add(gary)

    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))
    band.add(pat)

    kevin = Musician("Kevin Figueiredo")  # no instruments
    band.add(kevin)

    # Display band info
    print("band (str)")
    print(band)

    # Each member plays
    print("band.play()")
    band.play()


main()
