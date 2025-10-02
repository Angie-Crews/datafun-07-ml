# This script installs the required packages for the project.

import subprocess
import sys

# List of required packages
packages = ["numpy", "pandas", "matplotlib", "scikit-learn", "seaborn"]

# Install each package
for pkg in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
print("All packages installed successfully.")
