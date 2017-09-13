# physics-research
Code I'm writing as an undergraduate physics research assistant at Southern Methodist University<br/><br/>

The webpage will provide lots of input fields for different variables, which when submitted will be passed to a Mathematica program that will generate a graph, and the graph will then be displayed.<br/><br/>

I am using the "Material Design Lite" framework from Google for making the input fields, and writing the backend using the Python CGI module.<br/><br/>

When boxes are checked and the 'submit' button is pressed, a configuration file is written at HEAD/mathscript_v17/bin/config1.txt using the options selected. It then checks for the existence of a lockfile at HEAD/mathscript_v17/bin/lock, which is generated every time a job is run. If the lockfile is already there, it reads it and checks to see if that job has completed, and just waits until it has. If the previous job is done, it writes to the lockfile with the new job ID and calls the script, which in this test is at HEAD/mathscript_v17/bin/test_script.sh. It then waits for the images to be generated, and notifies the user the job has completed.<br/><br/>

The problem we've been having is with read/write permissions on the config file and lock file. The whole appplication runs perfectly when I test it on my local system,