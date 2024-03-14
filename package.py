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
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
]

uuid = "repository.Imath"

build_system = "cmake"


def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.IMATH_ROOT_DIR = "{root}"
    env.Imath_ROOT = "{root}"
    env.Imath_DIR = "{root}/lib64/cmake/Imath"
    env.LD_LIBRARY_PATH.append("{root}/lib64")
