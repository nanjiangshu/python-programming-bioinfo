#!/usr/bin/env python

import sys
import importlib

def check_package(package_name):
    try:
        return importlib.import_module(package_name)
    except ImportError:
        return None

# List of packages to check, with their import names
packages = {
    'python': sys.version_info,
    'pandas': 'pandas',
    'matplotlib': 'matplotlib',
    'biopython': 'Bio',
    'jupyter': 'notebook',
}

for package, import_name in packages.items():
    if package == 'python':
        print(f"Python version: {'.'.join(map(str, import_name[:3]))}")
    else:
        pkg = check_package(import_name)
        if pkg:
            if hasattr(pkg, '__version__'):
                print(f"{package} version: {pkg.__version__}")
            else:
                print(f"{package} is installed, but version cannot be determined.")
        else:
            print(f"{package} is NOT installed.")
