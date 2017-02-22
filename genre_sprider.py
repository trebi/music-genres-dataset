import scrapy

# Downlaod list of genres alogn with URL's to the page with Spotify playlist <iframe>
# Run with: `scrapy runspider genre_sprider.py -o data/genres.jl`
class GenreSpider(scrapy.Spider):
	name = 'genrespider'
	start_urls = ['http://everynoise.com/everynoise1d.cgi?scope=all']

	def parse(self, response):
		for genre in response.css('a[href^=\?root\=]'):
			yield {
				'name': genre.css('::text').extract_first(),
				'url': genre.css('::attr(href)').extract_first()
			}
