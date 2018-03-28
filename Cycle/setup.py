from cx_Freeze import setup, Executable

setup(
    name = "cycle",
    version = "1.0",
    description = "cycle solver",
    executables = [Executable("find.py")]
)