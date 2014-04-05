import json
from pprint import pprint
json_data = open('top100.json')
data = json.load(json_data)
to_write = {}
f = open('fix.json', 'a+')
for x in data['result']['tracks']:
    if x.get('albumArtist') is None:
        to_write['artist'] = x['artist']
    else:
        to_write['albumArtist'] = x['artist']
    to_write['albumKey'] = x['albumKey']
    to_write['artistUrl'] = x['albumUrl']
    to_write['embedUrl'] = x['embedUrl']
    to_write['icon'] = x['icon']
    to_write['key'] = x['key'] 
    to_write['shortUrl'] = x['shortUrl'] 
    json.dump(to_write, f)

f.close()
    
