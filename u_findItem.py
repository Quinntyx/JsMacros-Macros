import sys

if file.getParent() not in sys.path:
    sys.path.append(file.getParent())  # making files importable

import ctLib
import utils
import json

found = Hud.createDraw3D()
Hud.registerDraw3D(found)

event = utils.EventWrapper(event)
world = utils.WorldWrapper(World)
max_scan_dist = 64

# Chat.log(f"chestTracker/data_{ctLib.make_safe(world.server_address) + '-' + ctLib.id_to_name(world.dimension)}.json")

with open(f"chestTracker/data_{ctLib.make_safe(world.server_address) + '-' + ctLib.id_to_name(world.dimension)}.json", 'r') as f:
    pos = Player.getPlayer().getPos()
    data = json.loads(f.read())
    for i in data.keys():
        if utils.dist_3d(*i.split(), pos.x, pos.y, pos.z) <= max_scan_dist:
            cur = ctLib.StorageBlock(input_dict=data[i])
            if world.get_block(*cur.position).getId().split(':')[1] in ["chest", "barrel", "ender_chest"]:
                if cur.has_item(ctLib.name_to_id(event[0])):
                    found.addBox(*cur.position, *[i + 1 for i in cur.position], 0xFFFFFF, 0xFF, 0xFFFFFF, 0x32, True)
            else:
                pass

Time.sleep(6000)
Hud.unregisterDraw3D(found)
