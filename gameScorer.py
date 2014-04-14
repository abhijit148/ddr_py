
class gameScorer:
	def getScore(self,moves):
		score=0
		for move in moves:
			if move[2]==True:
				score+=25
		return score