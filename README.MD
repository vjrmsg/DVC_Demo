create env

`` (base) C:\Work_Imp\DataScience>cd MLOPS
``(base) C:\Work_Imp\DataScience\MLOPS>conda create -n MLOPS python=3.9.1 -y

Error:
If your current network has https://www.anaconda.com blocked, please file
a support request with your network engineering team.

'https://repo.anaconda.com/pkgs/main/win-64'


->Use below command to not to verify the SSL.
``(base) C:\Work_Imp\DataScience\MLOPS>conda config --set ssl_verify no

Then create the environment.
``(base) C:\Work_Imp\DataScience\MLOPS>conda create -n MLOPS python=3.9.1 -y
--Working fine..

Activate the environment

(base) C:\Work_Imp\DataScience\MLOPS>conda activate MLOPS

(MLOPS) C:\Work_Imp\DataScience\MLOPS>copy con requirements.txt
dvc
dvc[gdrive]
sklearn
        1 file(s) copied.

Run the requirements.txt with PIP to install the packages.
``(MLOPS) C:\Work_Imp\DataScience\MLOPS>pip install -r requirements.txt

if the above command not working, use the below one.
``(MLOPS) C:\Work_Imp\DataScience\MLOPS>pip  install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org  -r requirements.txt

--> next creating templates for us using python program.

''template.py'' is the program

This will work with any of the system.

#os.path.join # will create directories based on the operating system.
dirs=[

    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

create the file and run the template.py file.

``python template.py

Add winequality.csv file and run git init command.

``git init
``dvc init

`` dvc add data_given/winequality.csv







