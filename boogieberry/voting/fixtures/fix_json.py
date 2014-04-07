import json
from pprint import pprint
json_data = open('top100.json')
data = json.load(json_data)
to_write = {}
fields = {}
f = open('fix.json', 'a+')
id_count = 0
counter = 3000
my_list = [] 
for x in data['result']['tracks']:
    to_write['model'] = 'voting.song'
    to_write['id'] = id_count

    if x.get('albumArtist') is None:
        fields['artist'] = x['artist']
        fields['albumArtist'] = None
    else:
        fields['albumArtist'] = x['artist']
        fields['artist'] = None
    fields['albumKey'] = x['albumKey']
    fields['artistUrl'] = x['albumUrl']
    fields['embedUrl'] = x['embedUrl']
    fields['icon'] = x['icon']
    fields['key'] = x['key'] 
    fields['duration'] = x['duration']
    fields['name'] = x['name']
    fields['shortUrl'] = x['shortUrl']
    fields['songId'] = counter
    to_write['fields'] = fields
    my_list.append(to_write)
    to_write = {}
    fields = {}
    counter += 1
    id_count += 1

json.dump(my_list, f)
f.close()
    
