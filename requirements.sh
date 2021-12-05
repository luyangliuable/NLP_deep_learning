# chmod +x requirements.sh to run
#!/bin/bash

pip install virtualenv
python3 -m venv env
source env/bin/activate
pip install pylint
pip install torch torchvision torchaudio
