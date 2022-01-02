import uuid
import subprocess

def createfile(lang,code):
    filename = str(uuid.uuid4()) + "." + lang
    with open("code/"+filename , "w") as f:
        f.write(code)
    return filename


def execute_file(file_name,lang):
    if lang == "cpp":
        res=subprocess.run(["g++","code/"+file_name],stdout=subprocess.PIPE)
        # print(res.stdout,res.returncode,sep="                 ")
#     compile err using return code
        if res.returncode != 0 :
            return
        res = subprocess.run(["./a.exe"],stdout=subprocess.PIPE)
        if res.returncode != 0 :
            return
        return res.stdout
