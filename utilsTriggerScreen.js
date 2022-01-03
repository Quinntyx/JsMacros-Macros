let sentText = event.message; 
const default_type = ".py";

if (sentText[0] == '.') {
    //do stuff here
    script_name = "u_".concat(sentText.slice(1), default_type);
    JsMacros.runScript(script_name);
    Chat.actionbar("Ran Script ".concat(script_name), false);
    event.message = null;
}
