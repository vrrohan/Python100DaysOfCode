#Python module imports any module only once during a session
import mymodule2
"""
this is print statement 1
this is print statement 2
"""

print(mymodule2.getSystemInfo())                                                #Windows 10

#importing mymodule2 again will not make python interpreter to load your module because it been loaded once already
import mymodule2
import mymodule2

#If somehow, module you imported got changed or modified, we have to reload it again using in-built module named - importlib
#reload(modulename to import) - reloads the module which was passed as an argument
import importlib as ilib
ilib.reload(mymodule2)
"""
this is print statement 1
this is print statement 2
"""
