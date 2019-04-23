import cx_Freeze
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("[Game Project 4] Arcadian's Rythm v0-01 (Alpha Version).py")]

cx_Freeze.setup(
    name="Arcadian's Rythm v0.01 (Alpha Version)",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["Data",
                                             "List_Enemies.txt",
                                             "readme.txt"]}},
    executables = executables

    )
