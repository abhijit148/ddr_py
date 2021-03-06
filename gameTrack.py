class gameTrack:
	moves=[]
	tracklist=["gangnam"]
	songFile=None
	
	gangnam_raw=[
		('nw',4.922206),
		('ne',5.370756),
		('nw',5.802993),
		('ne',6.277092),
		('sw',6.72355),
		('se',7.134664),
		('sw',7.533974),
		('se',7.993727),
		('nw',8.447602),
		('ne',9.315086),
		('sw',10.186205),
		('se',10.207253),
		('se',11.131714),
		('sw',11.143401),
		('sw',12.113225),
		('se',12.540367),
		('sw',13.763686),
		('se',14.359407),
		('nw',15.746674),
		('ne',16.085149),
		('nw',17.507273),
		('ne',17.856132),
		('sw',19.318388),
		('nw',20.074537),
		('se',21.042526),
		('ne',21.92301),
		('sw',22.807151),
		('nw',23.745634),
		('se',24.567055),
		('ne',25.54354),
		('ne',26.608421),
		('nw',26.624146),
		('sw',27.554844),
		('se',28.118083),
		('ne',29.259996),
		('ne',30.108826),
		('nw',30.120595),
		('sw',31.003474),
		('se',31.937593),
		('ne',32.988445),
		('ne',33.735164),
		('nw',33.746195),
		('se',34.781235),
		('sw',35.516471),
		('se',36.369754),
		('ne',37.508509),
		('nw',37.520244),
		('se',38.301996),
		('sw',39.151259),
		('se',39.907231),
		('ne',41.125249),
		('nw',41.526261),
		('se',42.041017),
		('sw',42.494051),
		('ne',42.928749),
		('nw',43.348794),
		('se',43.854562),
		('sw',44.349951),
		('ne',44.862622),
		('nw',45.156343),
		('se',45.634865),
		('sw',46.125527),
		('se',46.48146),
		('nw',50.186223),
		('ne',50.89477),
		('nw',51.398812),
		('nw',51.717449),
		('ne',52.059503),
		('nw',52.416968),
		('ne',52.798285),
		('ne',53.263561),
		('nw',53.806365),
		('ne',54.276827),
		('nw',54.768411),
		('nw',55.119585),
		('ne',55.566214),
		('nw',56.018653),
		('ne',56.461586),
		('ne',56.883423),
		('nw',57.45329),
		('ne',57.925121),
		('nw',58.349815),
		('nw',58.754387),
		('ne',59.157341),
		('nw',59.731829),
		('ne',60.052949),
		('ne',60.49912),
		('nw',60.973136),
		('ne',61.472576),
		('nw',61.941939),
		('nw',62.326036),
		('nw',62.76673),
		('ne',63.446059),
		('nw',63.45781),
		('ne',64.517548),
		('nw',64.52847),
		('sw',65.185193),
		('se',65.577645),
		('sw',66.060811),
		('nw',68.475136),
		('ne',69.019137),
		('nw',69.991737),
		('ne',70.90443),
		('se',72.018282),
		('sw',72.039136),
		('se',72.549059),
		('sw',72.953592),
		('se',73.300609),
		('sw',73.775277),
		('se',74.268201),
		('sw',74.720079),
		('se',75.176948),
		('nw',75.564148),
		('ne',76.024388),
		('nw',77.503771),
		('ne',77.655729)]

	trackData={
	"gangnam":['gangnam.wav',gangnam_raw]
	}

	def set(self,Name):
		self.track=self.trackData[Name]
		self.songFile=self.track[0]
		for move in self.track[1]:
			self.moves.append((move[0],move[1]+1,False))