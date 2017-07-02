class Song(object):
	"""dlyricstring for Song"""
	def __init__(self, lyrics):
		super(Song, self).__init__()
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_song = Song(["Happy birthday to you",
	"I don't want to get Sued",
	"So i'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
	"With pocket full of shells"])

happy_song.sing_me_a_song()
bulls_on_parade.sing_me_a_song()			

