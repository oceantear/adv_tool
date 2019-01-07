import sys,os
from optparse import OptionParser, make_option
from datetime import datetime

tool_version = "1.0"

bcolors = {"RED" : '\033[91m',
           "BLUE": '\033[94m',
           "HIGH": '\033[93m',
           "BOLD": '\033[1m',
           "LINE": '\033[4m',
           "ENDC": '\033[0m'
           
           } 


def parseLog(path):
    with open(options.FileName) as f:
            for line in f:
                if line.find("secs:") != -1 and line.find("secs:") !=5:
                    time = line.split(":")[1]
                    #print bcolors["RED"] + line.split(":")[0] + ":"+ datetime.utcfromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
                    print line.split(":")[0] + ":"+ datetime.utcfromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
                elif line.find("msg:") != -1 :
                    #st = line.rstrip()
                    #print bcolors["BLUE"] + st.split(":")[0] +bcolors["ENDC"] + ":"+ st.split(":")[1]
                    print line.rstrip()


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

    options, args = optParser.parse_args()

    currentPath = os.getcwd()+ "/"

    
    if options.FileName != None :
        if os.path.isfile(options.FileName) :
            parseLog(options.FileName)
        elif os.path.isfile(currentPath + options.FileName):
            parseLog(currentPath + options.FileName)
        else:
            print "Error: file not exist"
    
            


    
   
    