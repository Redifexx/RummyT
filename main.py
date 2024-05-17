class Tile:
    def __init__(self, color, isJoker, number):
        self.color = color
        self.isJoker = isJoker
        self.number = number

def setupTiles():
    colors = ['blue', 'red', 'orange', 'black']
    tiles = []
    #Setup Tiles
    for i in range(4): #Four Colors
        for j in range(2): # Two Sets
            for k in range(13): # 13 numbers
                tile = Tile(colors[i], False, k+1)
                tiles.append(tile)
    
    #Jokers
    tile = Tile(colors[2], True, -1) #Orange
    tiles.append(tile)

    tile = Tile(colors[3], True, -1) #Black
    tiles.append(tile)

    return tiles

def main():
    tiles = setupTiles()

    for tile in tiles:
        if tile.isJoker:
            print(f"Joker:  {tile.color}")
        else:
            print(f"Color: {tile.color}, Number: {tile.number}")

main()