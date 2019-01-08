#!/usr/bin/python
from __future__ import division
import sys,os
from optparse import OptionParser, make_option
from datetime import datetime
import subprocess
from subprocess import Popen, PIPE, STDOUT


tool_version = "1.0"
match_time = False

bcolors = {"RED" : '\033[91m',
           "BLUE": '\033[94m',
           "HIGH": '\033[93m',
           "BOLD": '\033[1m',
           "LINE": '\033[4m',
           "ENDC": '\033[0m'
           
           } 

def fileLines(path):

    p = subprocess.Popen('wc -l ' +path, shell=True, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    out , err = p.communicate()

    print out.split()[0]
    return out.split()[0]

def parseLog(path ):
    i = 0
    with open(options.FileName) as f:
            for line in f:
                i += 1
                if line.find("secs:") != -1 and line.find("secs:") !=5:
                    time = line.split(":")[1]
                    if options.Time != None:

                        if datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S').find(options.Time) != -1:
                            print line.split(":")[0] + ": "+ datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')                        
                            match_time = True
                        else:
                            #print filelines
                            #percent = int(i) / int(filelines)*100
                            #print i,filelines,percent
                            #print "Serching file  [%d%%]\r" %percent,
                           
                            match_time = False
                    else:
                        #print bcolors["RED"] + line.split(":")[0] + ":"+ datetime.utcfromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
                        print line.split(":")[0] + ": "+ datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
                elif line.find("msg:") != -1 :
                    #st = line.rstrip()
                    #print bcolors["BLUE"] + st.split(":")[0] +bcolors["ENDC"] + ":"+ st.split(":")[1]
                    if options.Time != None:
                        if match_time == True:
                            print line.rstrip()

                        match_time = False
                    else:
                        print line.rstrip()
            else:
                print "End of File"


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print "Error: Need more input parameters"

    optParser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog "+tool_version)
    
    optParser.add_option("-f",
                         "--file",
                         action = "store",
                         type = "string",
                         dest = "FileName",
                         help = "input file name,relative path or absolute path")
    
    optParser.add_option("-t",
                         "--time",
                         action = "store",
                         type = "string",
                         dest = "Time",
                         help = "time filter, for example: YYYY-MM-DD")

    options, args = optParser.parse_args()

    currentPath = os.getcwd()+ "/"

    #if options.Time != None :
    #    print  options.Time ,options.FileName
    
    if options.FileName != None :
        if os.path.isfile(options.FileName) :
            #filelines = fileLines(options.FileName)
            
            parseLog(options.FileName )
        elif os.path.isfile(currentPath + options.FileName):
            #filelines = fileLines(options.FileName)
            parseLog(currentPath + options.FileName)
        else:
            print "Error: file not exist"
    
            


    
   
    