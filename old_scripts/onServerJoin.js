Chat.log("Welcome FlareStormGaming to ".concat(World.getCurrentServerAddress().split('/')[0], "!"))
Chat.log("The Current Time is ".concat(World.getTime(), " Ticks."))
let players = World.getPlayers()
for (player in players){
    Chat.log("Player: ".concat(players[player].getName(), " is online."));
}

