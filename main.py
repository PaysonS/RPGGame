import tcod
from actions import EscapeAction, MovementAction
from inputHandlers import EventHandler


def main()-> None:
    screenWidth = 80
    screenHeight = 50
    
    playerX = int(screenWidth / 2)
    playerY = int(screenHeight / 2)
    
    tileset = tcod.tileset.load_tilesheet(
        "Font.png",32,8,tcod.tileset.CHARMAP_TCOD
    )
    
    event_handler = EventHandler()
   
    with tcod.context.new_terminal(
       screenWidth,
       screenHeight,
       tileset=tileset,
       title = "My Rogue Game",
       vsync=True,
   ) as context:
       root_console = tcod.console.Console(screenWidth,screenHeight, order="F")
       while True:
           root_console.print(x=playerX,y=playerY, string="@")
           
           context.present(root_console)
           root_console.clear()
           
           for event in tcod.event.wait():
               action = event_handler.dispatch(event)
               if action is None:
                   continue
               if isinstance(action,MovementAction):
                   playerX += action.dx
                   playerY += action.dy
               elif isinstance(action, EscapeAction):
                   raise SystemExit()
               
    
if __name__ == "__main__":
    main()
    
    