import os,time,glob,sys
from elements import *

def TAB(num):
    #TAB(int num)
    #num: number of indentations
    #return: a string of whitespace of length num*4
    #Generates a string of num tabs, for formatting the generated HTML nicely

    return ('    '*num)

def log(msg):
    #string msg: message to print to logfile

    #os.system("echo '"+msg+"' >> "+AROOT+"log.txt")
    print "opening logfile for writing"
    logfile = open(AROOT+"log.txt","w")
    print "writing '"+msg+"'"
    logfile.write(msg+'\n')
    print "closing file"
    logfile.close()

def getJobID(all_elements):
    jobStr = ''.join([str(t.getState()) for t in all_elements])
    jobID = str(int(sum([(ord(jobStr[i])-45)*i for i in range(len(jobStr))])))
    return jobID

def makeConfig(test_boxes):
    #makeConfig(List boxes, List radios, List texts)
    #expids: list of experiment ids to include in the config file
    #return: the job ID associated with the submission
    #Generates and writes the configuration file for the given set of parameters

    #Open the file itself
    log("Attempting to open "+MATH+CONFIG+" for writing")

    try:
        configFile = open(MATH+CONFIG,'w+')
        #Write the version of the Mathematica script
        configFile.write("#Version %s\n"%VERSION)
        #Write the timestamp
        configFile.write(time.strftime("#%X %x\n\n"))

        #Generate the job ID
        all_elements = test_boxes

        jobID = getJobID(all_elements)

        #Job ID
        configFile.write("Job ID: %s\n"%jobID)

        flagstr = ""
        for box in test_boxes:
            flagstr += "     %d"%box.getState()
        configFile.write("Boxes checked:%s\n\n"%(flagstr[3:]))

        configFile.close()
        log("Successfully wrote config file")
    except:
        log("Failed with "+sys.exc_info()[0].__name__)
        raise

    return jobID

def makeGraph(jobID):
    #makeGraph(string jobID)
    #jobID: the ID of the job that is invoking the Mathematica script
    #Make a lockfile, invoke the Mathematica script, wait until the graph has been generated, and display it

    log("Generating graphs")

    #Create lockfile containing job ID of the image being generated
    log("Attempting to open "+MATH+"lock for writing")

    try:
        lockfile = file(MATH+'lock','w+')
        lockfile.write("%s\n%s\n%s\n%s\n"%(jobID,time.strftime("%X %x"),os.environ["REMOTE_ADDR"],os.environ['HTTP_USER_AGENT']))#Write job ID, time and date of creation, invoking host ip, and user agent 
        lockfile.close()
    except:
        log("Failed with "+sys.exc_info()[0].__name__)
        raise

    log("Successfully wrote lock file")

    #Invoke the program
    log("Running script at "+MATH+"test_script.sh")
    os.system(MATH+"test_script.sh&")

    #Check every 2 seconds to see if the graph is done being generated, and display it when it is
    path = JS_PREFIX+OUTPUT+jobID+IMAGE

    log("Waiting for script to finish generating images")
    print TAB(2)+"<h3 id='graph'>Loading...<h3/><br/>\n"
    #print TAB(2)+"""<script>var loop = setInterval(function() { if (UrlExists("%s")) { clearInterval(loop); document.getElementById('graph').src = "%s"; }; }, 2000);</script>"""%(path,path)
    print TAB(2)+"""<script>var loop = setInterval(function() { if (UrlExists("%s")) { clearInterval(loop); document.getElementById('graph').innerHTML = "<a onclick='window.location.reload()'>Click to view plots</a>"; }; }, 2000);</script>"""%(path)
