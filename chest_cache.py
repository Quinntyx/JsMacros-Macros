import sys

if file.getParent() not in sys.path:
    sys.path.append(file.getParent())

import ctLib
import utils
import json

world = utils.WorldWrapper(World)

if Hud.isContainer():
    current = ctLib.StorageBlock(Player.rayTraceBlock(8, True))
    inventory = Player.openInventory()
    try:
        container = inventory.getMap().get("container")
        for i in container:
            current.add_item(i, inventory.getSlot(i).getItemID(), inventory.getSlot(i).getCount())
        path = f"chestTracker/data_{ctLib.make_safe(world.server_address) + '-' + ctLib.id_to_name(world.dimension)}.json"
        try:
            with open(path, 'r') as f:
                existing = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            utils.ChatWrapper(Chat).log_fancy(f"No tracked chests so far on {world.server_address} in dimension {ctLib.id_to_name(world.dimension)}, starting new")
            existing = {}

        with open(path, 'w') as f:

            existing[current.name] = dict(current)
            f.seek(0, 0)
            f.write(json.dumps(existing, indent=4))
    except TypeError as e:
        pass
        # utils.ChatWrapper(Chat).log_fancy(f"&cError {e}")
