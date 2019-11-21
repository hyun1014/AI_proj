# NUGUMATE_Model
This reposiotory is for model of NUGUMATE.


1. Requirement

This folder contains txt files which show required python packages to run source codes.
There are several txt files, and each of their names show date and time when the requirement.txt is created.
To use this model, the most recent one must be used. All of packages can be installed at once by using a command below.

pip install -r "Requirement file"

2. venv

This folder contains data for virtual environment. Python packages are in this folder.

3. Model

This folder contains all of py source codes, json files for dataset, and raw txt files which can be converted to json file

3.1. txt_files

This folder contains raw datasets. They are preprocessed and converted to json file by txt_preprocessing.py.

3.2. json_files

This folder contains json files. All of dataset from raw txt files are converted into json files.

3.3. NLP_model

This folder contains .h5 file, which is core model of this project. After model is created and executed learning, the model
is saved in this folder (.h5 file). The model can be loaded in main_model.py. There is also selected_word.json, which is used
to vectorization of dataset in json file.

3.4 testing

This folder is for testing code, so it is not related with real project.
