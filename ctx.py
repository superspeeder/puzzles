tiles = {'tl':'01','t':'02','tr':'03','l':'04','m':'05','r':'06','bl':'07','bt':'08','br':'09','cnr;lt':'10','cnr;lb':'11','cnr;rt':'12','cnr;rb':'13'}
tile_symbol = '#'

map = '''#####      
  #######  
  #######  
    #######
'''

cmap = []

map_lines=  map.splitlines()
for line in map_lines:
  cmap.append([])
  for inum, item in enumerate(list(line)):
    if item == tile_symbol:
      cmap[-1].append(inum)

