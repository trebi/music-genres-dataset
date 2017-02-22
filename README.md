# Music genres dataset

## Dataset 
  - 1494 genres
  - each genre contains 200 songs
  - for each song, following attributes are provided:
    - artist
    - song name
    - position within the list of 200 songs
    - main genre
    - sub-genres (with popularity count, which could be interpreted as weight of the sub-genre)
	- tags (every label that is not some existing genre, usually emotions, "My top 10 favourite tracs" etc.; also with popularity count)

This dataset is basically list of genres and songs available at [EveryNoise](http://everynoise.com/everynoise1d.cgi?scope=all) extended with data from [Spotify](https://developer.spotify.com/web-api/) and [Last.FM](http://www.last.fm/api). 

[[ DOWNLOAD DATASET AS ZIP ]](./data.zip)

## Scraping scripts

This repository contains scripts to scrape data from internet and then transform it to format that could be easily imported into database.

### Scraping data from internet

1. Install [Scrapy](https://scrapy.org/): `pip install scrapy`
	
2. Register at http://www.last.fm/api to obtain Last.FM API key, then save it as a file `/data/last_fm_api.key`   

3. Run scripts in this order:
	```
	scrapy runspider genre_sprider.py -o data/genres.jl \
	&& scrapy runspider playlist_spider.py -o data/spotify_playlists.jl \
	&& scrapy runspider songs_spider.py -o data/songs.jl \
	&& scrapy runspider tags_spider.py -o data/tags.jl
	```

When process finishes (it could take several minutes or maybe hours), the following files should be present in `/data` folder:

- `genres.jl`
- `songs.jl`
- `spotify_playlists.jl`
- `tags.jl`

**Data size:** ~100 MB
**Scraping time:** ~2,5 hours
  

### Transforming data to CSV format

Run python scripts in folder `/csv-scripts` in arbitrary order, they should create output files with corresponding names in folder `/data/csv`. 

### Importing into database

CSV files generates in previous step should be easily importable into database (tested just on PostgreSQL). After import is finished, run SQL script `/sql-scripts/tag.tag_is_genre.sql`. to fill up `tags.tag_is_genre` column.
