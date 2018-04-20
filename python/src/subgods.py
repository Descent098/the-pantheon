from abc import ABC, abstractmethod #Library that forces abstraction, similar to abstract classes in java

class subgod(ABC):
    """
    This is the subgod class from which all other subgods/servant god classes derive
    """
    version = '0.1'

    @abstractmethod
    def __init__(self, name, type, hitpoints, devotion, attack, defence):
        """
        creates the variables associated with the class
        :type name: string
        :param name: the name of the god

        :type type: string
        :param type: the area the god is from i.e. greek

        :type hitpoints: string
        :param hitpoints: the amount of hitpoints the god starts with

        :type devotion: string
        :param devotion: the initial amount of devotion to their god the subgod has


        """
        self.name = name
        self.type = type
        self.hitpoints = hitpoints
        self.devotion = devotion
        self.rank = 5
        self.attack = attack
        self.defence = defence


    @abstractmethod
    def determinerank(self, devotion):
        """

        :type worshipers: string
        :param worshipers: the amount of worshipers a god currently has

        Method that changes the rank of the god based on worshipers;
        overridden in 'type' class | Is an abstact Method


        """
        pass

    @abstractmethod
    def servitudebonus(self):
        """Method that will be overridden based on which type of god the class is;
        adds a bonus to an attribute based on type and rank | Is an abstact Method"""
        pass


    def __str__(self):
        """Child classes will now print with all important info"""

        namestring = ("Name: {}".format(self.name))
        typestring = ("God Type: {}".format(self.type))
        hpstring = ("Hitpoints: {}".format(self.hitpoints))
        rankstring = ("Rank: {}".format(self.rank))
        devotionstring = ("Devotion: {}".format(self.devotion))
        attackstring = ("Attack: {}".format(self.attack))
        defencestring = ("Defence: {}".format(self.defence))

        return  "\n{} \n{} \n{} \n{} \n{} \n{} \n{}".format(namestring, typestring, hpstring, rankstring, devotionstring, attackstring, defencestring)
