from rdioapi import Rdio
from pprint import pprint
state = {}
r = Rdio('dxp456s4tww72scbwm7z8jbs','xC3hBJbkkY', state)
pprint(r.call('getObjectFromUrl', {"extra": "tracks"})) 
