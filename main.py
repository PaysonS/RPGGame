import tcod
from engine import Engine
from entity import Entity

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

    tileset = tcod.tileset.load_tilesheet("Font.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler()

    player = Entity(int(screenWidth / 2), int(screenHeight / 2), "@", (255, 255, 255))
    npc = Entity(int(screenWidth / 2 - 5), int(screenHeight / 2), "@", (255, 255, 0))
    entities = {npc, player}
    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=mapWidth,
        map_height=mapHeight,
        player=player,
    )

    engine = Engine(
        entities=entities, event_handler=event_handler, game_map=game_map, player=player
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
