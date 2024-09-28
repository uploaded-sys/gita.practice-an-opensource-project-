import subprocess
import sys
import time
def check_install_module(module):
    """Check if a Python module is installed. If not, install it."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", module])
        print(f"{module} is already installed.")
    except subprocess.CalledProcessError:
        try:
            print(f"Installing {module}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            print(f"{module} installed successfully.")
            print("Installation complete. you can now play the game ")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {module}: {e}")
            sys.exit(1)

def main():
    # Example usage: specify modules to check and install
    modules_to_install = ["tqdm"]

    for module in modules_to_install:
        check_install_module(module)
    
    # Optionally, you can add code to launch your game here
    print("module scan complete")

if __name__ == "__main__":
    main()
    time.sleep(10)
