import os 
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-p', dest='pathToSearch', type='string', help='specify path where to search')
parser.add_option('-s', dest='whatToSearch', type='string', help='specify where to search, content or name')

(options, args) = parser.parse_args()


if options.pathToSearch:	
	pathToSearch = options.pathToSearch
else:
    print("-p is missing - specify path where to search")
    exit()

if options.whatToSearch:	
	whatToSearch = options.whatToSearch
else:
    print("-s is missing - specify where to search, content or name")
    exit()

def get_dirs(base_path):
	dirs = []
	for file in os.listdir(base_path):
		if os.path.isdir(base_path+"\\"+file):
			dirs.append(base_path+"\\"+file)

	return dirs

def TestingFilesForInterestingContent(pathInPathToShearch):
    dirlist = os.listdir(pathInPathToShearch)
    interestingFiles = [] # Empty list 
    for x in dirlist: # Browsing on all files in list
        if not(os.path.isdir(pathInPathToShearch+'\\'+x)):  # Its file ?
            f = open(pathInPathToShearch+'\\'+x, 'rb') # read
            content = f.read()
            for y in interestingContent: # check file content against keys
                if y.encode() in content.lower():
                    
                    #print (shareDir+"\\"+x)
                    interestingFiles.append(pathInPathToShearch+"\\"+x) # write to list
                    
    interestingFiles = set(interestingFiles) # Unique 
    return interestingFiles

def TestingFilesForInterestingName(pathInPathToShearch):
    dirlist = os.listdir(pathInPathToShearch)
    interestingFiles = [] # Empty list 
    for x in dirlist: # Browsing on all files in list
        for y in interestingContent: # check file content against keys
            if y in x.lower():
                #print (shareDir+"\\"+x)
                interestingFiles.append(pathInPathToShearch+"\\"+x) # write to list
                    
    interestingFiles = set(interestingFiles) # Unique 
    return interestingFiles  

interestingContent = []
f = open("ToSearch.txt", "r")
for x in f:
    #print(x.replace("\n","").replace("\r",""))
    x = x.replace("\n","").replace("\r","")
    interestingContent.append(x)
f.close()

dirs0 = get_dirs(pathToSearch)

for dir0 in dirs0:
	for dir1 in get_dirs(dir0):
		dirs0.append(dir1)
dirs0.append(pathToSearch)	


for pathInPathToShearch in dirs0:
    if whatToSearch == 'filecontent':
        interestingFiles = TestingFilesForInterestingContent(pathInPathToShearch)
    else:
        interestingFiles = TestingFilesForInterestingName(pathInPathToShearch)
    f = open("output.txt", "a")
    for z in interestingFiles: 
        print (z)
        f.write(z+"\n")
    f.close()
