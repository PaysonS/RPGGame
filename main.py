import tcod
import copy
from engine import Engine
import entity_factories

from inputHandlers import EventHandler
from procgen import generate_dungeon


def main() -> None:
    screenWidth = 80
    screenHeight = 50

    mapWidth = 80
    mapHeight = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    max_monster_per_room = 2

    tileset = tcod.tileset.load_tilesheet("Font.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = copy.deepcopy(entity_factories.player)
  
    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=mapWidth,
        map_height=mapHeight,
        max_monster_per_room=max_monster_per_room,
        player=player,
    )

    engine = Engine(
        event_handler=event_handler, game_map=game_map, player=player
    )

    with tcod.context.new_terminal(
        screenWidth,
        screenHeight,
        tileset=tileset,
        title="My Rogue Game",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screenWidth, screenHeight, order="F")
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()
