import sys
if file.getParent() not in sys.path:
    sys.path.append(file.getParent()) # making files importable

import os
import utils

script_filetypes = ['js', 'py']  # defines what types are considered scripts

if event.message[0] == '0':
    msg = event.message[1:].split()
    scripts = []
    for i in os.listdir("./"): 
        if '.' in i:
            if i.split('.')[1] in script_filetypes:
                scripts.append(i.split('.'))
    
    script_name = ''
    for i in scripts:
        if f"u_{msg[0]}" == i[0]:
            script_name = '.'.join(i)
            break

    params = utils.EventWrapper(JsMacros.createCustomEvent("paramPasser"))
    params.smart_put_list(msg[1:])

    if script_name:
        try:    
            JsMacros.runScript(script_name, params)
            Chat.actionbar(f"Running script {script_name}", False)
        except Exception as e:
            Chat.actionbar(f"Failed to run script {script_name}", False)
            Chat.log(f"Error: {e}")
    else:
        Chat.actionbar(f"Script u_{msg} does not exist", False)
    
    event.message = None # overwrites message so it isn't sent to server. 
