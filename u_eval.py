import sys
if file.getParent() not in sys.path:
    sys.path.append(file.getParent()) # making files importable
    
import utils

event = utils.EventWrapper(event)

Chat.log(eval(event.join()))

