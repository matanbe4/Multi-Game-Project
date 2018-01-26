import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name = "Multi-Game",
    options = {"build_exe":{"packages":["pygame"], "include_files": ["Images"]}},
    
    description = "Multi-Game",
    executables = executables
    )
