import sys
if file.getParent() not in sys.path:
    sys.path.append(file.getParent())  # making files importable

import utils

Chat.log(utils.build_string("&7[&6Utils&7] &5Print &f&l| &r&6Hello, &7My Name is George!"))