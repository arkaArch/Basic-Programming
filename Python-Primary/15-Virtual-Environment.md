### Install virtualenv:
Fedora/Arch doesn't come with pip pre-installed. So install it with:
    1. sudo dnf install python3-pip
    2. sudo pacman -S python-pip
    
Now install 'virtualenv' package with pip: "pip3 install virtualenv"

In linux it's installed in $HOME/.local and the script 'virtualenv' is 
installed in '/home/arka/.local/bin'.

So add this directory to PATH. You can do this with add the following line in .zshrc/.bashrc 
'export PATH="$HOME/.local/bin:$PATH"'

### Create virtual environment:
    * Go to a folder where you want to create a virtual environment.
    * Create the virtual env with "python3 -m venv .venv". 
    * Activate the virtual environment with "source .venv/bin/activate"
    * This will create .venv folder which contains local copy of python and pip installed.
    * You can check that by typing 'pip list' 
    * Copy this thing into requirement.txt by pip freeze > requirements.txt
    * You can insall those packages from requirements.txt with 
      'pip install -r /path/to/requirements.txt'
    * You can exit from venv by typing "deactivate"
