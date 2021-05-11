import os
#os.path.join # will create directories based on the operating system.
dirs=[

    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
with open(os.path.join(dir_,".gitkeep"),"w") as f:

 files  =  [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",  #the file which contains all the files which are not get pushed and ignored.
     os.path.join("src","__init__.py") #to make sure the python package as a source file.
 ]

for file_ in files: 
    with open(file_,"w") as f:
        pass
