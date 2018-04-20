import gods

class greekgods(gods.Gods):
    def __init__(self, name, hitpoints, initialworshipers):
        super().__init__(name, "Greek", hitpoints, initialworshipers)

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
        if rank == 1:
            self.followerrate = 1000
            return None
        elif rank == 2:
            self.followerrate = 100
            return None
        elif rank == 3:
            self.followerrate = 10
            return None
        elif rank == 4:
            self.followerrate = 2
            return None
        else:
            self.followerrate = 1
            return None

class zuess(greekgods):
    def __init__(self):
        super().__init__("Zuess", 1000000, 1000000)


    def __str__(self):
        """String representation; calls super class greekgods"""
        return super().__str__()
