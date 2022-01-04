import sys
if file.getParent() not in sys.path:
    sys.path.append(file.getParent()) # making files importable

import os
import utils

script_filetypes = ['js', 'py']  # defines what types are considered scripts

# Chat.log("utils_run.py triggered")

if event.message[0] == '.':
    Chat.log("utils_run.py detected prefix '.'")
    msg = event.message[1:].split()
    event.message = None  # overwrites message so it isn't sent to server.
    context.releaseLock()
    scripts = []
    for i in os.listdir("./"): 
        if '.' in i:
            if i.split('.')[1] in script_filetypes:
                scripts.append(i.split('.'))
    # Chat.log(f"utils_run.py detected valid scripts: {scripts}")

    script_name = ''
    for i in scripts:
        if f"u_{msg[0]}" == i[0]:
            script_name = '.'.join(i)
            break

    # Chat.log("\n")
    # Chat.log(f"utils_run.py using script {script_name}")

    params = utils.EventWrapper(JsMacros.createCustomEvent("paramPasser"))
    # Chat.log("utils_run.py instantiated EventWrapper params with name paramPasser")

    params.smart_put_list(msg[1:])
    # Chat.log("utils_run.py added parameters to EventWrapper params")

    if script_name:
        # Chat.log("utils_run.py target script exists")
        try:
            Chat.log("utils_run.py attempting to run script")
            Chat.log(f"Parameter 0: {params[0]}")
            JsMacros.runScript(script_name, params.finalize())
            Chat.actionbar(f"Running script {script_name}", False)
        except Exception as e:
            Chat.actionbar(f"Failed to run script {script_name}", False)
            Chat.log(f"Error: {e}")
    else:
        Chat.actionbar(f"Script u_{msg[0]} does not exist", False)
