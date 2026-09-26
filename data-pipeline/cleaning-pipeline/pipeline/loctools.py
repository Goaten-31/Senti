import ctypes
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, 'loclib.dll')
handle = ctypes.CDLL(dir_path + "/loclib.dll")     

os.add_dll_directory(lib_path)

lib = ctypes.CDLL(lib_path)

lib.remove_titles_function.argtypes = [ctypes.c_int]
lib.remove_titles_function.restype = None

lib.add_commas_function.argtypes = [ctypes.c_int, ctypes.c_int]

def remove_titles(batch : int):
    return handle.remove_titles_function(batch)

def add_commas(batch :  int, reset : int):
    return handle.add_commas_function(batch, reset)