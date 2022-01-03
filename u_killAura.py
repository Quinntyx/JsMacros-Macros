import sys
if file.getParent() not in sys.path:
    sys.path.append(file.getParent())  # making files importable

import utils

reverse = not GlobalVars.getBoolean("killAuraState")
GlobalVars.putBoolean("killAuraState", reverse)

chat = utils.ChatWrapper(Chat)
world = utils.WorldWrapper(World)

turn = True

if reverse:
    chat.log_fancy("&7[&6Utils&7] &dKillAura &aenabled")
else:
    chat.log_fancy("&7[&6Utils&7] &dKillAura &cdisabled")

while GlobalVars.getBoolean("killAuraState"):
    for i in world.entities:
        # Chat.log(i.getPos())
        # Chat.log(Player.getPlayer().getPos())

        player_head = list(utils.pos_tuple(Player.getPlayer().getPos()))
        player_head[1] += Player.getPlayer().getEyeHeight()

        if utils.dist_3d(*utils.pos_tuple(i.getPos()), *utils.pos_tuple(Player.getPlayer().getPos())) > 5:
            pass
        else:
            Chat.log(i.getType())
            if i.getType() != "minecraft:player":
                if i.isAlive() and i.name() not in ("minecraft:experience_orb", "minecraft:item"):
                    if turn:
                        utils.look_at(Player.getPlayer(), *utils.pos_tuple(i.getPos()))
                    Player.getPlayer().attack(i)
                    Client.waitTick(20)

        if not GlobalVars.getBoolean("killAuraState"):
            break
