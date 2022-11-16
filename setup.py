from sys import platform
from cx_Freeze import setup, Executable


base = None
if platform == 'win32':
    base = 'Win32Gui'

build_exe_config = {
            # 'includes': ['tkinter', 'ttkbootstrap', 'sqlalchemy']
            'includes': ['tkinter', 'sqlalchemy'],
            'include_files': ['src'],
        }

setup(
    name='gerador_massas',
    version='1.0.0',
    description='Gerador de massas',
    options={'build_exe': build_exe_config},
    executables=[
        Executable('tela_carro.py', base=base)
    ],
)