const reverse = !GlobalVars.getBoolean("sp_tntPainterState");
GlobalVars.putBoolean("sp_tntPainterState", reverse);

if (reverse) {
    Chat.log(Chat.createTextBuilder().append("[").withColor(0x7)
    .append("Utils").withColor(0x6)
    .append("]").withColor(0x7)
    .append(" TNTPainter").withColor(0xd)
    .append(" enabled").withColor(0xa).build());
} else {
    Chat.log(Chat.createTextBuilder().append("[").withColor(0x7)
    .append("Utils").withColor(0x6)
    .append("]").withColor(0x7)
    .append(" TNTPainter").withColor(0xd)
    .append(" disabled").withColor(0xc).build());
}


let new_box = true;

while (GlobalVars.getBoolean("sp_tntPainterState")) {
    let targetBlock = Player.rayTraceBlock(100, true)
    Chat.say("/summon tnt ".concat(targetBlock.getX(), ' ', targetBlock.getY(), ' ', targetBlock.getZ(), ' '))
    Time.sleep(100)
}

//Hud.unregisterDraw3D(found)
