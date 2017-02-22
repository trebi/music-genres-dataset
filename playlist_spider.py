import scrapy
import json

# Extract and parse songs from spotify playlists
# Run with: `scrapy runspider playlist_spider.py -o data/spotify_playlists.jl`
class PlaylistSpider(scrapy.Spider):
	name = 'playlistspider'

	def start_requests(self):
		f = open("data/genres.jl")
		start_urls = [url.strip() for url in f.readlines()]
		f.close()

		for json_line in start_urls:
			line = json.loads(json_line.strip())
			genre = line['name']
			url = 'http://everynoise.com/everynoise1d.cgi' + line['url']
			yield scrapy.Request(url=url, callback=lambda r, g=genre: self.parse(r, g))

	def parse(self, response, genre):
		return {
			'genre': genre,
			'spotify_playlist_url': response.css('iframe#spotify::attr(src)').extract_first().replace("https://embed.spotify.com/?uri=", "https://open.spotify.com/embed?uri=")
		}
