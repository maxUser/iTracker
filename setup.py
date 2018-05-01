from cx_Freeze import setup, Executable

base = None

executables = [Executable("iTracker.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "iTracker",
    options = options,
    version = "0.1.0",
    description = '<any description>',
    executables = executables
)
