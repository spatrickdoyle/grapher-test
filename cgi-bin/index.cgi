#!/usr/bin/env python2

#CGI script for testing the LHC graphing application
#Written by Sean Doyle in 2017 for the Southern Methodist University theoretical physics research lab

# Import module for CGI handling 
import cgi

#Object wrappers for Google Material Design components
import mdl

#For debugging - remove or comment when complete
import cgitb
cgitb.enable()

#Other things
import glob,os,time

#Mathscript interface
from mathscript import *


#os.chdir(AROOT)


#Create all the input elements that will be on the page

log("Loading HTML page "+time.asctime())
log("Current working directory is "+os.getcwd())

#Get data from submitted form
form = cgi.FieldStorage()

#Print packet header
print "Content-type:text/html\r\n"

#The HTML bit
#Source file head
print "<html>"

print TAB(1)+"<head>"
print TAB(2)+"<title>Physics test page</title>\n"

#Google Material Design stylesheets
print TAB(2)+"<link rel='stylesheet' href='%sct66.css'>"%ASSETS
print TAB(2)+"<link rel='stylesheet' href='%smdl/material.min.css'>"%ASSETS
print TAB(2)+"<script src='%smdl/material.min.js'></script>"%ASSETS
print TAB(2)+"<link rel='stylesheet' href='%smdl/icon.css'>"%ASSETS

#Other resources
print TAB(2)+"<link rel='stylesheet' href='%sindex.css'>"%ASSETS
print TAB(2)+"<script src='%sindex.js'></script>"%ASSETS

print TAB(1)+"</head>"

print TAB(1)+"<body>"
print os.getcwd()
print TAB(2)+"<h1>LHC Grapher Test</h1>"
print TAB(2)+"<h2>Southern Methodist University Physics Department</h2>\n"

#Update input elements based on previous form submission
if len(form) != 0:
    for element in all_elements:
        element.checkState(form)

#Generate the actual HTML form and draw all the input elements

print TAB(2)+'<form action="index.cgi" method="post" style="display:inline" id="theForm">'

print TAB(3)+'<table>'

#Experiment IDs
print TAB(5)+'<td>'
print TAB(6)+'Some test elements:<br/>'

print TAB(6)+'<table>'

print TAB(7)+'<tr>'
print TAB(8)+'<td style="width:20%;border:none">'
for box in test_boxes:
    box.draw(9)
    print TAB(9)+'<br/>'
print TAB(8)+'</td>'
print TAB(7)+'</tr>'

print TAB(6)+'</table>'

print TAB(5)+'</td>'
print TAB(4)+'</tr>'
print TAB(3)+'</table>\n'


#Reset and submit buttons
print "<br/>"
buttons[0].draw(2)
print "&nbsp;"
print TAB(2)+'</form>'
buttons[1].draw(2)
print TAB(2)+'<br/><br/><br/>\n'

#The complicated part
#If a form has been submitted - this not is the first time the page is being loaded
if len(form) != 0:

    #Write the Mathematica configuration file
    jobID = getJobID(test_boxes)

    #Check if the graph being requested has already been generated and stored

    #Check if the plot is there
    path = ROUTPUT+jobID
    images = sorted(glob.glob(path[1:]+"/*.png"))

    log("Writing configuration file")
    makeConfig(test_boxes)

    if len(images) != 0:
        #If it is, display and nicely format the generated images
        log("Displaying generated graphs\n")
        print "<a href='%s'>Download configuration file</a>"%(RMATH+CONFIG)

        print "<table style='width:100%'><tr>"
        for image in images:
            print "<td style='text-align:center;width:3000px;border:none'>"
            print TAB(2)+"<img style='width:100%;max-width:800px' src='."+image+"'/><br/>\n"
            print "<a href='."+image+"'>View full image</a></td>"
        print "</tr><br/><tr>"
        print "</tr></table>"
    else:
        #Check for the presence of the lockfile
        log("Checking if lockfile exists")
        present = glob.glob(AMATH+"lock")
        if len(present) == 0:
            #If it isn't there, run the program
            makeGraph(jobID)
        else:
            #Otherwise, read the job ID of the lockfile
            log("Attempting to open "+AMATH+"lock for reading")

            try:
                lockfile = file(AMATH+'lock','r')
                prevID = lockfile.readline()[:-1]
                lockfile.close()
            except:
                log("Failed with "+sys.exc_info()[0].__name__)
                raise

            log("Successfully read lock file")

            #See if an output with the corresponding ID already exists, and if it does, delete the lockfile and generate the new graph
            prevPath = (ROUTPUT+prevID+IMAGE)
            if len(glob.glob(prevPath[1:])) != 0:
                os.system('rm '+AMATH+'lock')
                makeGraph(jobID)
            else:
                #If not, assume another process is running and wait until an output with the lockfile ID has been generated, then reload the page
                log("Waiting for previous job to finish")
                print TAB(2)+"<h3 id='graph'>Waiting for another request to finish...</h3><br/>\n"
                print TAB(2)+'<script>var loop = setInterval(function() { if (UrlExists("%s")) { clearInterval(loop); location.reload();} }, 3000);</script>'%(prevPath)

else:
    #If the page IS being loaded for the first time...
    print TAB(2)+"Plots will be displayed here<br/><br/>\n"

print TAB(1)+'</body>'
print '</html>'
