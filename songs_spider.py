import scrapy
import json

# Extract and parse songs from spotify playlists
# Run with: `scrapy runspider songs_spider.py -o data/songs.jl`
class SongsSpider(scrapy.Spider):
	name = 'songsspider'

	def start_requests(self):
		f = open("data/spotify_playlists.jl")
		start_urls = [url.strip() for url in f.readlines()]
		f.close()

		for json_line in start_urls:
			line = json.loads(json_line.strip())
			genre = line['genre']
			spotify_playlist_url = line['spotify_playlist_url']
			yield scrapy.Request(url=spotify_playlist_url, callback=lambda r, g=genre: self.parse(r, g))

	def parse(self, response, genre):
		songs = []
		for track_row in response.css("ul.track-list li.track-row"):
			songs.append({
				'position': track_row.css("::attr(data-position)").extract_first(),
				'name': track_row.css("::attr(data-name)").extract_first(),
				'artist': track_row.css("::attr(data-artists)").extract_first(),
				'uri_id': track_row.css("::attr(data-uri)").extract_first()
			})
			
		return {
			'genre': genre,
			'songs': songs
		}
