#config
file_path = 'req_packages.txt'#path to the requirements list
main_script = 'path here'#the path to your main code (eg. file\\file.py or file.py)
main_script_name="name here"#the name of the file
TitleText="Your Title Here"
#



requireTQDM_INSTALL=False
try:
    import tqdm
    print("tqdm is installed")
except ImportError:
    print("tqdm is not installed. installing now...")
    requireTQDM_INSTALL=True
from colorama import init, Fore, Style
init()
import time
import subprocess
import sys
import importlib.util
if requireTQDM_INSTALL==True:
    process = subprocess.Popen(
          [sys.executable, "-m", "pip", "install", "tqdm", "--progress-bar", "off"],
           stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          universal_newlines=True,
     )
from tqdm import tqdm
import threading
import importlib.util
def install_package(package_name):
     process = subprocess.Popen(
          [sys.executable, "-m", "pip", "install", package_name, "--progress-bar", "off"],
           stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          universal_newlines=True,
     )
    
     def read_output(pipe):
            for line in iter(pipe.readline, ''):
                tqdm.write(line.strip())
            pipe.close()
    
     stdout_thread = threading.Thread(target=read_output, args=(process.stdout,))
     stderr_thread = threading.Thread(target=read_output, args=(process.stderr,))
     stdout_thread.start()
     stderr_thread.start()

     with tqdm(total=1, bar_format="{l_bar}{bar} | {elapsed}", ncols=100, desc=Fore.YELLOW+f"Installing {package_name}"+Style.RESET_ALL) as pbar:
        while process.poll() is None:
            time.sleep(0.1)
            pbar.update(0)

     stdout_thread.join()
     stderr_thread.join()
     process.wait()

def install():
    
    # Example usage:
    file_path = 'req_packages.txt'
    try:
        with open(file_path, 'r') as file:
          packages = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
      print(Fore.RED+f"The file {file_path} was not found."+Style.RESET_ALL)
      packages = []


    for package in packages:
      print(Fore.GREEN + f"Starting installation of {package}..."+ Style.RESET_ALL)
      install_package(package)
      print(Fore.CYAN+f"Finished installing {package}."+Style.RESET_ALL)

    print(Fore.CYAN+"All packages installed."+Style.RESET_ALL)
    #

print(TitleText)
print(Fore.BLUE+"Awaiting Input..."+Style.RESET_ALL)
isdone=False
while isdone==False:
    inputed=input()
    if inputed=="help":
        print("Help : Shows This Menu\nStart : Start The Program\nI_req : install required files\nClose : closes the program")
    if inputed=="Start":
        print(Fore.LIGHTMAGENTA_EX+"Starting Up..."+Style.RESET_ALL)
        isdone=True
    if inputed=="I_req":
        print(Fore.GREEN+"Starting Install..."+Style.RESET_ALL)
        install()
        print(Fore.YELLOW+"Do you want to start the program?"+Style.RESET_ALL)
        if input()=="y" or input()=="yes":
            isdone=True
   

try :
    spec = importlib.util.spec_from_file_location(main_script_name, main_script)
    module = importlib.util.module_from_spec(spec)
    sys.modules[main_script_name] = module
    spec.loader.exec_module(module)
     
except :
    print(Fore.RED+"Error Running The Program!"+Style.RESET_ALL)
else:
    print(Fore.RED+"Program Stopped!"+Style.RESET_ALL)    
    

