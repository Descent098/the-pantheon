import subgods

class catholicangel(subgods.subgod):
	def __init__(self, name, hitpoints, devotion, attack, defence):
		super().__init__(name, "Catholic", hitpoints, devotion, attack, defence)
		self.determinerank(self.devotion)
		self.servitudebonus()

	def servitudebonus(self):
		"""Method that will be overridden based on which type of angel the class is;
		adds a bonus to an attribute based on type and rank | Is an abstact Method"""
		if self.rank == 5:
			self.attack *= 1.1
			return None
		elif self.rank == 4:
			self.attack *= 2
			return None
		elif self.rank == 3:
			self.attack *= 5
			return None
		elif self.rank == 2:
			self.attack *= 10
			return None
		elif self.rank == 1:
			self.attack *= 100
			return None


	def determinerank(self, devotion):
		"""Method that changes the rank of the angel based on devotion"""
		if self.devotion >= 1000000:
			self.rank = 1
			return None
		elif self.devotion >= 750000:
			self.rank = 2
			return None
		elif self.devotion >= 500000:
			self.rank = 3
			return None
		elif self.devotion >= 250000:
			self.rank = 4
			return None
		else:
			self.rank = 5
			return None

	def __str__(self):
		"""String representation; calls super class gods"""
		return super().__str__()


class seraph(catholicangel):
	
	def __init_(self):
		super().__init__("Seraph", 1000000, 1000000, 1000, 1000)

	def __str__(self):
		"""String representation; calls super class gods"""
		return super().__str__()
