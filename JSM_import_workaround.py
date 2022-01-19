old_globals = dir()
import sys
import os
# noinspection PyPep8
from xyz.wagyourtail.jsmacros.core.library import BaseLibrary
jsmacros_libs = type(os)('jsmacros')
for attr in old_globals:
    val = globals()[attr]
    if isinstance(val, BaseLibrary):
        setattr(jsmacros_libs, attr, val)
sys.modules['jsmacros'] = jsmacros_libs
sys.path.insert(0, os.path.abspath('.'))