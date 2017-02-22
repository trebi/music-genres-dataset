import scrapy
import json
import urllib

# Scrabbles song's tags from Last.fm
# Run with: `scrapy runspider tags_spider.py -o data/tags.jl`
class TagsSpider(scrapy.Spider):
	name = 'tagsspider'
	with open('data/last_fm_api.key') as f_api_key:
		lastfm_api_key = f_api_key.read()
	global lastfm_api_url
	lastfm_api_url = 'http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&format=json&api_key=' + lastfm_api_key

	def start_requests(self):
		with open("data/songs.jl") as f: 
			for json_line in f.readlines():
				line = json.loads(json_line.strip())
				for song in line['songs']: 
					artist = urllib.parse.quote(song['artist'])
					track = urllib.parse.quote(song['name'])
					url = lastfm_api_url + '&artist=' + artist + '&track=' + track
					yield scrapy.Request(
						url=url,
						callback=lambda r,
						g=line['genre'],
						t=urllib.parse.unquote(track),
						a=urllib.parse.unquote(artist),
						p=song['position'],
						u=song['uri_id']:
						self.parse(r, g, t, a, p, u)
					)

	def parse(self, response, genre, track, artist, position, uri_id):
		tags = []
		j = json.loads(response.body.decode('utf-8'))
		if 'toptags' in j:
			tags = list(map(
				lambda t: {
						'tag': t['name'],
						'count': t['count']
					},
					j['toptags']['tag']
				)
			)

		return {
			'genre': genre,
			'track': track,
			'artist': artist,
			'position': position,	
			'tags': tags,
			'uri_id': uri_id
		}
