"""
CP1404/CP5632 Practical
Band class for use with Musician and Guitar classes
"""


class Band:
    """A Band class that contains a list of Musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.members = []

    def add(self, musician):
        """Add a Musician to the band."""
        self.members.append(musician)

    def __str__(self):
        """Return string representation of the band and its members."""
        member_descriptions = ", ".join(str(member) for member in self.members)
        return f"{self.name} ({member_descriptions})"

    def play(self):
        """Each member of the band plays (or says they need an instrument)."""
        for member in self.members:
            print(member.play())
