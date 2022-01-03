
let triggeringMessage = event.text.getString();

let split = triggeringMessage.split('>');

if (split[0] == "<FlareStormGaming") {
    // pass
} else {
    Chat.actionbar(triggeringMessage, false);
}


