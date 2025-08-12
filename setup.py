from cx_Freeze import setup, Executable

build_options = {
        "packages": ["tabulate"],
        "include_files": ["gradesJSON", "password.json"]
}

setup(
        name="School Management System",
        version="1.0",
        description="School Management System",
        options={"build_exe": build_options},
        executables=[Executable(
                "script.py",
                base=None,
                icon="logo.ico"
        )]
)
