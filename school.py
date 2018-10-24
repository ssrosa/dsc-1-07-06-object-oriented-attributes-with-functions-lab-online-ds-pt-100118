import copy

class School:
	def __init__(self, name=None):
		self.name = name
		self._roster = {}

	def roster(self):
		return self._roster

	def add_student(self, name, grade):
		if grade in self._roster:
			self._roster[grade].append(name)
		else:
			self._roster[grade] = [name]
#		return self._roster

	def grade(self, grade):
		return self._roster[grade]

	def sort_roster(self):
		self.sorted_roster = copy.deepcopy(self._roster)
		for key in self.sorted_roster:
				self.sorted_roster[key].sort()
		return self.sorted_roster
