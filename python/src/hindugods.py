import gods

class hindugod(gods.Gods):
    def __init__(self, name, hitpoints, initialworshipers):
        super().__init__(name, "Hindu", hitpoints, initialworshipers)
        self.determinerank(self.worshipers)
        self.typebonus()

    def determinerank(self, worshipers):
        """Method that changes the rank of the god based on worshipers"""

        if self.worshipers >= 1000000:
            self.rank = 1
            return None
        elif self.worshipers >= 750000:
            self.rank = 2
            return None
        elif self.worshipers >= 500000:
            self.rank = 3
            return None
        elif self.worshipers >= 250000:
            self.rank = 4
            return None
        else:
            self.rank = 5
            return None

    def __str__(self):
        """String representation; calls super class gods"""
        return super().__str__()

    def typebonus(self):
        """Assigns typebonus based on current rank"""
        if self.rank == 1:
            self.hitpoints *= 1000
            return None
        elif self.rank == 2:
            self.hitpoints *= 100
            return None
        elif self.rank == 3:
            self.hitpoints *= 10
            return None
        elif self.rank == 4:
            self.hitpoints *= 2
            return None
        else:
            self.hitpoints *= 1
            return None


class vishnu(hindugod):
    def __init__(self):
        super().__init__("Vishnu", 1000000, 1000000)


    def __str__(self):
        """String representation; calls super class greekgods"""
        return super().__str__()
