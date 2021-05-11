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

``C:\Work_Imp\DataScience\MLOPS>dvc add data_given\winequality.csv

''git add . 
--will add all the files to the staging
-- after adding the files do the commit with a message

``git commit -m "first commit" 

git add . && git commit -m "update Readme.md"

Adding a Remote repository..

``create the new repository 

git remote add origin https://github.com/vjrmsg/DVC_Demo.git

in case, if the github is showing that master branch instead main.. we have to change it to main with below command.

``git branch -M main

-- Now push the origin to main.

``git push -u origin main

-- if above push not worked, follow below steps.

C:\Work_Imp\DataScience\MLOPS>git config --global http.sslVerify false

C:\Work_Imp\DataScience\MLOPS>git push origin main

*Create params file and update
``git add . && git commit -m "Params.yaml file  updated"
Push the changes to the GitHub.
``git push origin main

Create get_data

(MLOPS) C:\Work_Imp\DataScience\MLOPS\src>copy con get_data.py
^Z
        1 file(s) copied.
pip  install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --upgrade pandas
If pandas is not working fine.  Install the python for VSCode to resolve the issue.

``python src\get_data.py

it reads params.yaml file











