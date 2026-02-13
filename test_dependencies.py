#!/usr/bin/env python3
"""
Test script to verify that all dependencies from pixi.toml are installed correctly.
This script checks if the required Python packages are available and can be imported.
"""

import sys
import importlib
from typing import List, Tuple, Dict

# Dependencies from pixi.toml with correct import names
REQUIRED_PACKAGES = {
    'sympy': {
        'import_name': 'sympy',
        'description': 'SymPy symbolic mathematics library',
        'install_name': 'sympy'
    },
    'scipy': {
        'import_name': 'scipy',
        'description': 'Scientific computing library',
        'install_name': 'scipy'
    },
    'matplotlib': {
        'import_name': 'matplotlib',
        'description': 'Plotting library',
        'install_name': 'matplotlib'
    },
    'ipython': {
        'import_name': 'IPython',
        'description': 'Enhanced interactive Python shell',
        'install_name': 'ipython'
    },
    'jupyter': {
        'import_name': 'jupyter',
        'description': 'Jupyter notebook environment',
        'install_name': 'jupyter'
    },
    'pythreejs': {
        'import_name': 'pythreejs',
        'description': '3D visualization library',
        'install_name': 'pythreejs'
    }
}

def check_package(package_name: str, package_info: Dict[str, str]) -> Tuple[bool, str]:
    """Check if a package can be imported and get its version."""
    try:
        module = importlib.import_module(package_info['import_name'])
        version = getattr(module, '__version__', 'unknown')
        return True, f"✓ {package_info['install_name']} ({package_info['description']}) - Version: {version}"
    except ImportError as e:
        return False, f"✗ {package_info['install_name']} ({package_info['description']}) - Not installed: {e}"
    except Exception as e:
        return False, f"✗ {package_info['install_name']} ({package_info['description']}) - Error: {e}"

def main() -> int:
    """Main function to test all dependencies."""
    print("Testing dependencies from pixi.toml...")
    print("=" * 50)
    
    results = []
    all_passed = True
    
    for package_name, package_info in REQUIRED_PACKAGES.items():
        success, message = check_package(package_name, package_info)
        results.append((success, message))
        print(message)
        if not success:
            all_passed = False
    
    print("=" * 50)
    
    if all_passed:
        print("✓ All dependencies are installed correctly!")
        return 0
    else:
        print("✗ Some dependencies are missing or have issues.")
        print("\nTo install missing dependencies, run:")
        print("  pixi install")
        return 1

if __name__ == "__main__":
    sys.exit(main())