import sys
if file.getParent() not in sys.path:
    sys.path.append(file.getParent()) # making files importable

import utils

# noinspection PyUnboundLocalVariable
event = utils.EventWrapper(event)


for i in event:
    Chat.log(i)

Chat.log(f"len(event) == {len(event)}")
 