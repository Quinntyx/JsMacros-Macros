const reverse = !GlobalVars.getBoolean("fullBrightState");
GlobalVars.putBoolean("fullBrightState", reverse);

if (reverse) {
    Chat.log(Chat.createTextBuilder().append("[").withColor(0x7)
    .append("Utils").withColor(0x6)
    .append("]").withColor(0x7)
    .append(" FullBright").withColor(0xd)
    .append(" enabled").withColor(0xa).build());
    Client.getGameOptions().setGamma(16.0);
} else {
    Chat.log(Chat.createTextBuilder().append("[").withColor(0x7)
    .append("Utils").withColor(0x6)
    .append("]").withColor(0x7)
    .append(" FullBright").withColor(0xd)
    .append(" disabled").withColor(0xc).build());
    Client.getGameOptions().setGamma(0.5);
}
