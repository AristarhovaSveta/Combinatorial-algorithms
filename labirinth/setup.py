from cx_Freeze import setup, Executable

setup(
    name = "labirinth",
    version = "1.0",
    description = "labirinth solver",
    executables = [Executable("solver.py")]
)