found = Hud.createDraw3D()
Hud.registerDraw3D(found)

cubeSize = 12
cubeY = 50

reverse = not GlobalVars.getBoolean("chestESPNoDungeonState")
GlobalVars.putBoolean("chestESPNoDungeonState", reverse)

new_box = True

frequency = 1  # number of times code should run per second

while GlobalVars.getBoolean("chestESPNoDungeonState"):
    Chat.log("Running")
    pos = Player.getPlayer().getPos()
    minX = int(pos.x) + cubeSize//2
    minY = int(pos.y) + cubeY//2
    minZ = int(pos.z) + cubeSize//2

    for x in range(int(pos.x) - cubeSize//2, minX):
        for y in range(int(pos.y) - cubeY//2, minY): 
            for z in range(int(pos.z) - cubeSize//2, minZ): 
                if World.getBlock(x, y, z).getId() in ["minecraft:chest", "minecraft:barrel", "minecraft:shulker_box"] \
                and World.getBlock(x, y - 1, z).getId() not in ["minecraft:mossy_cobblestone", "minecraft:cobblestone"]:
                    new_box = True
                    for e in found.getBoxes():
                        if e.pos.x1 == x and e.pos.y1 == y and e.pos.z1 == z:
                            new_box = False
                            break
                    if new_box:
                        found.addBox(x, y, z, x+1, y+1, z+1, 0xFFFFFF, 0xFF, 0xFFFFFF, 0x32, True)
    Time.sleep(int(20/frequency))
    
Hud.unregisterDraw3D(found)
