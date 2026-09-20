import ctypes
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, 'loclib.dll')
handle = ctypes.CDLL(dir_path + "/loclib.dll")     

print(dir_path)
print(lib_path)

os.add_dll_directory(lib_path)

lib = ctypes.CDLL(lib_path)

def remove_titles():
    return handle.Loc_lib_function()