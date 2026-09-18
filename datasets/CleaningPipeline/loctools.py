import ctypes
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.join(dir_path, 'loclib.dll')
handle = ctypes.CDLL(dir_path + "/loclib.dll")     

os.add_dll_directory(lib_path)

lib = ctypes.CDLL(lib_path)

def remove_title(input_file_path, output_file_path):
    return handle.remove_title(input_file_path, output_file_path)

def remove_commas(input_file_path, output_file_path):
    return handle.remove_comams(input_file_path, output_file_path)