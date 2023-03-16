name = "imath"

version = "3.1.5.sse.1.0.0"

authors = [
    "ILM & AcademySoftwareFoundation"
]

description = \
    """
    Imath is a basic, light-weight, and efficient C++ representation of 2D and
    3D vectors and matrices and other simple but useful mathematical objects,
    functions, and data types common in computer graphics applications,
    including the “half” 16-bit floating-point type.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"],
]

uuid = "repository.Imath"

build_system = "cmake"


def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.IMATH_ROOT_DIR = "{root}"
    env.Imath_ROOT = "{root}"
    env.Imath_DIR = "{root}/lib64/cmake/Imath"
    env.LD_LIBRARY_PATH.append("{root}/lib64")
