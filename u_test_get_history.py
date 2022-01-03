import sys
if file.getParent() not in sys.path:
    sys.path.append(file.getParent())  # making files importable

import utils

chat = utils.ChatWrapper(Chat)

Chat.log(list(map(str, chat.history.messages)))