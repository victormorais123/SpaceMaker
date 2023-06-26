import cx_Freeze

executables = [cx_Freeze.Executable(script="main.py", icon="images/space.png")]

cx_Freeze.setup(
    name="Space Marker",
    version = "1.0",
    options={"build_exe":
        {"packages":
            ["pygame", "tkinter", "json"],"include_files":["images", "sounds"]}},
    executables = executables
)

