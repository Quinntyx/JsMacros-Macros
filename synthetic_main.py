import sys

if __name__ == '':
    from JsMacrosAC import *

if file.getParent() not in sys.path:
    sys.path.append(file.getParent())  # making files importable

# script starts here

import os
import json

try:
    with open('config/synthetic_main-config.json', 'r') as config:
        config = json.loads(config.read())
        directory = config['directory']  # default "./syntheticModules", defines the directory to look for scripts
        script_filetypes = config['filetypes']  # default ['js', 'py'], defines what types are considered scripts
        prefix = config['prefix']  # default ".", defines the prefix used for commands
        lang_key = config['lang_key']
except FileNotFoundError:
    with open('config/synthetic_main-config.json', 'w') as config:
        config.write(json.dumps({
            'directory': './syntheticModules/',
            'filetypes': [
                'js',
                'py'
            ],
            'prefix': '.',
            'lang_key': {
                "py": "Python",
                "js": "JavaScript"
            }
        }))

    directory = "./syntheticModules/"
    script_filetypes = ['js', 'py']
    prefix = '.'
    lang_key = {"py": "Python", "js": "JavaScript"}

if event.message.startswith(prefix):
    content = event.message[len(event.message.prefix):].split()
    event.message = None

    script_name = ''
    for i in os.listdir(directory):
        if '.' in i and i.split('.')[1].lower() in script_filetypes and i.split('.')[0].lower() == content[0].lower():
            script_name = i
            break

    if script_name:
        params_numeric = []
        params_named = {}
        for i in content[1:]:
            if '=' in i:
                params_named[i.split('=')[0]] = i.split('=')[1]
                continue
            params_numeric.append(i)

        parameters = JsMacros.createCustomEvent("paramPasser")
        parameters.putString(json.dumps({"numeric": params_numeric, "named": params_named}))

        JsMacros.runScript(f"{directory}script_name", parameters)

        Chat.actionbar(f"Ran Script {script_name.split('.')[0]} ({lang_key[script_name.split('.')[1]]})", False)

    else:
        Chat.actionbar(f"Script {content[0]} not found.", False)

