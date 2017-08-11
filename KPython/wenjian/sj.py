import os

def sj(rootDir,outPutFile):
    fw = open(outPutFile,'w')

    for dirName in os.listdir(rootDir):
        if os.path.isdir(os.path.join(rootDir,dirName)):
            print 'process in dir:%s'%dirName
            for fileName in os.listdir(os.path.join(rootDir,dirName)):
                if os.path.isfile(os.path.join(rootDir,os.path.join(dirName,fileName))):
                    fr = open(os.path.join(rootDir,os.path.join(dirName,fileName)),'r')
                    for eachLine in fr:
                        fw.write(eachLine)
                    fr.close()

    fw.close()

sj('mydir','newfile.txt')
