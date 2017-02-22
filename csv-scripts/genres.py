import csv
import json

with open('../data/genres.jl', encoding='utf8') as in_file:
	with open('../data/csv/genres.csv', 'a', encoding='utf8') as out_file:
		out_file.write('"name"\n')
		for json_line in in_file:
			line = json.loads(json_line)
			out_file.write(';'.join([line['name']]) + '\n')
