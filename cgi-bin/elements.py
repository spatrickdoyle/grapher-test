import mdl,os

VERSION = '17' #Version of the Mathematica script
RROOT = '../' #Relative root, use for links
AROOT = '/htdocs/seand/' #Absolute root, use for file accessing
AMATH = AROOT+'mathscript_v%s/bin/'%VERSION #Path to Mathematica script bin
RMATH = RROOT+'mathscript_v%s/bin/'%VERSION#Relative path to Mathematica script bin
ASSETS = RROOT+'assets/' #Path to HTML page assets
AOUTPUT = AROOT+'mathscript_v%s/plots/Jobs/'%VERSION #Path to output directory - the script will create a separate  folder here for each unique job ID
ROUTPUT = RROOT+'mathscript_v%s/plots/Jobs/'%VERSION

EXPIDS = 'exptidname_inconfig.txt'
CONFIG = 'config1.txt' #Name of config file to be generated in the Mathematica script bin directory
IMAGE = '/test_image2.png'

#Test checkboxes
test_boxes = [mdl.CheckBox(str(i),str(i),False,'test') for i in range(4)]

#Buttons
buttons = [
    mdl.Button('button1','SUBMIT'), #[0]
    mdl.Button('button2','RESET','resetbutton') #[1]
]

all_elements = test_boxes
