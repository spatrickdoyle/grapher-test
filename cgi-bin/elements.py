import mdl,os

VERSION = '17' #Version of the Mathematica script
MATH = './' #Path to Mathematica script bin
EXPIDS = 'exptidname_inconfig.txt'
CONFIG = 'config1.txt' #Name of config file to be generated in the Mathematica script bin directory
JS_PREFIX = '../mathscript_v%s/bin/'%VERSION
OUTPUT = '../plots/Jobs/' #Path to output directory - the script will create a separate  folder here for each unique job ID
ASSETS = '../assets/' #Path to HTML page assets
IMAGE = '/test_image2.png'
#CWD = "/home/sean/Programs/git-repos/physics-research/mathscript_v%s/bin"%VERSION
CWD = "./mathscript_v%s/bin/"%VERSION

#os.chdir(CWD)

#Test checkboxes
test_boxes = [mdl.CheckBox(str(i),str(i),False,'test') for i in range(4)]

#Buttons
buttons = [
    mdl.Button('button1','SUBMIT'), #[0]
    mdl.Button('button2','RESET','resetbutton') #[1]
]

all_elements = test_boxes
