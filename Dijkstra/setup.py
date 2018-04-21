from cx_Freeze import setup, Executable

setup(
    name = "dijkstra",
    version = "1.0",
    description = "dijkstra",
    executables = [Executable("min path Dijkstra.py")]
)