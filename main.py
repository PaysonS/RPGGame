import tcod
from engine import Engine
from entity import Entity
from game_map import GameMap
from inputHandlers import EventHandler


def main()-> None:
    screenWidth = 80
    screenHeight = 50
    
    mapWidth = 80
    mapHeight = 45
    
     
    
    tileset = tcod.tileset.load_tilesheet(
        "Font.png",32,8,tcod.tileset.CHARMAP_TCOD
    )
    
    event_handler = EventHandler()
    
    player = Entity(int(screenWidth/2), int(screenHeight/2),"@",(255,255,255))
    npc = Entity(int(screenWidth/2 - 5),int(screenHeight/2),"@",(255,255,0))
    entities = {npc,player}
    game_map = GameMap(mapWidth, mapHeight)
    
    engine = Engine(entities=entities, event_handler=event_handler,game_map=game_map,player=player)
   
    with tcod.context.new_terminal(
       screenWidth,
       screenHeight,
       tileset=tileset,
       title = "My Rogue Game",
       vsync=True,
   ) as context:
       root_console = tcod.console.Console(screenWidth,screenHeight, order="F")
       while True:
           engine.render(console=root_console,context=context)
           events = tcod.event.wait()
           engine.handle_events(events)
    
if __name__ == "__main__":
    main()
    
    