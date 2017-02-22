UPDATE recsys.tags SET tag_is_genre = TRUE WHERE tag IN (
	SELECT tag FROM recsys.tags INNER JOIN recsys.genres ON recsys.tags.tag = recsys.genres.name
)