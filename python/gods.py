from abc import ABC, abstractmethod #Library that forces abstraction, similar to abstract classes in java

class Gods(ABC):

    @abstractmethod
    def __init__(self, name, type, hitpoints, initialworshipers):
        self.name = name
        self.type = type
        self.hitpoints = hitpoints
        self.worshipers = initialworshipers
        self.followerrate = 1
        self.determinerank(self.worshipers)

    @abstractmethod
    def determinerank(self, worshipers):
        """Method that changes the rank of the god based on worshipers;
        overridden in 'type' class | Is an abstact Method"""
        pass

    @abstractmethod
    def typebonus(self):
        """Method that will be overridden based on which type of god the class is;
        adds a bonus to an attribute based on type and rank | Is an abstact Method"""
        pass


    def __str__(self):
        """Child classes will now print with all important info"""

        namestring = ("Name: {}".format(self.name))
        typestring = ("God Type: {}".format(self.type))
        hpstring = ("Hitpoints: {}".format(self.hitpoints))
        rankstring = ("Rank: {}".format(self.rank))
        worshipersstring = ("Worshipers: {}".format(self.worshipers))
        followerratestring = ("Follower Rate: {}".format(self.followerrate))

        return  "{} \n{} \n{} \n{} \n{}".format(namestring, typestring, hpstring, rankstring, worshipersstring, followerratestring)
