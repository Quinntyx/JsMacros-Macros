import sys
if file.getParent() not in sys.path:
    sys.path.append(file.getParent()) # making files importable

import utils

event = utils.EventWrapper(event)

if event[0]:
    JsMacros.runScript(event[0])
else:
    import os
    os.system("python -m compileall")