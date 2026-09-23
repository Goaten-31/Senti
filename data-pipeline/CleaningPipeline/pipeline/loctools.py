import ctypes
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, 'loclib.dll')
handle = ctypes.CDLL(dir_path + "/loclib.dll")     

os.add_dll_directory(lib_path)

lib = ctypes.CDLL(lib_path)

def remove_titles():
    return handle.remove_titles_function()

def add_commas():
    return handle.add_commas_function()