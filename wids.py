#! /usr/bin/python
#
# This was written for educational purpose only. Use it at your own risk.
# Author will be not responsible for any damage!
# Written By SY Chua, syworks@gmail.com
#

appver="1.0, R.2"
apptitle="WIDS"
appDesc="- The Wireless Intrusion Detection System"
appcreated="07 Jan 2014"
appupdated="17 Jan 2014"
appnote="by SY Chua, " + appcreated + ", Updated " + appupdated


import httplib
import sys
import requests
import sys,os
import subprocess
import random
import curses
from subprocess import call
import termios
import tty
import time
import signal
import select 
import datetime
import urllib2
import ssl
import os.path
import binascii, re
import commands
from subprocess import Popen, PIPE
import threading

##################################
#  Global Variables Declaration  #
##################################
global RTY
RTY=""

def CheckAdmin():
    is_admin = os.getuid() == 0
    if is_admin==False:
        printc ("!!!","Application required admin rights in-order to work properly !","")
        exit(1)

class fcolor:
    CReset='\033[0m'
    CBold='\033[1m'
    CDim='\033[2m'
    CUnderline='\033[4m'
    CBlink='\033[5m'
    CInvert='\033[7m'
    CHidden='\033[8m'
    CDebugB='\033[1;90m'
    CDebug='\033[0;90m'
    Black='\033[30m'
    Red='\033[31m'
    Green='\033[32m'
    Yellow='\033[33m'
    Blue='\033[34m'
    Pink='\033[35m'
    Cyan='\033[36m'
    White='\033[37m'
    SBlack='\033[0;30m'
    SRed='\033[0;31m'
    SGreen='\033[0;32m'
    SYellow='\033[0;33m'
    SBlue='\033[0;34m'
    SPink='\033[0;35m'
    SCyan='\033[0;36m'
    SWhite='\033[0;37m'
    BBlack='\033[1;30m'
    BRed='\033[1;31m'
    BBlue='\033[1;34m'
    BYellow='\033[1;33m'
    BGreen='\033[1;32m'
    BPink='\033[1;35m'
    BCyan='\033[1;36m'
    BWhite='\033[1;37m'
    UBlack='\033[4;30m'
    URed='\033[4;31m'
    UGreen='\033[4;32m'
    UYellow='\033[4;33m'
    UBlue='\033[4;34m'
    UPink='\033[4;35m'
    UCyan='\033[4;36m'
    UWhite='\033[4;37m'
    BUBlack=CBold + '\033[4;30m'
    BURed=CBold + '\033[4;31m'
    BUGreen=CBold + '\033[4;32m'
    BUYellow=CBold + '\033[4;33m'
    BUBlue=CBold + '\033[4;34m'
    BUPink=CBold + '\033[4;35m'
    BUCyan=CBold + '\033[4;36m'
    BUWhite=CBold + '\033[4;37m'
    IGray='\033[0;90m'
    IRed='\033[0;91m'
    IGreen='\033[0;92m'
    IYellow='\033[0;93m'
    IBlue='\033[0;94m'
    IPink='\033[0;95m'
    ICyan='\033[0;96m'
    IWhite='\033[0;97m'
    BIGray='\033[1;90m'
    BIRed='\033[1;91m'
    BIGreen='\033[1;92m'
    BIYellow='\033[1;93m'
    BIBlue='\033[1;94m'
    BIPink='\033[1;95m'
    BICyan='\033[1;96m'
    BIWhite='\033[1;97m'
    BGBlack='\033[40m'
    BGRed='\033[41m'
    BGGreen='\033[42m'
    BGYellow='\033[43m'
    BGBlue='\033[44m'
    BGPink='\033[45m'
    BGCyan='\033[46m'
    BGWhite='\033[47m'
    BGIBlack='\033[100m'
    BGIRed='\033[101m'
    BGIGreen='\033[102m'
    BGIYellow='\033[103m'
    BGIBlue='\033[104m'
    BGIPink='\033[105m'
    BGICyan='\033[106m'
    BGIWhite='\033[107m'



def read_a_key():
    stdinFileDesc = sys.stdin.fileno()
    oldStdinTtyAttr = termios.tcgetattr(stdinFileDesc)
    try:
        tty.setraw(stdinFileDesc)
        sys.stdin.read(1)
    finally:
        termios.tcsetattr(stdinFileDesc, termios.TCSADRAIN, oldStdinTtyAttr)

def printc(ptype, ptext,ptext2):
    """
    Function	   : Displaying text with pre-defined icon and color
    Usage of printc:
        ptype      - Type of Icon to display
        ptext      - First sentence to display
        ptext2     - Second sentence, "?" as reply text, "@"/"@^" as time in seconds
    Examples       : Lookup DemoOnPrintC() for examples
    """

    ScriptName=os.path.basename(__file__)
    printd("PType - " + str(ptype) + "\n       " + "PText = " + str(ptext) + "\n       " + "PText2 = " + str(ptext2))
    ReturnOut=""
    bcolor=fcolor.SWhite
    if ptype=="i":
        pcolor=fcolor.BBlue
        tcolor=fcolor.BWhite
    if ptype=="H":
        pcolor=fcolor.BBlue
        tcolor=fcolor.BWhite
        hcolor=fcolor.BUBlue
    if ptype=="!":
        pcolor=fcolor.BRed
        tcolor=fcolor.BYellow
    if ptype=="!!":
        ptype="!"
        pcolor=fcolor.BRed
        tcolor=fcolor.SRed
    if ptype=="!!!":
        ptype="!"
        pcolor=fcolor.BRed
        tcolor=fcolor.BRed
    if ptype==".":
        pcolor=fcolor.BGreen
        tcolor=fcolor.SGreen
    if ptype=="-":
        pcolor=fcolor.SWhite
        tcolor=fcolor.SWhite
    if ptype=="--":
        ptype="-"
        pcolor=fcolor.BWhite
        tcolor=fcolor.BWhite
    if ptype=="..":
        ptype="."
        pcolor=fcolor.BGreen
        tcolor=fcolor.BGreen
    if ptype==">" or ptype=="+":
        pcolor=fcolor.BCyan
        tcolor=fcolor.BCyan
    if ptype==" ":
        pcolor=fcolor.BYellow
        tcolor=fcolor.Green
    if ptype=="  ":
        pcolor=fcolor.BYellow
        tcolor=fcolor.BGreen
    if ptype=="?":
        pcolor=fcolor.BYellow
        tcolor=fcolor.BGreen
    if ptype=="x":
        pcolor=fcolor.BRed
        tcolor=fcolor.BBlue
    if ptype=="*":
        pcolor=fcolor.BYellow
        tcolor=fcolor.BPink
    if ptype=="@" or ptype=="@^":
        pcolor=fcolor.BRed
        tcolor=fcolor.White

    if ptext!="":
        tscolor=fcolor.Blue
        ts = time.time()
        DateTimeStamp=datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')
        TimeStamp=datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        DateStamp=datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y')
        ptext=ptext.replace("%dt -",tscolor + DateTimeStamp + " -" + tcolor)
        ptext=ptext.replace("%dt",tscolor + DateTimeStamp + tcolor)
        ptext=ptext.replace("%t -",tscolor + TimeStamp + " -" + tcolor)
        ptext=ptext.replace("%t",tscolor + TimeStamp + tcolor)
        ptext=ptext.replace("%d -",tscolor + DateStamp + " -" + tcolor)
        ptext=ptext.replace("%d",tscolor + DateStamp + tcolor)
        ptext=ptext.replace("%an",tscolor + ScriptName + tcolor)
        if "%cs" in ptext:
            ptext=ptext.replace("%cs",tscolor + ptext2 + tcolor)
            ptext2=""
        lptext=len(ptext) 
        if lptext>6:
            firstsix=ptext[:6].lower()
            if firstsix=="<$rs$>":
                ReturnOut="1"
                lptext=lptext-6
                ptext=ptext[-lptext:]
    if ptype=="x":
        if ptext=="":
            ptext="Press Any Key To Continue..."
        c1=bcolor + "[" + pcolor + ptype + bcolor + "]  " + tcolor + ptext
        print c1,
        sys.stdout.flush()
        read_a_key()
        print ""
        return
    if ptype=="H":
        c1=bcolor + "[" + pcolor + "i" + bcolor + "]  " + hcolor + ptext + fcolor.CReset 
        if ReturnOut!="1":
            print c1
            return c1
        else:
            return c1
    if ptype=="@" or ptype=="@^":
        if ptext2=="":
            ptext2=5
        t=int(ptext2)
        while t!=0:
            s=bcolor + "[" + pcolor + str(t) + bcolor + "]  " + tcolor + ptext + "\r"
            s=s.replace("%s",pcolor+str(ptext2)+tcolor)
            sl=len(s)
            print s,
            sys.stdout.flush()
            time.sleep(1)
            s=""
            ss="\r"
            print "" + s.ljust(sl+2) + ss,
            sys.stdout.flush()
            if ptype=="@^":
                t=t-1
                while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    line = sys.stdin.readline()
                    if line:
                        print bcolor + "[" + fcolor.BRed + "!" + bcolor + "]  " + fcolor.Red + "Interupted by User.." + fcolor.Green
                        return
            else:
                t=t-1            
        c1=bcolor + "[" + pcolor + "-" + bcolor + "]  " + tcolor + ptext + "\r"
        c1=c1.replace("%s",pcolor+str(ptext2)+tcolor)
        print c1,
        sys.stdout.flush()
        return
    if ptype=="?":
        if ptext2!="":
            usr_resp=raw_input(bcolor + "[" + pcolor + ptype + bcolor + "]  " + tcolor + ptext + " ( " + pcolor + ptext2 + tcolor + " ) : " + fcolor.BWhite)
            return usr_resp;
        else:
            usr_resp=raw_input(bcolor + "[" + pcolor + ptype + bcolor + "]  " + tcolor + ptext + " : " + fcolor.BWhite)
            return usr_resp;
    if ptype==" " or ptype=="  ":
        if ReturnOut!="1":
            print bcolor + "     " + tcolor + ptext + ptext2
        else:
            return bcolor + "     " + tcolor + ptext + ptext2
    else:
        if ReturnOut!="1":
            print bcolor + "[" + pcolor + ptype + bcolor + "]  " + tcolor + ptext + ptext2
        else:
            return bcolor + "[" + pcolor + ptype + bcolor + "]  " + tcolor + ptext + ptext2

def AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply):
    """
    Function	        : Question for user input. Quite similar to printc("?") function
    Usage of AskQuestion:
        QuestionText    - Question Text to ask
        ReplyText       - The reply text. Ex : "Y/n")
    Examples            : Lookup DemoOnPrintC() for examples
    """
    if DisplayReply=="":
        DisplayReply=1

    bcolor=fcolor.SWhite
    pcolor=fcolor.BYellow
    tcolor=fcolor.BGreen
    if ReplyText!="":
        usr_resp=raw_input(bcolor + "[" + pcolor + "?" + bcolor + "]  " + tcolor + QuestionText + " ( " + pcolor + ReplyText + tcolor + " ) : " + fcolor.BWhite)
    else:
        usr_resp=raw_input(bcolor + "[" + pcolor + "?" + bcolor + "]  " + tcolor + QuestionText + " : " + fcolor.BWhite)

    if DefaultReply!="":
        if usr_resp=="":
            if DisplayReply=="1":
                printc (" ",fcolor.SWhite + "Default Selected ==> " + fcolor.BYellow + str(DefaultReply),"")   
            return DefaultReply
        else:
            if ReplyType=="U":
               if DisplayReply=="1":
                   printc (" ",fcolor.SWhite + "Selected ==> " + fcolor.BYellow + str(usr_resp.upper()),"")   
               return usr_resp.upper()
            if ReplyType=="FN":
               if os.path.isfile(usr_resp)==True:
                   if DisplayReply=="1":
                       printc (" ",fcolor.SWhite + "Filename ==> " + fcolor.BYellow + str(usr_resp),"")   
                   return usr_resp
               else:
                   printc ("!!","Filename [" + fcolor.SYellow + usr_resp + fcolor.SRed + "] does not exist !.","")
                   usr_resp=AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply)
                   return usr_resp;
            if ReplyType=="FP":
               if os.path.exists(usr_resp)==True:
                   if DisplayReply=="1":
                       printc (" ",fcolor.SWhite + "Path ==> " + fcolor.BYellow + str(usr_resp),"")   
                   return usr_resp
               else:
                   printc ("!!","Filename/Pathname [" + fcolor.SYellow + usr_resp + fcolor.SRed + "] does not exist !.","")
                   usr_resp=AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply)
                   return usr_resp;
            if ReplyType=="PN":
               if os.path.isdir(usr_resp)==True:
                   if usr_resp[-1:]!="/":
                       usr_resp=usr_resp + "/"
                   if DisplayReply=="1":
                       printc (" ",fcolor.SWhite + "Path ==> " + fcolor.BYellow + str(usr_resp),"")   
                   return usr_resp
               else:
                   printc ("!!","Path [" + fcolor.SYellow + usr_resp + fcolor.SRed + "] does not exist !.","")
                   usr_resp=AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply)
                   return usr_resp;
            if ReplyType=="L":
               if DisplayReply=="1":
                   printc (" ",fcolor.SWhite + "Selected ==> " + fcolor.BYellow + str(usr_resp.lower()),"")   
               return usr_resp.lower()
            if ReplyType=="N":
               if usr_resp.isdigit()==True:
                   if DisplayReply=="1":
                       printc (" ",fcolor.SWhite + "Selected ==> " + fcolor.BYellow + str(usr_resp),"")   
                   return usr_resp;
               else:
                   usr_resp=AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply)
                   return usr_resp;
    if DefaultReply=="":
        if usr_resp=="":
            if ReplyText!="":
                usr_resp=raw_input(bcolor + "[" + pcolor + "?" + bcolor + "]  " + tcolor + QuestionText + " ( " + pcolor + ReplyText + tcolor + " ) : " + fcolor.BWhite)
                return usr_resp;
            else:
                if ReplyType=="MA" or ReplyType=="FN" or ReplyType=="PN" or ReplyType=="FP":
                    usr_resp=AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply)
                    return usr_resp;
                else:
                    if DisplayReply=="1":
                        printc (" ",fcolor.SWhite + "Selected ==> " + fcolor.BYellow + str("Nothing"),"")   
                    return usr_resp;
        else:
            if ReplyType=="MN":
               if usr_resp.isdigit()==True:
                   if DisplayReply=="1":
                       printc (" ",fcolor.SWhite + "Selected ==> " + fcolor.BYellow + str(usr_resp),"")   
                   return usr_resp;
               else:
                   usr_resp=AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply)
                   return usr_resp;
            if ReplyType=="FN":
               if os.path.isfile(usr_resp)==True:
                   if DisplayReply=="1":
                       printc (" ",fcolor.SWhite + "Filename ==> " + fcolor.BYellow + str(usr_resp),"")   
                   return usr_resp
               else:
                   printc ("!!","Filename [" + fcolor.SYellow + usr_resp + fcolor.SRed + "] does not exist !.","")
                   usr_resp=AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply)
                   return usr_resp;
            if ReplyType=="PN":
               if os.path.isdir(usr_resp)==True:
                   if usr_resp[-1:]!="/":
                       usr_resp=usr_resp + "/"
                       if DisplayReply=="1":
                           printc (" ",fcolor.SWhite + "Path ==> " + fcolor.BYellow + str(usr_resp),"")   
                   return usr_resp
               else:
                   printc ("!!","Path [" + fcolor.SYellow + usr_resp + fcolor.SRed + "] does not exist !.","")
                   usr_resp=AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply)
                   return usr_resp;
            if ReplyType=="FP":
               if os.path.exists(usr_resp)==True:
                   if os.path.isfile(usr_resp)==True:
                       if DisplayReply=="1":
                           printc (" ",fcolor.SWhite + "Filename ==> " + fcolor.BYellow + str(usr_resp),"")   
                       return usr_resp
                   if os.path.isdir(usr_resp)==True:
                       if usr_resp[-1:]!="/":
                           usr_resp=usr_resp + "/"
                       if DisplayReply=="1":
                           printc (" ",fcolor.SWhite + "Path ==> " + fcolor.BYellow + str(usr_resp),"")   
                       return usr_resp
                   return usr_resp
               else:
                   printc ("!!","Filename/Pathname [" + fcolor.SYellow + usr_resp + fcolor.SRed + "] does not exist !.","")
                   usr_resp=AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply)
                   return usr_resp;

            if ReplyType=="U":
               if DisplayReply=="1":
                   printc (" ",fcolor.SWhite + "Selected ==> " + fcolor.BYellow + str(usr_resp.upper()),"")   
               return usr_resp.upper()
            if ReplyType=="L":
               if DisplayReply=="1":
                   printc (" ",fcolor.SWhite + "Selected ==> " + fcolor.BYellow + str(usr_resp.lower()),"")   
               return usr_resp.lower()
            if ReplyType=="N":
               if usr_resp.isdigit()==True:
                   if DisplayReply=="1":
                       printc (" ",fcolor.SWhite + "Selected ==> " + fcolor.BYellow + str(usr_resp),"")   
                   return usr_resp;
               else:
                   usr_resp=AskQuestion(QuestionText, ReplyText,ReplyType,DefaultReply,DisplayReply)
                   return usr_resp;
    if usr_resp=="":
        if DisplayReply=="1":
            printc (" ",fcolor.SWhite + "Selected ==> " + fcolor.BYellow + str("Nothing"),"")   
        return usr_resp;
    else:
        if DisplayReply=="1":
            printc (" ",fcolor.SWhite + "Selected ==> " + fcolor.BYellow + str(usr_resp),"")   
        return usr_resp;

def printl (DisplayText,ContinueBack,PrevIconCount):
    """
    Function	   : Displaying text on the same line
    Usage of printl:
        DisplayText        - Text to Display
        ContinueBack = "0" - Start DisplayText on beginning of line.
        ContinueBack = "1" - Start from the back of the previous DisplayText
        ContinueBack = "2" - Start DisplayText on beginning of line with Icon,PrevIconCount need to contain value
        PrevIconCount      - Value of last icon count
    Examples       : Lookup DemoOnPrintl() for examples
    """
    icolor=fcolor.BGreen
    bcolor=fcolor.SWhite
    IconDisplay=""
    if ContinueBack=="":
       ContinueBack="0"
    if PrevIconCount=="":
        PrevIconCount="0"
    else:
        PrevIconCount=int(PrevIconCount)+1
    if PrevIconCount>=8:
        PrevIconCount=0
    PrevIconCount=str(PrevIconCount)
    if PrevIconCount=="0":
        IconDisplay="|"
    if PrevIconCount=="1":
        IconDisplay="/"
    if PrevIconCount=="2":
        IconDisplay="-"
    if PrevIconCount=="3":
        IconDisplay="\\"
    if PrevIconCount=="4":
        IconDisplay="|"
    if PrevIconCount=="5":
        IconDisplay="/"
    if PrevIconCount=="6":
        IconDisplay="-"
    if PrevIconCount=="7":
        IconDisplay="\\"
    if ContinueBack=="0":
        curses.setupterm()
        TWidth=curses.tigetnum('cols')
        TWidth=TWidth-1
        sys.stdout.write("\r")
        sys.stdout.flush()
        sys.stdout.write (" " * TWidth + "\r")
        sys.stdout.flush()
        sys.stdout.write(DisplayText)
        sys.stdout.flush()
    if ContinueBack=="1":
        sys.stdout.write(DisplayText)
        sys.stdout.flush()
    if ContinueBack=="2":
        curses.setupterm()
        TWidth=curses.tigetnum('cols')
        TWidth=TWidth-1
        sys.stdout.write("\r")
        sys.stdout.flush()
        sys.stdout.write (" " * TWidth + "\r")
        sys.stdout.flush()
        sys.stdout.write(bcolor + "[" + icolor + str(IconDisplay) + bcolor + "]  " + DisplayText)
        sys.stdout.flush()
    return str(PrevIconCount);

def DrawLine(LineChr,LineColor,LineCount):
    """
    Function	     : Drawing of Line with various character type, color and count
    Usage of DrawLine:
        LineChr      - Character to use as line
        LineColor    - Color of the line
        LineCount    - Number of character to print. "" is print from one end to another
    Examples         : Lookup DemoDrawLine for examples
    """
 
    printd(fcolor.CDebugB + "DrawLine Function\n" + fcolor.CDebug + "       LineChr - " + str(LineChr) + "\n       " + "LineColor = " + str(LineColor) + "\n       " + "LineCount = " + str(LineCount))
    if LineColor=="":
        LineColor=fcolor.SBlack
    if LineChr=="":
        LineChr="_"
    if LineCount=="":
        curses.setupterm()
        TWidth=curses.tigetnum('cols')
        TWidth=TWidth-1
    else:
        TWidth=LineCount
    print LineColor + LineChr * TWidth


def MoveInstallationFiles(srcPath,dstPath):
    import shutil
    listOfFiles = os.listdir(srcPath)
    listOfFiles.sort()
    for f in listOfFiles:
        if f!=".git" and f!=".gitignore":
            srcfile = srcPath + f
            dstfile = dstPath + f
            if f==ScriptName:
                shutil.copy2(srcfile, "/usr/sbin/" + str(ScriptName))
                printd("Copy to " + "/usr/sbin/" + str(ScriptName))
                result=os.system("chmod +x /usr/sbin/" + ScriptName + " > /dev/null 2>&1")
                printd("chmod +x " + "/usr/sbin/" + str(ScriptName))
            if os.path.exists(dstfile):
                os.remove(dstfile)
            shutil.move(srcfile, dstfile)
            print fcolor.SGreen + "        Moving " + fcolor.CUnderline + f + fcolor.CReset + fcolor.SGreen + " to " + dstfile
            if f==ScriptName:
                result=os.system("chmod +x " + dstfile + " > /dev/null 2>&1")
                printd("chmod +x " + str(dstfile))

def GetScriptVersion(cmdScriptName):
    if cmdScriptName=="":
        cmdScriptName=str(os.path.realpath(os.path.dirname(sys.argv[0]))) + "/" + str(os.path.basename(__file__))

    VerStr=""
    findstr="appver=\""
    printd ("Get Version : " + cmdScriptName)
    if os.path.exists(cmdScriptName)==True:
        ps=subprocess.Popen("cat " + cmdScriptName + " | grep '" + findstr + "' | sed -n '1p'" , shell=True, stdout=subprocess.PIPE)	
        VerStr=ps.stdout.read()
        VerStr=VerStr.replace("appver=\"","")
        VerStr=VerStr.replace("\"","")
        VerStr=VerStr.replace("\n","")
        return VerStr;

def GetUpdate(ExitMode):
    if ExitMode=="":
        ExitMode="1"

    github="https://github.com/SYWorks/wireless-ids.git"
    Updatetmpdir="/tmp/git-update/"
    DownloadedScriptLocation=Updatetmpdir + ScriptName
    dstPath=os.getcwd() + "/"
    dstPath=appdir
    dstScript=dstPath + ScriptName

    CurVersion=GetScriptVersion(dstScript)
    printc (".","Retrieving update details ....","")
    result=RemoveTree(Updatetmpdir,"")
    result=os.system("git clone " + github + " " + Updatetmpdir + " > /dev/null 2>&1")
    if result==0:
        printc (" ",fcolor.SGreen + "Package downloaded..","")
        NewVersion=GetScriptVersion(DownloadedScriptLocation)
        if CurVersion!=NewVersion:
            printc ("i","Current Version\t: " + fcolor.BRed + str(CurVersion),"")
            printc ("  ",fcolor.BWhite + "New Version\t: " + fcolor.BRed + str(NewVersion),"")
            Ask=AskQuestion ("Do you want to update ?","Y/n","","Y","")
            if Ask=="y" or Ask=="Y" or Ask=="":
                srcPath=Updatetmpdir
                result=MoveInstallationFiles(srcPath,dstPath)
                result=os.system("chmod +x " + dstScript + " > /dev/null 2>&1")
                result=RemoveTree(Updatetmpdir,"")
                print ""
                printc ("i",fcolor.BGreen + "Application updated !!","")
                printc ("  ",fcolor.SGreen + "Re-run the updated application on [ " + fcolor.BYellow + dstScript + fcolor.SGreen + " ]..","")
                if ExitMode=="1":
                    exit(0)
                else:
                    return
            else:
                printc ("i",fcolor.BWhite + "Update aborted..","")
                result=RemoveTree(Updatetmpdir,"")
        else:
            printc ("i","Your already have the latest version [ " + fcolor.BRed + str(CurVersion) + fcolor.BWhite + " ].","")
            printc ("  ",fcolor.BWhite + "Update aborted..","")
            result=RemoveTree(Updatetmpdir,"")
            if ExitMode=="1":
                exit(0)
            else:
                return
    else:
        printd ("Unknown Error : " + str(result))
        printc ("!!!","Unable to retrieve update !!","")
        if ExitMode=="1":
            exit(1)
        else:
            return


def GetDir(LookupPath):
    """
        Function   : Return the varius paths such as application path, current path and Temporary path
        Example    : 
    """
    import os
    import tempfile
    pathname, scriptname = os.path.split(sys.argv[0])

    if LookupPath=="":
        LookupPath="appdir"
    LookupPath=LookupPath.lower()

    if LookupPath=="curdir":
        result=os.getcwd()
    if LookupPath=="appdir":
       result=os.path.realpath(os.path.dirname(sys.argv[0]))
    if LookupPath=="exedir":
        result=os.path.dirname(sys.executable)
    if LookupPath=="relativedir":
        result=pathname
    if LookupPath=="scriptdir":
        result=os.path.abspath(pathname)
    if LookupPath=="sysdir":
        result=sys.path[0]
    if LookupPath=="pypath":
        result=sys.path[1]
    if LookupPath=="homedir":
        result=os.environ['HOME']
    if LookupPath=="tmpdir":
        result=tempfile.gettempdir()
    if LookupPath=="userset":
        result=appdir



    result=result + "/"

    if result[-2:]=="//":
        result=result[:len(str(result))-1]
    return result;
def CheckLinux():
    """
        Function : Check for Current OS. Exit if not using Linux
    """
    from subprocess import call
    from platform import system
    os = system()
    printd ("Operating System : " + os)
    if os != 'Linux':
        printc ("!!!","This application only works on Linux.","")
        exit(1)


def CheckPyVersion(MinPyVersion):
    """
        Function : Check for current Python Version. 
                   Exit if current version is less than MinPyVersion
    """

    import platform
    PyVersion = platform.python_version()
    printd ("Python Version : " + PyVersion)
    if MinPyVersion!="":
        if MinPyVersion >= PyVersion:
            printc ("!!!",fcolor.BGreen + "Your Python version " + fcolor.BRed + str(PyVersion) + fcolor.BGreen + " may be outdated.","")
            printc ("  ",fcolor.BWhite + "Minimum version required for this application is " + fcolor.BRed + str(MinPyVersion) + fcolor.BWhite + ".","")
            exit(0)

def GetAppName():
    """
        Function : Get Current Script Name
        Return   : ScriptName  = Actual script name
                   DScriptName = For Display
    """

    global ScriptName
    global FullScriptName
    global DScriptName
    ScriptName=os.path.basename(__file__)
    DScriptName="./" + ScriptName
    appdir=os.path.realpath(os.path.dirname(sys.argv[0]))
    FullScriptName=str(appdir) + "/" + str(ScriptName)
    printd("FullScriptName : " + FullScriptName)
    printd("ScriptName : " + str(ScriptName))


def DisplayAppDetail():
    print fcolor.SBlue + "   $$$$$  $  $$  $       $$  $$$$$   $$$$$   $$   $   $$$$$" + fcolor.SYellow + "   / \\"
    print fcolor.SBlue + "  $       $  $$  $   $   $$ $    $$  $   $$  $$  $$  $    " + fcolor.SYellow + "   ( R )"
    print fcolor.SBlue + "   $$$$   $$$$   $   $$  $  $    $$  $$$$$   $$$$     $$$$" + fcolor.SYellow + "    \\_/"
    print fcolor.SBlue + "       $   $$     $ $ $ $$  $    $$  $ $$    $ $$        $$"
    print fcolor.SBlue + "       $  $$      $ $ $$$   $$   $$  $  $$   $  $$        $"
    print fcolor.SBlue + "  $$$$$  $$       $$  $$     $$$$$   $   $$  $   $$  $$$$$ "
    print ""
    print fcolor.BGreen + apptitle + " " + appver + fcolor.SGreen + " " + appDesc
    print fcolor.CReset + fcolor.White + appnote
    print ""


def DisplayDisclaimer():
    printc ("!!!","Legal Disclaimer :- " + fcolor.Red + "FOR EDUCATIONAL PURPOSES ONLY !!","")
    print fcolor.SWhite + "     Usage of this application for attacking target without prior mutual consent is illegal. It is the"
    print fcolor.SWhite + "     end user's responsibility to obey all applicable local, state and  federal laws. Author assume no"
    print fcolor.SWhite + "     liability and are not responsible for any misuse or damage caused by this application."
    print ""

def DisplayDescription():
    printc ("!!!","Description : " + fcolor.Red + "< Beta Release >","")
    print fcolor.SGreen + "     This a a beta release and reliablity of the information might not be totally correct.."
    print fcolor.SWhite + "     This application sniff the surrounding wireless network for any suspicious packets detected such"
    print fcolor.SWhite + "     as high amount of association/authentical packets, suspicious data sent via broadcast address, "
    print fcolor.SWhite + "     unreasonable high amount of deauthentication packets or EAP association packets which in the other"
    print fcolor.SWhite + "     way indicated possible WEP/WPA/WPS attacks found.."
    print ""

def DisplayDetailHelp():
    print fcolor.BGreen + "Usage   : " + fcolor.BYellow + "" + DScriptName + fcolor.BWhite + " [options] " + fcolor.BBlue + "<args>"
    print fcolor.CReset + fcolor.Black + "          Running application without parameter will fire up the interactive mode."
    print ""
    print fcolor.BIPink + "Options:" + fcolor.CReset
    print fcolor.BWhite + "    -h  --help\t\t" + fcolor.CReset + fcolor.White + "- Show basic help message and exit"
    print fcolor.BWhite + "    -hh \t\t" + fcolor.CReset + fcolor.White + "- Show advanced help message and exit"
    print fcolor.BWhite + "        --update\t" + fcolor.CReset + fcolor.White + "- Check for updates"
    print fcolor.BWhite + "        --remove\t" + fcolor.CReset + fcolor.White + "- Uninstall application"
    print ""
    print fcolor.BWhite + "    -i  --iface" + fcolor.BBlue + " <arg>\t" + fcolor.CReset + fcolor.White + "- Set Interface to use"
    print fcolor.BWhite + "    -t  --timeout" + fcolor.BBlue + " <arg>\t" + fcolor.CReset + fcolor.White + "- Duration to capture before analysing the captured data"

    print ""
    print fcolor.BGreen + "Examples: " + fcolor.BYellow + "" + DScriptName + fcolor.BWhite + " --update"
    print fcolor.BGreen + "          " + fcolor.BYellow + "" + DScriptName + fcolor.BWhite + " -i " + fcolor.BBlue + "wlan0" + fcolor.BWhite + " -t " + fcolor.BBlue + "120"+ fcolor.BWhite
    print fcolor.BGreen + "          " + fcolor.BYellow + "" + DScriptName + fcolor.BWhite + " --iface " + fcolor.BBlue + "wlan1" + fcolor.BWhite + " --timeout " + fcolor.BBlue + "20"+ fcolor.BWhite
    print ""
    DrawLine("-",fcolor.CReset + fcolor.Black,"")
    print ""

def DisplayHelp():
    print fcolor.BGreen + "Usage   : " + fcolor.BYellow + "" + DScriptName + fcolor.BWhite + " [options] " + fcolor.BBlue + "<args>"
    print fcolor.CReset + fcolor.Black + "          Running application without parameter will fire up the interactive mode."
    print ""
    print fcolor.BIPink + "Options:" + fcolor.CReset
    print fcolor.BWhite + "    -h  --help\t\t" + fcolor.CReset + fcolor.White + "- Show basic help message and exit"
    print fcolor.BWhite + "    -hh \t\t" + fcolor.CReset + fcolor.White + "- Show advanced help message and exit"
    print ""
    print fcolor.BWhite + "    -i  --iface" + fcolor.BBlue + " <arg>\t" + fcolor.CReset + fcolor.White + "- Set Interface to use"
    print fcolor.BWhite + "    -t  --timeout" + fcolor.BBlue + " <arg>\t" + fcolor.CReset + fcolor.White + "- Duration to capture before analysing the captured data"
    print ""
    print fcolor.BGreen + "Examples: " + fcolor.BYellow + "" + DScriptName + fcolor.BWhite + " --update"
    print fcolor.BGreen + "          " + fcolor.BYellow + "" + DScriptName + fcolor.BWhite + " -i " + fcolor.BBlue + "wlan0" + fcolor.BWhite + " -t " + fcolor.BBlue + "120"+ fcolor.BWhite
    print fcolor.BGreen + "          " + fcolor.BYellow + "" + DScriptName + fcolor.BWhite + " --iface " + fcolor.BBlue + "wlan1" + fcolor.BWhite + " --timeout " + fcolor.BBlue + "20"+ fcolor.BWhite
    print ""
    DrawLine("-",fcolor.CReset + fcolor.Black,"")
    print ""

def GetParameter(cmdDisplay):
    """
   cmdDisplay = "0" : Does not display help if not specified
                "1" : Display help even not specified
                "2" : Display Help, exit if error
    """
    global DebugMode
    global AllArguments
    global SELECTED_IFACE
    SELECTED_IFACE=""
    global SELECTED_MON
    SELECTED_MON=""

    global TIMEOUT
    TIMEOUT=60
    global ASSIGNED_MAC
    ASSIGNED_MAC=""
    global SPOOF_MAC
    SPOOF_MAC=""

    AllArguments=""
    
    import sys, getopt
    if cmdDisplay=="":
        cmdDisplay="0"
    Err=0
    totalarg=len(sys.argv)
    printd ("Argument Len    : " + str(totalarg))
    printd ("Argument String : " + str(sys.argv))
    if totalarg>1:
        i=1
        while i < totalarg:
            Err=""
            if i>0:
                i2=i+1
                if i2 >= len(sys.argv):
                   i2=i
                   i2str=""
                else:
                   i2str=str(sys.argv[i2])
                argstr=("Argument %d : %s" % (i, str(sys.argv[i])))
                printd (argstr) 
                arg=str(sys.argv[i])
                if arg=="-h" or arg=="--help":
                    DisplayHelp()
                    Err=0
                    exit()
                    break;
                elif arg=="-hh":
                    DisplayDetailHelp()
                    Err=0
                    exit()
                elif arg=="--update":
                    Err=0
                    GetUpdate("1")
                    exit()
                elif arg=="--remove":
                    Err=0
                    UninstallApplication()
                    exit()
                elif arg=="--spoof":
                    AllArguments=AllArguments + fcolor.BWhite + "Spoof MAC\t\t:  " + fcolor.BRed + "Enabled\n"
                    SPOOF_MAC="1"
                    Err=0
                elif arg=="-m" or arg=="--mac":
                    i=i2
                    if i2str=="":
                        printc("!!!","Invalid MAC Address set !","")  
                        Err=1
                    else:
                        Err=0
                        if i2str[:1]!="-":
                            if len(i2str)==17:
                                Result=CheckMAC(i2str)
                                if Result!="":
                                    ASSIGNED_MAC=i2str 
                                    AllArguments=AllArguments + fcolor.BWhite + "Selected MAC\t\t:  " + fcolor.BRed + i2str + "\n"
                                    SPOOF_MAC="1"
                                else:
                                    printc("!!!","Invalid MAC Address set [ " + fcolor.BWhite + i2str + fcolor.BRed + " ] !","")  
                                    Err=1
                            else:
                                printc("!!!","Invalid MAC Address set [ " + fcolor.BWhite + i2str + fcolor.BRed + " ] !","")  
                                Err=1
                        else:
                            printc("!!!","Invalid MAC Address set [ " + fcolor.BWhite + i2str + fcolor.BRed + " ] !","")  
                            Err=1
                elif arg=="-t" or arg=="--timeout":
                    i=i2
                    if i2str=="":
                        printc("!!!","Invalid timeout variable set !","")  
                        Err=1
                    else:
                        Err=0
                        if i2str[:1]!="-":
                            if i2str.isdigit():
                                TIMEOUT=i2str
                                AllArguments=AllArguments + fcolor.BWhite + "Timeout (Seconds)\t:  " + fcolor.BRed + i2str + "\n"
                            else:
                                printc("!!!","Invalid timeout variable set [ " + fcolor.BWhite + i2str + fcolor.BRed + " ] !","")  
                                Err=1
                        else:
                            printc("!!!","Invalid timeout variable set [ " + fcolor.BWhite + i2str + fcolor.BRed + " ] !","")  
                            Err=1
                elif arg=="-i" or arg=="--iface":
                    i=i2
                    if i2str=="":
                        printc("!!!","Invalid Interface variable set !","")  
                        Err=1
                    else:
                        Err=0
                        if i2str[:1]!="-":
                            SELECTED_IFACE=i2str
                            AllArguments=AllArguments + fcolor.BWhite + "Selected interface\t:  " + fcolor.BRed + i2str + "\n"
                        else:
                            printc("!!!","Invalid Interface variable set [ " + fcolor.BWhite + i2str + fcolor.BRed + " ] !","")  
                            Err=1
                elif Err=="":
                        DisplayHelp()
                        printc("!!!","Invalid option set ! [ " + fcolor.BGreen + arg + fcolor.BRed + " ]","")
                        Err=1
                        exit(0)
                if Err==1:
                    if cmdDisplay=="2":
                        print ""
                        DisplayHelp()
                        exit(0)
                i=i+1
        if AllArguments!="":
            print ""
            print fcolor.BYellow + "Parameter set:"
            print AllArguments
        else:
            print ""
            DisplayHelp()
        print ""
        printc ("i", fcolor.BCyan + "Entering Semi-Interactive Mode..","")
        result=DisplayTimeStamp("start","")
        print ""

    else:
        if cmdDisplay=="1":
            DisplayHelp()
        if cmdDisplay=="2":
            DisplayHelp()
            exit(0)
        else:
            printc ("i", fcolor.BCyan + "Entering Interactive Mode..","")
            result=DisplayTimeStamp("start","")
            print ""


def GetFileLine(filename,omitblank):
    global TotalLine
    global UsableLine
    TotalLine=0
    UsableLine=0
    if omitblank=="":
        omitblank="0"

    if omitblank=="1":
        with open(filename, 'r') as f: 
            lines = len(list(filter(lambda x: x.strip(), f)))
        TotalLine=lines
        UsableLine=lines
    if omitblank=="0":
        with open(filename) as f:
            lines=len(f.readlines())
        TotalLine=lines
        UsableLine=lines
    if omitblank=="2":
        lines=0
	with open(filename,"r") as f:
	    for line in f:
                sl=len(line.replace("\n",""))
                if sl>0:
                    TotalLine=TotalLine+1
                    if sl>=8 and sl<=63:
                        lines=lines+1
                        UsableLine=lines
    return lines

def CheckMAC(MACAddr):
    import string
    result=""
    allchars = "".join(chr(a) for a in range(256))
    delchars = set(allchars) - set(string.hexdigits)
    mac = MACAddr.translate("".join(allchars),"".join(delchars))
    if len(mac) != 12:
        print "mac result = " + str(result)
        return result;
    else:
        result=MACAddr.upper()
    print "mac result = " + str(result)
    return result;

def CheckAppLocation():
    import shutil
    cpath=0
    if os.path.exists(appdir)==True:
        printd ("[" + appdir + "] exist..")
    else:
        printd ("[" + appdir + "] does not exist..")
        result=MakeTree(appdir,"")
        cpath=1
    curdir=os.getcwd() + "/"
    printd ("Current Path : " + str(curdir))
    CurFileLocation=curdir + ScriptName
    AppFileLocation=appdir + ScriptName
    printd("Current File : " + str(CurFileLocation))
    printd("Designated File : " + str(AppFileLocation))
    if os.path.exists(AppFileLocation)==False:
        printd("File Not found in " + str(AppFileLocation))
        printd("Copy file from [" + str(CurFileLocation) + "] to [" + str(AppFileLocation) + " ]")
        shutil.copy2(CurFileLocation, AppFileLocation)
        result=os.system("chmod +x " + AppFileLocation + " > /dev/null 2>&1")
    if os.path.exists("/usr/sbin/" + ScriptName)==False:
        printd("File Not found in " + "/usr/sbin/" + str(ScriptName))
        printd("Copy file from [" + str(CurFileLocation) + "] to [" + "/usr/sbin/" + str(ScriptName) + " ]")
        shutil.copy2(CurFileLocation, "/usr/sbin/" + str(ScriptName))
        result=os.system("chmod +x " + "/usr/sbin/" + str(ScriptName) + " > /dev/null 2>&1")
    if PathList!="":
        printd("PathList : " + str(PathList))
        for path in PathList:
            newPath=appdir + path
            printd("Checking : " + str(newPath))
            if os.path.exists(newPath)==False:
                printd("Path [ " + str(newPath) + " ] not found.")
                cpath=1
                result=MakeTree(newPath,"")
    if cpath==1:
        print ""




def DisplayTimeStamp(cmdDisplayType,cmdTimeFormat):
#   Requirement : import datetime
#   cmdDisplayType = start   : Tag starting timestamp and display
#                    start-h : Tag starting timestamp only
#                    stop    : Tag stopping timestamp and display
#                    stop-h : Tag stopping timestamp only
#
#   cmdTimeFormat  = User defined (Default : %Y-%m-%d %H:%M:%S)
#
    global TimeStart
    global TimeStop
    global DTimeStart
    global DTimeStop
    lblColor=fcolor.BGreen
    txtColor=fcolor.SGreen

    cmdDisplayType=cmdDisplayType.lower()
    if cmdTimeFormat=="":
        timefmt="%Y-%m-%d %H:%M:%S"
    else:
         timefmt=cmdTimeFormat

    if cmdDisplayType=="start":
        TimeStop=""
        DTimeStop=""
        DTimeStart=time.strftime(timefmt)
        printc ("  ",lblColor + "Started\t: " + txtColor + str(DTimeStart),"")
        TimeStart=datetime.datetime.now()
        return DTimeStart;
    if cmdDisplayType=="start-h":
        TimeStop=""
        DTimeStop=""
        DTimeStart=time.strftime(timefmt)
        TimeStart=datetime.datetime.now()
        return DTimeStart;
    if cmdDisplayType=="stop":
        DTimeStop=time.strftime(timefmt)
        printc ("  ",lblColor + "Stopped\t: " + txtColor + str(DTimeStop),"")
        TimeStop=datetime.datetime.now()
        return DTimeStop;
    if cmdDisplayType=="stop-h":
        DTimeStop=time.strftime(timefmt)
        TimeStop=datetime.datetime.now()
        return DTimeStop;
    if TimeStart!="":
        if cmdDisplayType=="summary" or cmdDisplayType=="summary-a":
            if TimeStop=="":
                TimeStop=datetime.datetime.now()
                DTimeStop=time.strftime(timefmt)
            ElapsedTime = TimeStop - TimeStart
	    ElapsedTime=str(ElapsedTime)
	    ElapsedTime=ElapsedTime[:-4]
            if cmdDisplayType=="summary-a":
                printc ("  ",lblColor + "Started\t: " + txtColor + str(DTimeStart),"")
                printc ("  ",lblColor + "Stopped\t: " + txtColor + str(DTimeStop),"")
	        printc ("  ",lblColor + "Time Spent\t: " + fcolor.BRed + str(ElapsedTime),"")
            if cmdDisplayType=="summary":
	        printc ("  ",lblColor + "Time Spent\t: " + fcolor.BRed + str(ElapsedTime),"")
        return ElapsedTime;
         
class GracefulInterruptHandler(object):
    def __init__(self, sig=signal.SIGINT):
        self.sig = sig
    def __enter__(self):
        self.interrupted = False
        self.released = False
        self.original_handler = signal.getsignal(self.sig)
        def handler(signum, frame):
            self.release()
            self.interrupted = True
        signal.signal(self.sig, handler)
        return self
    def __exit__(self, type, value, tb):
        self.release()
    def release(self):
        if self.released:
            return False
        signal.signal(self.sig, self.original_handler)
        self.released = True
        return True

def printd(ptext):
    if DebugMode=="1":
        print fcolor.CDebugB  + "[DBG]  " + fcolor.CDebug + ptext  + fcolor.CReset
    if DebugMode=="2":
        print fcolor.CDebugB + "[DBG]  " + fcolor.CDebug + ptext + fcolor.CReset
        print fcolor.CReset + fcolor.White + "       [Break - Press Any Key To Continue]" + fcolor.CReset
        read_a_key()


def GetInterfaceList(cmdMode):
    global IFaceList
    global IEEEList
    global ModeList
    global MACList
    global IPList
    global BCastList
    global MaskList
    global UpDownList
    global StatusList
    global ISerialList
    global IPv6List
    if cmdMode=="":
        cmdMode="ALL"
    proc  = Popen("ifconfig -a", shell=True, stdout=subprocess.PIPE, stderr=open(os.devnull, 'w'))
    IFACE = ""
    IEEE = ""
    MODE = ""
    MACADDR=""
    IPADDR=""
    IPV6ADDR = ""
    BCAST=""
    MASK=""
    STATUS=""
    IFUP=""
    LANMODE=""
    GATEWAY=""
    IFaceCount=0
    IFaceList = []
    IEEEList = []
    ModeList = []
    MACList = []
    IPList = []
    IPv6List = []
    BCastList = []
    MaskList = []
    StatusList = []
    UpDownList = []
    ISerialList = []
    for line in proc.communicate()[0].split('\n'):
        if len(line) == 0: continue
	if ord(line[0]) != 32:
            printd ("Line : " + str(line))
            IFACE = line[:line.find(' ')]
            IFACE2=IFACE[:2].upper()
            printd ("IFACE : " + str(IFACE))
            printd ("IFACE2 : " + str(IFACE2))

            if IFACE2!="ET" and IFACE2!="LO" and IFACE2!="VM" and IFACE2!="PP" and IFACE2!="AT":
                ps=subprocess.Popen("iwconfig " + str(IFACE) + "| grep -i 'Mode:' | tr -s ' ' | egrep -o 'Mode:..................' | cut -d ' ' -f1 | cut -d ':' -f2" , shell=True, stdout=subprocess.PIPE, stderr=open(os.devnull, 'w'))	
                MODEN=ps.stdout.read().replace("\n","")
                MODE=MODEN.upper()
                ps=subprocess.Popen("iwconfig " + str(IFACE) + "| grep -o 'IEEE..........................' | cut -d ' ' -f2" , shell=True, stdout=subprocess.PIPE)	
                IEEE=ps.stdout.read().replace("\n","").upper().replace("802.11","802.11 ")
                LANMODE="WLAN"
            else:
                MODE="NIL"
                MODEN="Nil"
                IEEE="802.3"
                LANMODE="LAN"

            if IFACE2=="LO":
                MODE="LO"
                MODEN="Loopback"
                IEEE="Nil"
                LANMODE="LO"

            printd ("MODE : " + str(MODE))
            printd ("MODEN : " + str(MODEN))

            ps=subprocess.Popen("ifconfig " + str(IFACE) + " | grep 'HWaddr' | tr -s ' ' | cut -d ' ' -f5" , shell=True, stdout=subprocess.PIPE)	
            MACADDR=ps.stdout.read().replace("\n","").upper().replace("-",":")
            MACADDR=MACADDR[:17]

            ps=subprocess.Popen("ifconfig " + str(IFACE) + " | egrep -o '([0-9]{1,3}\.){3}[0-9]{1,3}' | sed -n '1p'" , shell=True, stdout=subprocess.PIPE)	
            IPADDR=ps.stdout.read().replace("\n","").upper()    

            ps=subprocess.Popen("ifconfig " + str(IFACE) + " | grep -a -i 'inet6 addr:' | tr -s ' ' | sed -n '1p' | cut -d ' ' -f4" , shell=True, stdout=subprocess.PIPE)	
            IPV6ADDR=ps.stdout.read().replace("\n","").upper()

            ps=subprocess.Popen("ifconfig " + str(IFACE) + " | grep '\<Bcast\>' | sed -n '1p' | tr -s ' '  | cut -d ' ' -f4 | cut -d ':' -f2" , shell=True, stdout=subprocess.PIPE)	
            BCAST=ps.stdout.read().replace("\n","").upper()

            ps=subprocess.Popen("ifconfig " + str(IFACE) + " | grep '\<Mask\>' | sed -n '1p' | tr -s ' '  | cut -d ' ' -f5 | cut -d ':' -f2" , shell=True, stdout=subprocess.PIPE)	
            MASK=ps.stdout.read().replace("\n","").upper()

            if cmdMode=="CON":
                ps=subprocess.Popen("netstat -r | grep -a -i '" + str(IFACE) + "'  | awk '{print $2}' | egrep -o '([0-9]{1,3}\.){3}[0-9]{1,3}' | sed -n '1p'" , shell=True, stdout=subprocess.PIPE)	
                GATEWAY=ps.stdout.read().replace("\n","").upper()
            else:
                GATEWAY=""
            printd ("GATEWAY : " + GATEWAY)

            ps=subprocess.Popen("ifconfig " + str(IFACE) + " | grep 'MTU:' | sed -n '1p' | tr -s ' ' | grep -o '.\{0,100\}MTU'" , shell=True, stdout=subprocess.PIPE)	
            STATUS=ps.stdout.read().replace("\n","").upper().replace(" MTU","").lstrip().rstrip()
            ps=subprocess.Popen("ifconfig " + str(IFACE) + " | grep 'MTU:' | sed -n '1p' | tr -s ' ' | grep -o '.\{0,100\}MTU' | cut -d ' ' -f2 | grep 'UP'" , shell=True, stdout=subprocess.PIPE)	
            Result=ps.stdout.read().replace("\n","").upper().lstrip().rstrip()
            if Result=="UP":
                IFUP="Up"
            else:
                IFUP="Down"

            printd ("STATUS : " + str(STATUS))
            printd ("line " + line)
            printd ("IEEE : " + IEEE)
            printd ("MACADDR : " + str(MACADDR))
            printd ("IPADDR : " + str(IPADDR))
            printd ("MASK : " + str(MASK))
            printd ("IFUP : " + str(IFUP))
            printd ("cmdMode := " + str(cmdMode))
            if cmdMode=="ALL":
                IFaceCount=IFaceCount+1
                ModeList.append(str(MODEN))
                IFaceList.append(IFACE)
                IEEEList.append(IEEE)
                MACList.append(MACADDR)
                IPList.append(IPADDR)
                IPv6List.append(IPV6ADDR)
                BCastList.append(BCAST)
                MaskList.append(MASK)
                StatusList.append(STATUS)
                UpDownList.append(IFUP)
                ISerialList.append(str(IFaceCount))
            if MODE=="MANAGED":
                if cmdMode=="MAN":
                    IFaceCount=IFaceCount+1
                    ModeList.append(MODEN)
                    IFaceList.append(IFACE)
                    IEEEList.append(IEEE)
                    MACList.append(MACADDR)
                    IPList.append(IPADDR)
                    IPv6List.append(IPV6ADDR)
                    BCastList.append(BCAST)
                    MaskList.append(MASK)
                    StatusList.append(STATUS)
                    UpDownList.append(IFUP)
                    ISerialList.append(str(IFaceCount))
            if MODE=="MONITOR":
                if cmdMode=="MON":
                    IFaceCount=IFaceCount+1
                    ModeList.append(MODEN)
                    IFaceList.append(IFACE)
                    IEEEList.append(IEEE)
                    MACList.append(MACADDR)
                    IPList.append(IPADDR)
                    IPv6List.append(IPV6ADDR)
                    BCastList.append(BCAST)
                    MaskList.append(MASK)
                    StatusList.append(STATUS)
                    UpDownList.append(IFUP)
                    ISerialList.append(str(IFaceCount))
            if MODE=="MASTER":
                if cmdMode=="MAS":
                    IFaceCount=IFaceCount+1
                    ModeList.append(MODEN)
                    IFaceList.append(IFACE)
                    IEEEList.append(IEEE)
                    MACList.append(MACADDR)
                    IPList.append(IPADDR)
                    IPv6List.append(IPV6ADDR)
                    BCastList.append(BCAST)
                    MaskList.append(MASK)
                    StatusList.append(STATUS)
                    UpDownList.append(IFUP)
                    ISerialList.append(str(IFaceCount))
            if MODE=="AD-HOC":
                if cmdMode=="ADH":
                    IFaceCount=IFaceCount+1
                    ModeList.append(MODEN)
                    IFaceList.append(IFACE)
                    IEEEList.append(IEEE)
                    MACList.append(MACADDR)
                    IPList.append(IPADDR)
                    IPv6List.append(IPV6ADDR)
                    BCastList.append(BCAST)
                    MaskList.append(MASK)
                    StatusList.append(STATUS)
                    UpDownList.append(IFUP)
                    ISerialList.append(str(IFaceCount))
            if cmdMode=="IP" and BCAST!="":
                if IPV6ADDR!="" or IPADDR!="":
                    IFaceCount=IFaceCount+1
                    ModeList.append(MODEN)
                    IFaceList.append(IFACE)
                    IEEEList.append(IEEE)
                    MACList.append(MACADDR)
                    IPList.append(IPADDR)
                    IPv6List.append(IPV6ADDR)
                    BCastList.append(BCAST) 
                    MaskList.append(MASK)
                    StatusList.append(STATUS)
                    UpDownList.append(IFUP)
                    ISerialList.append(str(IFaceCount))
            if cmdMode=="CON" and IPADDR!="" and GATEWAY!="" and BCAST!="":
                IFaceCount=IFaceCount+1
                ModeList.append(MODEN)
                IFaceList.append(IFACE)
                IEEEList.append(IEEE)
                MACList.append(MACADDR)
                IPList.append(IPADDR)
                IPv6List.append(IPV6ADDR)
                BCastList.append(BCAST) 
                MaskList.append(MASK)
                StatusList.append(STATUS)
                UpDownList.append(IFUP)
                ISerialList.append(str(IFaceCount))

            if cmdMode=="WLAN" and LANMODE=="WLAN":
                IFaceCount=IFaceCount+1
                ModeList.append(MODEN)
                IFaceList.append(IFACE)
                IEEEList.append(IEEE)
                MACList.append(MACADDR)
                IPList.append(IPADDR)
                IPv6List.append(IPV6ADDR)
                BCastList.append(BCAST) 
                MaskList.append(MASK)
                StatusList.append(STATUS)
                UpDownList.append(IFUP)
                ISerialList.append(str(IFaceCount))

            if cmdMode=="LAN" and LANMODE=="LAN":
                IFaceCount=IFaceCount+1
                ModeList.append(MODEN)
                IFaceList.append(IFACE)
                IEEEList.append(IEEE)
                MACList.append(MACADDR)
                IPList.append(IPADDR)
                IPv6List.append(IPV6ADDR)
                BCastList.append(BCAST) 
                MaskList.append(MASK)
                StatusList.append(STATUS)
                UpDownList.append(IFUP)
                ISerialList.append(str(IFaceCount))

            if cmdMode=="LOOP" and LANMODE=="LO":
                IFaceCount=IFaceCount+1
                ModeList.append(MODEN)
                IFaceList.append(IFACE)
                IEEEList.append(IEEE)
                MACList.append(MACADDR)
                IPList.append(IPADDR)
                IPv6List.append(IPV6ADDR)
                BCastList.append(BCAST) 
                MaskList.append(MASK)
                StatusList.append(STATUS)
                UpDownList.append(IFUP)
                ISerialList.append(str(IFaceCount))
    return IFaceCount;


def RemoveColor(InText):
    if InText!="":
        InText=InText.replace('\033[0m','')
        InText=InText.replace('\033[1m','')
        InText=InText.replace('\033[2m','')
        InText=InText.replace('\033[4m','')
        InText=InText.replace('\033[5m','')
        InText=InText.replace('\033[7m','')
        InText=InText.replace('\033[8m','')
        InText=InText.replace('\033[1;90m','')
        InText=InText.replace('\033[0;90m','')
        InText=InText.replace('\033[30m','')
        InText=InText.replace('\033[31m','')
        InText=InText.replace('\033[32m','')
        InText=InText.replace('\033[33m','')
        InText=InText.replace('\033[34m','')
        InText=InText.replace('\033[35m','')
        InText=InText.replace('\033[36m','')
        InText=InText.replace('\033[37m','')
        InText=InText.replace('\033[0;30m','')
        InText=InText.replace('\033[0;31m','')
        InText=InText.replace('\033[0;32m','')
        InText=InText.replace('\033[0;33m','')
        InText=InText.replace('\033[0;34m','')
        InText=InText.replace('\033[0;35m','')
        InText=InText.replace('\033[0;36m','')
        InText=InText.replace('\033[0;37m','')
        InText=InText.replace('\033[1;30m','')
        InText=InText.replace('\033[1;31m','')
        InText=InText.replace('\033[1;34m','')
        InText=InText.replace('\033[1;33m','')
        InText=InText.replace('\033[1;32m','')
        InText=InText.replace('\033[1;35m','')
        InText=InText.replace('\033[1;36m','')
        InText=InText.replace('\033[1;37m','')
        InText=InText.replace('\033[4;30m','')
        InText=InText.replace('\033[4;31m','')
        InText=InText.replace('\033[4;32m','')
        InText=InText.replace('\033[4;33m','')
        InText=InText.replace('\033[4;34m','')
        InText=InText.replace('\033[4;35m','')
        InText=InText.replace('\033[4;36m','')
        InText=InText.replace('\033[4;37m','')
        InText=InText.replace('\033[0;90m','')
        InText=InText.replace('\033[0;91m','')
        InText=InText.replace('\033[0;92m','')
        InText=InText.replace('\033[0;93m','')
        InText=InText.replace('\033[0;94m','')
        InText=InText.replace('\033[0;95m','')
        InText=InText.replace('\033[0;96m','')
        InText=InText.replace('\033[0;97m','')
        InText=InText.replace('\033[1;90m','')
        InText=InText.replace('\033[1;91m','')
        InText=InText.replace('\033[1;92m','')
        InText=InText.replace('\033[1;93m','')
        InText=InText.replace('\033[1;94m','')
        InText=InText.replace('\033[1;95m','')
        InText=InText.replace('\033[1;96m','')
        InText=InText.replace('\033[1;97m','')
        InText=InText.replace('\033[40m','')
        InText=InText.replace('\033[41m','')
        InText=InText.replace('\033[42m','')
        InText=InText.replace('\033[43m','')
        InText=InText.replace('\033[44m','')
        InText=InText.replace('\033[45m','')
        InText=InText.replace('\033[46m','')
        InText=InText.replace('\033[47m','')
        InText=InText.replace('\033[100m','')
        InText=InText.replace('\033[101m','')
        InText=InText.replace('\033[102m','')
        InText=InText.replace('\033[103m','')
        InText=InText.replace('\033[104m','')
        InText=InText.replace('\033[105m','')
        InText=InText.replace('\033[106m','')
        InText=InText.replace('\033[107m','')
    return InText;

def CombineListing(List1, List2, List3, List4, List5, List6, List7, List8):
    global MergedList
    global MergedSpaceList
    global TitleList
    MergedList=[]
    MergedSpaceList=[]
    TitleList=[]
    CombineText=""
    ListMax1=0
    ListMax2=0
    ListMax3=0
    ListMax4=0
    ListMax5=0
    ListMax6=0
    ListMax7=0
    ListMax8=0

    x=0
    if str(List1)!="":
        while x < len(List1):
            if str(List1[x])!="":
                ETxt=RemoveColor(str(List1[x]))
                if len(ETxt)>ListMax1:
                    ListMax1=len(ETxt)
            x = x +1
        printd ("ListMax1 : " + str(ListMax1))
        ListMax1 = ListMax1 + 4

    x=0
    if str(List2)!="":
        while x < len(List2):
            if str(List2[x])!="":
                ETxt=RemoveColor(str(List2[x]))
                if len(ETxt)>ListMax2:
                    ListMax2=len(ETxt)
            x = x +1
        printd ("ListMax2 : " + str(ListMax2))
        ListMax2 = ListMax2 + 4

    x=0
    if str(List3)!="":
        while x < len(List3):
            if str(List3[x])!="":
                ETxt=RemoveColor(str(List3[x]))
                if len(ETxt)>ListMax3:
                    ListMax3=len(ETxt)
            x = x +1
        printd ("ListMax3 : " + str(ListMax3))
        ListMax3 = ListMax3 + 4
    x=0
    if str(List4)!="":
        while x < len(List4):
            if str(List4[x])!="":
                ETxt=RemoveColor(str(List4[x]))
                if len(ETxt)>ListMax4:
                    ListMax4=len(ETxt)
            x = x +1
        printd ("ListMax4 : " + str(ListMax4))
        ListMax4 = ListMax4 + 4
    x=0
    if str(List5)!="":
        while x < len(List5):
            if str(List5[x])!="":
                ETxt=RemoveColor(str(List5[x]))
                if len(ETxt)>ListMax5:
                    ListMax5=len(ETxt)
            x = x +1
        printd ("ListMax5 : " + str(ListMax5))
        ListMax5 = ListMax5 + 4
    x=0
    if str(List6)!="":
        while x < len(List6):
            if str(List6[x])!="":
                ETxt=RemoveColor(str(List6[x]))
                if len(ETxt)>ListMax6:
                    ListMax6=len(ETxt)
            x = x +1
        printd ("ListMax6 : " + str(ListMax6))
        ListMax6 = ListMax6 + 4
    x=0
    if str(List7)!="":
        while x < len(List7):
            if str(List7[x])!="":
                ETxt=RemoveColor(str(List7[x]))
                if len(ETxt)>ListMax7:
                    ListMax7=len(ETxt)
            x = x +1
        printd ("ListMax7 : " + str(ListMax7))
        ListMax7 = ListMax7 + 4
    x=0
    if str(List8)!="":
        while x < len(List8):
            if str(List8[x])!="":
                ETxt=RemoveColor(str(List8[x]))
                if len(ETxt)>ListMax8:
                    ListMax8=len(ETxt)
            x = x +1
        printd ("ListMax8 : " + str(ListMax8))
        ListMax8 = ListMax8 + 4
    printd ("ListMax1 - After + 4 : " + str(ListMax1))
    printd ("ListMax2 - After + 4 : " + str(ListMax2))
    printd ("ListMax3 - After + 4  : " + str(ListMax3))
    printd ("ListMax4 - After + 4  : " + str(ListMax4))
    printd ("ListMax5 - After + 4  : " + str(ListMax5))
    printd ("ListMax6 - After + 4  : " + str(ListMax6))
    printd ("ListMax7 - After + 4  : " + str(ListMax7))
    printd ("ListMax8 - After + 4  : " + str(ListMax8))
    MergedSpaceList.append(5)
    MergedSpaceList.append(ListMax1)
    MergedSpaceList.append(ListMax2)
    MergedSpaceList.append(ListMax3)
    MergedSpaceList.append(ListMax4)
    MergedSpaceList.append(ListMax5)
    MergedSpaceList.append(ListMax6)
    MergedSpaceList.append(ListMax7)
    MergedSpaceList.append(ListMax8)

    i=0
    while i < len(List1):
        remain1spc=ListMax1 - len(RemoveColor(List1[i]))
        CombineText=List1[i] + "<#&!#>" + " " * remain1spc

        if str(List2)!="":
            if str(List2[i])!="":
                remainspc=ListMax2 - len(RemoveColor(List2[i]))
                CombineText=CombineText  + List2[i] + " " * remainspc
            else:
                CombineText=CombineText + " " * ListMax2
        if str(List3)!="":
            if str(List3[i])!="":
                remainspc=ListMax3 - len(RemoveColor(List3[i]))
                CombineText=CombineText + "" + List3[i] + " " * remainspc
            else:
                CombineText=CombineText + "" + " " * ListMax3
        if str(List4)!="":
            if str(List4[i])!="":
                remainspc=ListMax4 - len(RemoveColor(List4[i]))
                CombineText=CombineText + "" + List4[i] + " " * remainspc
            else:
                CombineText=CombineText + "" + " " * ListMax4
        if str(List5)!="":
            if str(List5[i])!="":
                remainspc=ListMax5 - len(RemoveColor(List5[i]))
                CombineText=CombineText + "" + List5[i] + " " * remainspc
            else:
                CombineText=CombineText + "" + " " * ListMax5
        if str(List6)!="":
            if str(List6[i])!="":
                remainspc=ListMax6 - len(RemoveColor(List6[i]))
                CombineText=CombineText + "" + List6[i] + " " * remainspc
            else:
                CombineText=CombineText + "" + " " * ListMax6
        if str(List7)!="":
            if str(List7[i])!="":
                remainspc=ListMax7 - len(RemoveColor(List7[i]))
                CombineText=CombineText + "" + List7[i] + " " * remainspc
            else:
                CombineText=CombineText + "" + " " * ListMax7
        if str(List8)!="":
            if str(List8[i])!="":
                remainspc=ListMax8 - len(RemoveColor(List8[i]))
                CombineText=CombineText + "" + List8[i] + " " * remainspc
            else:
                CombineText=CombineText + "" + " " * ListMax8


        CombineText=CombineText.lstrip().rstrip()
        MergedList.append(str(CombineText))
        i = i + 1
    return i;



def QuestionFromList(ListTitle,ListTitleSpace,ListUse,AskQuestion,RtnType):
#   RtnType "0" = Return Selected Number
#           "1" = Return first field of selected list number
    global ListingIndex
    ListingIndex=""
    bcolor=fcolor.SWhite
    pcolor=fcolor.BYellow
    ttcolor=fcolor.BBlue
    lcolor=fcolor.SYellow
    scolor=fcolor.BRed
    tcolor=fcolor.BGreen
    x=0
    sn=0
    CombineTitle=""
    totallen=0
    while x < len(ListTitle):
        xlen=len(ListTitle[x])
        remainspc=ListTitleSpace[x] - xlen
        if x==8:
            remainspc = remainspc - 4
            if remainspc<1:
                remainspc=1
        CombineTitle=CombineTitle + ListTitle[x] + " " * remainspc
        x = x +1 
    totallen=len(CombineTitle) + 1
    printl("    ","1","")
    DrawLine("=",fcolor.SWhite,totallen)
    print bcolor + "[" + pcolor + "*" + bcolor + "]  " + ttcolor + str(CombineTitle) + fcolor.CReset
    printl("    ","1","")
    DrawLine("=",fcolor.SWhite,totallen)
    for i, showtext in enumerate(ListUse):
        sn=i + 1
        remainspc = 4 - len(str(sn))
        showtext=showtext.replace("<#&!#>","")
        print "     " +scolor + str(sn) + "." + " " * remainspc + lcolor+ showtext
    printl("    ","1","")
    DrawLine("^",fcolor.SWhite,totallen)
    usr_resp=raw_input (bcolor + "[" + pcolor + "?" + bcolor + "]  " + tcolor + str(AskQuestion) + " [ " + scolor + "1" + tcolor + "-" + scolor + str(sn) + tcolor + " / " + scolor + "0" + fcolor.SWhite + " = Cancel" + tcolor + " ] : " + fcolor.BWhite)
    while not usr_resp.isdigit() or int(usr_resp) < 0 or int(usr_resp) > len(ListUse):
        print ""
        Result=QuestionFromList(ListTitle,ListTitleSpace,ListUse,AskQuestion,RtnType)
        return str(Result)
    if RtnType=="1":
        usr_resp = int(usr_resp) - 1
        ListingIndex=usr_resp
        SelList=ListUse[int(usr_resp)]
        SelList=SelList.replace("<#&!#>","\t")
        SelList=RemoveColor(SelList)
        POS=SelList.find("\t", 2) +1
        SelList=SelList[:POS]
        Rtn=SelList
        ps=subprocess.Popen("echo " + str(SelList) + " | cut -d '\t' -f1" , shell=True, stdout=subprocess.PIPE)	
        Rtn=ps.stdout.read()
        Rtn=Rtn.replace("\n","")
        if usr_resp==-1:
            usr_resp=0
            Rtn="0"
        return Rtn;
    else:
        usr_resp=usr_resp.replace("\n","")
        ListingIndex=usr_resp
        return usr_resp;

def DelFile(strFileName,ShowDisplay):
    import glob, os
    RtnResult=False
    if ShowDisplay=="":
        ShowDisplay=0
    if strFileName.find("*")==-1 and strFileName.find("?")==-1:
        Result=IsFileDirExist(strFileName)
        if Result=="F":
            os.remove(strFileName)
            RtnResult=True
            if ShowDisplay=="1":
                printc (" ",fcolor.SGreen + "File [ " + fcolor.SRed + strFileName + fcolor.SGreen + " ] deleted.","")
        else:
            if ShowDisplay=="1":
                printc ("!!",fcolor.SRed + "File [ " + fcolor.SYellow + strFileName + fcolor.SRed + " ] does not exist.","")
        return RtnResult
    else:
        filelist = glob.glob(strFileName)
        fc=0
        for f in filelist:
            if ShowDisplay=="1":
                printc (" ",fcolor.SGreen + "Deleting [ " + fcolor.SRed + str(f) + fcolor.SGreen + " ]...","")
            os.remove(f)
            fc=fc+1
        if ShowDisplay=="1":
            printc (" ",fcolor.SGreen + "Total [ " + fcolor.BRed + str(fc) + fcolor.SGreen + " ] files deleted.","")
        RtnResult=True
    return RtnResult
    


def IsFileDirExist(strFilePath):
    """
        Function   : Check if a file/path exist
        Return     : "F" - Exist File 
                   : "D" - Exist Directory
                   : "E" - Does not exist
    """
    RtnResult="E"
    if os.path.exists(strFilePath)==True:
        if os.path.isfile(strFilePath)==True:
            RtnResult="F"
        if os.path.isdir(strFilePath)==True:
            RtnResult="D"
    return RtnResult;

def MakeTree(dirName,ShowDisplay):
    if ShowDisplay=="":
        ShowDisplay=0
    RtnResult=False
    printd ("Make Tree - " + dirName)
    printd ("Check Exists : " + str(os.path.exists(dirName)))
    printd ("IsFileDirExist : " + str(IsFileDirExist(dirName)))

    if not os.path.exists(dirName) or IsFileDirExist(dirName)=="E":
        printd ("Tree - " + dirName + " not found")
        ldir=[]
        splitpath = "/"
        ldir = dirName.split("/")
        i = 1
        while i < len(ldir):
            splitpath = splitpath + ldir[i] + "/"
            i = i + 1
            if not os.path.exists(splitpath):
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "Creating path [ " + fcolor.SRed + splitpath + fcolor.SGreen + " ] ...","")
                os.mkdir(splitpath, 0755)
                RtnResult=True
        printc (" ",fcolor.SGreen + "Path [ " + fcolor.SRed + dirName + fcolor.SGreen + " ] created...","")
        return RtnResult
    else:
        printd ("Tree - " + dirName + " Found")
        printc ("!!",fcolor.SRed + "Path [ " + fcolor.SYellow + dirName + fcolor.SRed + " ] already exist.","")
        RtnResult=True
        return RtnResult
    return RtnResult

def RemoveTree(dirName,ShowDisplay):
    import shutil
    RtnResult=False
    if ShowDisplay=="":
        ShowDisplay="0"

    if os.path.exists(dirName)==True:
        if ShowDisplay=="1":
            printc (" ",fcolor.SGreen + "Removing Tree [ " + fcolor.SRed + dirName + fcolor.SGreen + " ] ...","")
        shutil.rmtree(dirName)
        RtnResult=True
    else:
        if ShowDisplay=="1":
            printc ("!!",fcolor.SRed + "Path [ " + fcolor.SYellow + dirName + fcolor.SRed + " ] does not exist..","")
        return RtnResult;
    if IsFileDirExist(dirName)=="E":
        RtnResult=True
        if ShowDisplay=="1":
            printc (" ",fcolor.SGreen + "Tree [ " + fcolor.SRed + dirName + fcolor.SGreen + " ] Removed...","")
        return RtnResult
    else:
        return RtnResult

def CopyFile(RootSrcPath,RootDstPath, strFileName,ShowDisplay):
    import shutil
    import glob, os
    RtnResult=False
    if ShowDisplay=="":
        ShowDisplay=0

    if RootSrcPath[-1:]!="/":
        RootSrcPath=RootSrcPath + "/"
    if RootDstPath[-1:]!="/":
        RootDstPath=RootDstPath + "/"

    if strFileName.find("*")==-1 and strFileName.find("?")==-1:
        Result=IsFileDirExist(RootSrcPath + strFileName)
        if Result=="F":
            if not os.path.exists(RootDstPath):
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   Making Directory [ " + fcolor.SRed + RootDstPath + fcolor.SGreen + " ] ....","")
                Result=MakeTree(RootDstPath,ShowDisplay)
            if os.path.exists(RootDstPath + strFileName):
                os.remove(RootDstPath + strFileName)
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   Removing Existing Destination File [ " + fcolor.SRed + RootDstPath + strFileName + fcolor.SGreen + " ] ....","")
            if ShowDisplay=="1":
                printc (" ",fcolor.SGreen + "   Copying  [ " + fcolor.SWhite + RootSrcPath + strFileName + fcolor.SGreen + " ] to [ " + fcolor.SRed + RootDstPath + strFileName + fcolor.SGreen + " ] ....","")
            shutil.copy(RootSrcPath + strFileName, RootDstPath + strFileName)
            if os.path.exists(RootDstPath + strFileName):
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   File copied to [ " + fcolor.SRed + RootDstPath  + strFileName + fcolor.SGreen + " ] ....","")
                RtnResult=True
                return RtnResult;
            else:
                if ShowDisplay=="1":
                    printc ("!!",fcolor.SRed + "   File copying [ " + fcolor.SRed + RootDstPath  + strFileName + fcolor.SGreen + " ] failed....","")
            return RtnResult;
        else:
            if ShowDisplay=="1":
                printc ("!!",fcolor.SRed + "Source File [ " + fcolor.SRed + RootSrcPath  + strFileName + fcolor.SGreen + " ] not found !!","")
            return RtnResult;
    else:
        if not os.path.exists(RootDstPath):
            if ShowDisplay=="1":
                printc (" ",fcolor.SGreen + "   Making Directory [ " + fcolor.SRed + RootDstPath + fcolor.SGreen + " ] ....","")
            Result=MakeTree(RootDstPath,ShowDisplay)
        if ShowDisplay=="1":
            printc (" ",fcolor.SGreen + "   Listing File...." + RootSrcPath + strFileName,"")
        filelist = glob.glob(RootSrcPath + strFileName)
        fc=0
        for file in filelist:
            if os.path.exists(RootDstPath + file):
                os.remove(RootDstPath + file)
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   Removing Existing Destination File [ " + fcolor.SRed + RootDstPath + file + fcolor.SGreen + " ] ....","")
            DstFile=file.replace(RootSrcPath,RootDstPath)
            if ShowDisplay=="1":
                printc (" ",fcolor.SGreen + "   Moving  [ " + fcolor.SWhite + file + fcolor.SGreen + " ] to [ " + fcolor.SRed + DstFile + fcolor.SGreen + " ] ....","")
            shutil.copy(file, DstFile)
            if os.path.exists(DstFile):
                fc=fc+1
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   File copied to [ " + fcolor.SRed + DstFile + fcolor.SGreen + " ] ....","")
            else:
                if ShowDisplay=="1":
                    printc ("!!",fcolor.SRed + "   File copying [ " + fcolor.SRed + DstFile + fcolor.SGreen + " ] failed....","")
        if ShowDisplay=="1":
            printc (" ",fcolor.BGreen + "Total [ " + fcolor.BRed + str(fc) + fcolor.BGreen + " ] files copied.","")
        RtnResult=fc
    return RtnResult

def MoveFile(RootSrcPath,RootDstPath, strFileName,ShowDisplay):
    import shutil
    import glob, os
    RtnResult=False
    if ShowDisplay=="":
        ShowDisplay=0

    if RootSrcPath[-1:]!="/":
        RootSrcPath=RootSrcPath + "/"
    if RootDstPath[-1:]!="/":
        RootDstPath=RootDstPath + "/"

    if strFileName.find("*")==-1 and strFileName.find("?")==-1:
        Result=IsFileDirExist(RootSrcPath + strFileName)
        if Result=="F":
            if not os.path.exists(RootDstPath):
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   Making Directory [ " + fcolor.SRed + RootDstPath + fcolor.SGreen + " ] ....","")
                Result=MakeTree(RootDstPath,ShowDisplay)
            if os.path.exists(RootDstPath + strFileName):
                os.remove(RootDstPath + strFileName)
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   Removing Existing Destination File [ " + fcolor.SRed + RootDstPath + strFileName + fcolor.SGreen + " ] ....","")
            if ShowDisplay=="1":
                printc (" ",fcolor.SGreen + "   Moving  [ " + fcolor.SWhite + RootSrcPath + strFileName + fcolor.SGreen + " ] to [ " + fcolor.SRed + RootDstPath + strFileName + fcolor.SGreen + " ] ....","")
            shutil.move(RootSrcPath + strFileName, RootDstPath + strFileName)
            if os.path.exists(RootDstPath + strFileName):
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   File moved to [ " + fcolor.SRed + RootDstPath  + strFileName + fcolor.SGreen + " ] ....","")
                RtnResult=True
                return RtnResult;
            else:
                if ShowDisplay=="1":
                    printc ("!!",fcolor.SRed + "   File moving [ " + fcolor.SRed + RootDstPath  + strFileName + fcolor.SGreen + " ] failed....","")
            return RtnResult;
        else:
            if ShowDisplay=="1":
                printc ("!!",fcolor.SRed + "Source File [ " + fcolor.SRed + RootSrcPath  + strFileName + fcolor.SGreen + " ] not found !!","")
            return RtnResult;
    else:
        if not os.path.exists(RootDstPath):
            if ShowDisplay=="1":
                printc (" ",fcolor.SGreen + "   Making Directory [ " + fcolor.SRed + RootDstPath + fcolor.SGreen + " ] ....","")
            Result=MakeTree(RootDstPath,ShowDisplay)
        if ShowDisplay=="1":
            printc (" ",fcolor.SGreen + "   Listing File...." + RootSrcPath + strFileName,"")
        filelist = glob.glob(RootSrcPath + strFileName)
        fc=0
        for file in filelist:
            if os.path.exists(RootDstPath + file):
                os.remove(RootDstPath + file)
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   Removing Existing Destination File [ " + fcolor.SRed + RootDstPath + file + fcolor.SGreen + " ] ....","")
            DstFile=file.replace(RootSrcPath,RootDstPath)
            if ShowDisplay=="1":
                printc (" ",fcolor.SGreen + "   Moving  [ " + fcolor.SWhite + file + fcolor.SGreen + " ] to [ " + fcolor.SRed + DstFile + fcolor.SGreen + " ] ....","")
            shutil.move(file, DstFile)
            if os.path.exists(DstFile):
                fc=fc+1
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   File moved to [ " + fcolor.SRed + DstFile + fcolor.SGreen + " ] ....","")
            else:
                if ShowDisplay=="1":
                    printc ("!!",fcolor.SRed + "   File moving [ " + fcolor.SRed + DstFile + fcolor.SGreen + " ] failed....","")
        if ShowDisplay=="1":
            printc (" ",fcolor.BGreen + "Total [ " + fcolor.BRed + str(fc) + fcolor.BGreen + " ] files moved.","")
        RtnResult=fc
    return RtnResult

def MoveTree(RootSrcDir,RootDstDir,ShowDisplay):
    import shutil
    if ShowDisplay=="":
        ShowDisplay="0"

    ti=0
    td=0
    for Src_Dir, dirs, files in os.walk(RootSrcDir):
        Dst_Dir = Src_Dir.replace(RootSrcDir, RootDstDir)
        if Src_Dir!=RootSrcDir and Dst_Dir!=RootDstDir:
            td=td+1
            if ShowDisplay=="1":
                print fcolor.SGreen + "        Moving Directory " + "[ " + fcolor.SWhite + Src_Dir + fcolor.CReset + fcolor.SGreen + " ] to [ " + fcolor.SRed + Dst_Dir + fcolor.CReset + fcolor.SGreen + " ] ..."
        if not os.path.exists(Dst_Dir):
            os.mkdir(Dst_Dir)
        for file_ in files:
            SrcFile = os.path.join(Src_Dir, file_)
            DstFile = os.path.join(Dst_Dir, file_)
            if os.path.exists(DstFile):
                os.remove(DstFile)
            if ShowDisplay=="1":
                print fcolor.SGreen + "        Moving File " + "[ " + fcolor.SWhite + SrcFile + fcolor.CReset + fcolor.SGreen + " ] to [ " + fcolor.SRed + DstFile + fcolor.CReset + fcolor.SGreen + " ] ..."
            shutil.move(SrcFile, Dst_Dir)
            ti=ti+1
            if os.path.exists(Dst_Dir):
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   File moved to [ " + fcolor.SRed + DstFile + fcolor.SGreen + " ] ....","")
        if IsFileDirExist(Src_Dir)=="D":
            if Src_Dir!=RootSrcDir:
                print fcolor.SGreen + "        Removing Directory " + "[ " + fcolor.SWhite + Src_Dir + fcolor.CReset + fcolor.SGreen + " ] ...."
                Result=os.rmdir(Src_Dir)
    if ShowDisplay=="1":
        print fcolor.BGreen + "     Total [ " + fcolor.BRed + str(td) + fcolor.BGreen + " ] director(ies) and [ " + fcolor.BRed + str(ti) + fcolor.BGreen + " ] file(s) transfered.."
    return str(ti);


def CopyTree(RootSrcDir,RootDstDir,ShowDisplay):
    import shutil
    if ShowDisplay=="":
        ShowDisplay="0"

    ti=0
    td=0
    for Src_Dir, dirs, files in os.walk(RootSrcDir):
        Dst_Dir = Src_Dir.replace(RootSrcDir, RootDstDir)
        if Src_Dir!=RootSrcDir and Dst_Dir!=RootDstDir:
            td=td+1
            if ShowDisplay=="1":
                print fcolor.SGreen + "        Copying Directory " + "[ " + fcolor.SWhite + Src_Dir + fcolor.CReset + fcolor.SGreen + " ] to [ " + fcolor.SRed + Dst_Dir + fcolor.CReset + fcolor.SGreen + " ] ..."
        if not os.path.exists(Dst_Dir):
            os.mkdir(Dst_Dir)
        for file_ in files:
            SrcFile = os.path.join(Src_Dir, file_)
            DstFile = os.path.join(Dst_Dir, file_)
            if os.path.exists(DstFile):
                if ShowDisplay=="1":
                    print fcolor.SGreen + "        Replacing File " + fcolor.SRed + DstFile + fcolor.CReset + fcolor.SGreen + " ] ..."
                os.remove(DstFile)
                shutil.copy(SrcFile, Dst_Dir)
            else:
                if ShowDisplay=="1":
                    print fcolor.SGreen + "        Copy File " + "[ " + fcolor.SWhite + SrcFile + fcolor.CReset + fcolor.SGreen + " ] to [ " + fcolor.SRed + DstFile + fcolor.CReset + fcolor.SGreen + " ] ..."
                shutil.copy(SrcFile, Dst_Dir)
            ti=ti+1
            if os.path.exists(Dst_Dir):
                if ShowDisplay=="1":
                    printc (" ",fcolor.SGreen + "   File copied to [ " + fcolor.SRed + DstFile + fcolor.SGreen + " ] ....","")
    if ShowDisplay=="1":
        print fcolor.BGreen + "     Total [ " + fcolor.BRed + str(td) + fcolor.BGreen + " ] director(ies) and [ " + fcolor.BRed + str(ti) + fcolor.BGreen + " ] file(s) copied.."
    return str(ti);

def Explore(DirUrlName,ShowDisplay):
    if ShowDisplay=="":
        ShowDisplay=0
    Result=-1
    if DirUrlName!="":
        if ShowDisplay=="1":
            printc (" ",fcolor.SGreen + "Opening location [ " + fcolor.SRed + DirUrlName + fcolor.SGreen + " ] ...","")
        Result=os.system("xdg-open " + str(DirUrlName) + " > /dev/null 2>&1")
    return Result
def UninstallApplication():
    Ask=AskQuestion ("Are you sure you want to remove this application ?","y/N","","N","")
    if Ask=="y" or Ask=="Y":
        curdir=os.getcwd() + "/"
        CurFileLocation=curdir + ScriptName
        if os.path.exists(CurFileLocation)==True:
            printd("Delete File : " + CurFileLocation)
            result=os.remove(CurFileLocation)
        if os.path.exists("/usr/sbin/" + ScriptName)==True:
            printd("Delete File : " + "/usr/sbin/" + str(ScriptName))
            result=os.remove("/usr/sbin/" + ScriptName)
        if os.path.exists(appdir)==True:
            printd("Remove Path : " + appdir)
            result=RemoveTree(appdir,"")
        printc ("i", "Application successfully removed !!","")
        exit(0)
    else:
        printc ("i",fcolor.BWhite + "Uninstall aborted..","")
        exit(0)

def GetIWList(cmdMode,SELECTED_IFACE,RETRY):
    global AP_BSSIDList
    global AP_FREQList
    global AP_QUALITYList
    global AP_SIGNALList
    global AP_ENCKEYList
    global AP_ESSIDList
    global AP_MODEList
    global AP_CHANNELList
    global AP_ENCTYPEList
    if RETRY=="":
        AP_BSSIDList=[]
        AP_FREQList=[]
        AP_QUALITYList=[]
        AP_SIGNALList=[]
        AP_ENCKEYList=[]
        AP_ESSIDList=[]
        AP_MODEList=[]
        AP_CHANNELList=[]
        AP_ENCTYPEList=[]

    POPULATE=0
    if len(AP_BSSIDList)>0:
        Result=AskQuestion(fcolor.SGreen + "An existing list with [ " + fcolor.BRed + str(len(AP_BSSIDList)) + fcolor.SGreen + " ] records were found, " + fcolor.BGreen + "populate existing ?","Y/n","U","Y","1")
        if Result=="Y":
            POPULATE=1
        else:
            AP_BSSIDList=[]
            AP_FREQList=[]
            AP_QUALITYList=[]
            AP_SIGNALList=[]
            AP_ENCKEYList=[]
            AP_ESSIDList=[]
            AP_MODEList=[]
            AP_CHANNELList=[]
            AP_ENCTYPEList=[]
    cmdMode=cmdMode.upper()
    if cmdMode=="":
        cmdMode="ALL"
    Result=Run("ifconfig " + SELECTED_IFACE + " up","1")
    Result=printc (".","<$rs$>" + "Scanning for Access Point..Please wait..","")
    printl(Result,"1","")
    iwlistfile=appdir + "tmp/scan.lst"
    Result=Run("iwlist " + SELECTED_IFACE + " scanning > " + iwlistfile ,"0")
    printl(fcolor.BGreen + " [Completed]","1","")
    print ""
    statinfo = os.stat(iwlistfile)
    if statinfo.st_size==0:
        printc ("@",fcolor.SRed + "Scanning failed to get any access point..Retrying in 5 seconds..","5")
        GetIWList(cmdMode,SELECTED_IFACE,"1")
        return
    f = open( iwlistfile, "r" )
    AP_BSSID=""
    AP_FREQ=""
    AP_QUALITY=""
    AP_SIGNAL=""
    AP_ENCKEY=""
    AP_ESSID=""
    AP_MODE=""
    AP_CHANNEL=""
    AP_ENCTYPE=""
    if POPULATE=="1":
        printc (".","Populating current list...","")

    for line in f:
        line=line.replace("\n","").lstrip().rstrip()

        if line.find("Cell ")!=-1:
            if AP_BSSID!="" and AP_MODE!="":
                if AP_ENCTYPE=="" and AP_ENCKEY=="ON":
                    AP_ENCTYPE="WEP"
                if AP_ENCTYPE=="" and AP_ENCKEY=="OFF":
                    AP_ENCTYPE="OPEN"
                if AP_ENCTYPE=="WPA2/WPA":
                    AP_ENCTYPE=="WPA/WPA2"
                ADD=""
                if cmdMode=="ALL-S" and AP_ESSID.find("\\x")==-1 and AP_ESSID!="":
                    ADD="1"
                if cmdMode=="ALL":
                    ADD="1"
                if cmdMode=="WPA-S" and AP_ENCTYPE.find("WPA")!=-1 and AP_ESSID.find("\\x")==-1 and AP_ESSID!="" and len(AP_ESSID)>2:
                    ADD="1"
                if cmdMode=="WPA" and AP_ENCTYPE.find("WPA")!=-1:
                    ADD="1"
                if cmdMode=="WEP-S" and AP_ENCTYPE.find("WEP")!=-1 and AP_ESSID.find("\\x")==-1 and AP_ESSID!="" and len(AP_ESSID)>2:
                    ADD="1"
                if cmdMode=="WEP" and AP_ENCTYPE.find("WEP")!=-1:
                    ADD="1"
                if cmdMode=="OPN-S" and AP_ENCTYPE.find("OPEN")!=-1 and AP_ESSID.find("\\x")==-1 and AP_ESSID!="" and len(AP_ESSID)>2:
                    ADD="1"
                if cmdMode=="OPN" and AP_ENCTYPE.find("OPEN")!=-1:
                    ADD="1"
                if str(POPULATE)=="1":
                    if any(AP_BSSID in s for s in AP_BSSIDList):
                        ADD="0"


                if ADD=="1":
                    if int(AP_QUALITY[:2])<=35:
                        SNLColor=fcolor.IRed
                        BSNLColor=fcolor.BIRed
                    if int(AP_QUALITY[:2])>35 and int(AP_QUALITY[:2])<55:
                        SNLColor=fcolor.IYellow
                        BSNLColor=fcolor.BIYellow
                    if int(AP_QUALITY[:2])>=55:
                        SNLColor=fcolor.IGreen
                        BSNLColor=fcolor.BIGreen
                    if AP_ENCTYPE.find("WPA")!=-1:
                        AP_ENCTYPE=fcolor.IPink + AP_ENCTYPE
                        AP_BSSID=SNLColor + AP_BSSID
                    if AP_ENCTYPE.find("OPEN")!=-1:
                        AP_ENCTYPE=fcolor.IBlue + AP_ENCTYPE
                        AP_BSSID=SNLColor + AP_BSSID
                    if AP_ENCTYPE.find("WEP")!=-1:
                        AP_ENCTYPE=fcolor.ICyan + AP_ENCTYPE
                        AP_BSSID=SNLColor + AP_BSSID
                    AP_BSSIDList.append(str(AP_BSSID))
                    AP_FREQList.append(str(AP_FREQ))
                    AP_QUALITYList.append(SNLColor + str(AP_QUALITY))
                    AP_SIGNALList.append(SNLColor + str(AP_SIGNAL))
                    AP_ENCKEYList.append(str(AP_ENCKEY))
                    AP_ESSIDList.append(str(BSNLColor + AP_ESSID))
                    AP_MODEList.append(str(AP_MODE))
                    AP_CHANNELList.append(str(AP_CHANNEL))
                    AP_ENCTYPEList.append(str(AP_ENCTYPE))

                AP_BSSID=""
                AP_FREQ=""
                AP_QUALITY=""
                AP_CHANNEL=""
                AP_SIGNAL=""
                AP_ENCKEY=""
                AP_ESSID=""
                AP_MODE=""
                AP_ENCTYPE=""
                                
            POS=line.index('Address:')
            if POS>-1:
                POS=POS+9
                AP_BSSID=str(line[POS:])
        if AP_BSSID!="" and line.find("Channel:")!=-1:
            POS=line.index('Channel:')
            if POS>-1:
                POS=POS+8
                AP_CHANNEL=str(line[POS:])
        if AP_BSSID!="" and line.find("Frequency:")!=-1:
            POS=line.index('Frequency:')
            if POS>-1:
                POS=POS+10
                AP_FREQ=str(line[POS:])
                POS=AP_FREQ.index(' (')
                if POS>-1:
                    AP_FREQ=str(AP_FREQ[:POS])
        if AP_BSSID!="" and line.find("Quality=")!=-1:
            POS=line.index('Quality=')
            if POS>-1:
                POS=POS+8
                AP_QUALITY=str(line[POS:])
                POS=AP_QUALITY.index(' ')
                if POS>-1:
                    AP_QUALITY=str(AP_QUALITY[:POS])
        if AP_BSSID!="" and line.find("Signal level=")!=-1:
            POS=line.index('Signal level=')
            if POS>-1:
                POS=POS+13
                AP_SIGNAL=str(line[POS:])
        if AP_BSSID!="" and line.find("Encryption key:")!=-1:
            POS=line.index('Encryption key:')
            if POS>-1:
                POS=POS+15
                AP_ENCKEY=str(line[POS:]).upper()
        if AP_BSSID!="" and line.find("ESSID:")!=-1:
            POS=line.index('ESSID:')
            if POS>-1:
                POS=POS+6
                AP_ESSID=str(line[POS:])
        if AP_BSSID!="" and line.find("Mode:")!=-1:
            POS=line.index('Mode:')
            if POS>-1:
                POS=POS+5
                AP_MODE=str(line[POS:])
        if AP_BSSID!="" and line.find("WPA2 Version")!=-1:
            if AP_ENCTYPE!="": 
                if AP_ENCTYPE.find("WPA2")==-1:
                    AP_ENCTYPE=AP_ENCTYPE + "/WPA2"
            else:
                AP_ENCTYPE=AP_ENCTYPE + "WPA2"

        if AP_BSSID!="" and line.find("WPA Version")!=-1:
            if AP_ENCTYPE!="": 
                AP_ENCTYPE=AP_ENCTYPE + "/WPA"
            else:
                AP_ENCTYPE=AP_ENCTYPE + "WPA"
        AP_ENCTYPE=AP_ENCTYPE.replace("\n","")
        if AP_ENCTYPE=="WPA2/WPA":
            AP_ENCTYPE="WPA/WPA2"
    f.close()
    if AP_BSSID!="" and AP_MODE!="":
        if AP_ENCTYPE=="" and AP_ENCKEY=="ON":
            AP_ENCTYPE="WEP"
        if AP_ENCTYPE=="" and AP_ENCKEY=="OFF":
            AP_ENCTYPE="OPEN"
        if AP_ENCTYPE=="WPA2/WPA":
            AP_ENCTYPE=="WPA/WPA2"

        ADD=""
        if cmdMode=="ALL-S" and AP_ESSID.find("\\x")==-1 and AP_ESSID!="":
            ADD="1"
        if cmdMode=="ALL":
            ADD="1"
        if cmdMode=="WPA-S" and AP_ENCTYPE.find("WPA")!=-1 and AP_ESSID.find("\\x")==-1 and AP_ESSID!="" and len(AP_ESSID)>2:
            ADD="1"
        if cmdMode=="WPA" and AP_ENCTYPE.find("WPA")!=-1:
            ADD="1"
        if cmdMode=="WEP-S" and AP_ENCTYPE.find("WEP")!=-1 and AP_ESSID.find("\\x")==-1 and AP_ESSID!="" and len(AP_ESSID)>2:
            ADD="1"
        if cmdMode=="WEP" and AP_ENCTYPE.find("WEP")!=-1:
            ADD="1"
        if cmdMode=="OPN-S" and AP_ENCTYPE.find("OPEN")!=-1 and AP_ESSID.find("\\x")==-1 and AP_ESSID!="" and len(AP_ESSID)>2:
            ADD="1"
        if cmdMode=="OPN" and AP_ENCTYPE.find("OPEN")!=-1:
            ADD="1"
        if ADD=="1":
            if int(AP_QUALITY[:2])<=35:
                SNLColor=fcolor.IRed
                BSNLColor=fcolor.BIRed
            if int(AP_QUALITY[:2])>35 and int(AP_QUALITY[:2])<55:
                SNLColor=fcolor.IYellow
                BSNLColor=fcolor.BIYellow
            if int(AP_QUALITY[:2])>=55:
                SNLColor=fcolor.IGreen
                BSNLColor=fcolor.BIGreen
            if AP_ENCTYPE.find("WPA")!=-1:
                AP_ENCTYPE=fcolor.IPink + AP_ENCTYPE
                AP_BSSID=SNLColor + AP_BSSID
            if AP_ENCTYPE.find("OPEN")!=-1:
                AP_ENCTYPE=fcolor.IBlue + AP_ENCTYPE
                AP_BSSID=SNLColor + AP_BSSID
            if AP_ENCTYPE.find("WEP")!=-1:
                AP_ENCTYPE=fcolor.ICyan + AP_ENCTYPE
                AP_BSSID=SNLColor + AP_BSSID
            AP_BSSIDList.append(str(AP_BSSID))
            AP_FREQList.append(str(AP_FREQ))
            AP_QUALITYList.append(SNLColor + str(AP_QUALITY))
            AP_SIGNALList.append(SNLColor + str(AP_SIGNAL))
            AP_ENCKEYList.append(str(AP_ENCKEY))
            AP_ESSIDList.append(str(BSNLColor + AP_ESSID))
            AP_MODEList.append(str(AP_MODE))
            AP_CHANNELList.append(str(AP_CHANNEL))
            AP_ENCTYPEList.append(str(AP_ENCTYPE))
        AP_BSSID=""
        AP_FREQ=""
        AP_QUALITY=""
        AP_CHANNEL=""
        AP_SIGNAL=""
        AP_ENCKEY=""
        AP_ESSID=""
        AP_MODE=""
        AP_ENCTYPE=""
              

def SelectInterfaceToUse():
#    global SELECTED_IFACE
#    SELECTED_IFACE=""
    printc ("i", fcolor.BRed + "Wireless Adapter Selection","")
    Result = GetInterfaceList("MAN")
    if Result==0:
        printc ("!", fcolor.SRed + "No wireless adapter adapter found !!","")
        exit()

    Result = CombineListing(IFaceList, MACList,UpDownList,IEEEList,StatusList,ModeList,IPList,ISerialList)
    if int(Result)>1:
        TitleList=['Sel','Iface','MAC Address','Up ?', 'IEEE','Status','Mode','IP Addr','Sr No']
        Result=QuestionFromList(TitleList, MergedSpaceList,MergedList,"Select the interface from the list","0")
        if Result=="0":
                 Result=AskQuestion(fcolor.SGreen + "You need to select a interface to use," + fcolor.BGreen + " retry ?","Y/n","U","Y","1")
                 if Result=="Y":
                     Result=SelectInterfaceToUse()
                     return Result
                 else:
                     exit(0)
        Result=int(Result)-1
        SELECTED_IFACE=IFaceList[int(Result)]
    else:
        SELECTED_IFACE=IFaceList[0]
    return SELECTED_IFACE;


def SelectMonitorToUse():
    time.sleep (0)
    MonCt = GetInterfaceList("MON")
    if MonCt==0:
        printc ("i", fcolor.BRed + "Monitoring Adapter Selection","")
    MonCt = GetInterfaceList("MON")
    if MonCt==0:
        printc ("!", fcolor.SRed + "No monitoring adapter found !!","")
        exit()


    Result = CombineListing(IFaceList, MACList,UpDownList,IEEEList,StatusList,ModeList,IPList,ISerialList)
    if int(Result)>1:
        TitleList=['Sel','Iface','MAC Address','Up ?', 'IEEE','Status','Mode','IP Addr','Sr No']
        Result=QuestionFromList(TitleList, MergedSpaceList,MergedList,"Select the monitoring interface from the list","0")
        if Result=="0":
                 Result=AskQuestion(fcolor.SGreen + "You need to select a monitoring interface to use," + fcolor.BGreen + " retry ?","Y/n","U","Y","1")
                 if Result=="Y":
                     Result=SelectMonitorToUse()
#                     print "SelectMonitorToUse " + str(Result)
                     return Result
                 else:
                     exit(0)
        Result=int(Result)-1
        SELECTED_MON=IFaceList[int(Result)]
    else:
        SELECTED_MON=IFaceList[0]
    return SELECTED_MON;

def CheckRequiredFiles():
    WPAS="/sbin/wpa_supplicant"
    if IsFileDirExist(WPAS)!="F":
            DDict=Run("locate aircrack-ng | sed -n '1p'","0")
            if DDict=="":
		printc ("!!!","Aircrack-NG suite must be installed inorder to use the Wireless IDS !","")
		exit (0)
    if IsFileDirExist(WPAS)!="F":
            DDict=Run("locate tshark | sed -n '1p'","0")
            if DDict=="":
		printc ("!!!","Aircrack-NG suite must be installed inorder to use the Wireless IDS !","")
		exit (0)

 
def AddTime(tm, secs):
    fulldate = datetime.datetime(tm.year, tm.month, tm.day, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate

def Percent(val, digits):
    val *= 10 ** (digits + 2)
    return '{1:.{0}f} %'.format(digits, floor(val) / 10 ** digits)

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
	    printd ("Thread started")
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
	    printd ("Thread Finish")

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
	    printd ("Terminating process..")
            self.process.terminate()
            thread.join()
	    printd ("Process Terminated")


def ChangeHex(n):
    x = (n % 16)
    c = ""
    if (x < 10):
        c = x
    if (x == 10):
        c = "A"
    if (x == 11):
        c = "B"
    if (x == 12):
        c = "C"
    if (x == 13):
        c = "D"
    if (x == 14):
        c = "E"
    if (x == 15):
        c = "F"
    if (n - x != 0):
        Result=ChangeHex(n / 16) + str(c)
    else:
        Result=str(c)
    if len(Result)==1:
        Result="0" + str(Result)
    if len(Result)==3:
        Result=Result[-2:]
    return Result

def SpoofMAC(SELECTED_IFACE,ASSIGNED_MAC):

    if ASSIGNED_MAC=="":
        H1="00"
        H2=ChangeHex(randrange(255))
        H3=ChangeHex(randrange(255))
        H4=ChangeHex(randrange(255))
        H5=ChangeHex(randrange(255))
        H6=ChangeHex(randrange(255))
        ASSIGNED_MAC=str(H1) + ":" + str(H2) + ":" + str(H3) + ":" + str(H4) + ":" + str(H5) + ":" + str(H6) 

    Result=""
    ps=subprocess.Popen("ifconfig " + str(SELECTED_IFACE) + " | grep 'HWaddr' | tr -s ' ' | cut -d ' ' -f5" , shell=True, stdout=subprocess.PIPE, stderr=open(os.devnull, 'w'))	
    MACADDR=ps.stdout.read().replace("\n","").upper().replace("-",":")
    MACADDR=MACADDR[:17]
    if str(MACADDR)!=ASSIGNED_MAC:
        printc ("i",fcolor.BRed + "Spoofing [ " + str(SELECTED_IFACE) + " ] MAC Address","")
        printc (" ",fcolor.BBlue + "Existing MAC\t: " + fcolor.BWhite + str(MACADDR),"")
        printc (" ",fcolor.BBlue + "Spoof MAC\t\t: " + fcolor.BWhite +  str(ASSIGNED_MAC),"")
        Result=MACADDR
        Ask=AskQuestion("Continue to spoof the MAC Address ?","Y/n","U","Y","0")
        if Ask=="Y":
            ps=subprocess.Popen("ifconfig " + str(SELECTED_IFACE) + " down hw ether " + str(ASSIGNED_MAC) + " > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE,stderr=open(os.devnull, 'w'))
            ps=subprocess.Popen("ifconfig " + str(SELECTED_IFACE) + " up > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE,stderr=open(os.devnull, 'w'))
            time.sleep(1)
            ps=subprocess.Popen("ifconfig " + str(SELECTED_IFACE) + " | grep 'HWaddr' | tr -s ' ' | cut -d ' ' -f5" , shell=True, stdout=subprocess.PIPE)
            NEWADDR=""
            NEWADDR=ps.stdout.read().replace("\n","").upper().replace("-",":")
            NEWADDR=NEWADDR[:17]
            if str(NEWADDR)==str(ASSIGNED_MAC):
                printc (" ",fcolor.BBlue + "MAC Address successfully changed to [ " + fcolor.BYellow + str(ASSIGNED_MAC) + fcolor.BBlue + " ]","")
                Result=str(ASSIGNED_MAC)
            else:
                printc (" ",fcolor.BRed + "Failed to change MAC Address !!","")
                Ask=AskQuestion("Retry with a new MAC Address ?","Y/n","U","Y","0")
                if Ask=="Y":
                    Result=SpoofMAC(SELECTED_IFACE,"")
                    return Result;
                else:
                    printc (" ",fcolor.BRed + "You choose to abort spoofing of MAC address.","")
                    printc (" ",fcolor.BBlue + "Using MAC Address [ " + fcolor.BYellow + str(NEWADDR) + fcolor.BBlue + " ]","")
                    return Result
        else:
            printc (" ",fcolor.BRed + "You choose to abort spoofing of MAC address.","")
            printc (" ",fcolor.BBlue + "Using MAC Address [ " + fcolor.BYellow + str(MACADDR) + fcolor.BBlue + " ]","")
    return Result


def CaptureTraffic():
    global pid1
    pid1=""
    captured_pcap=tmpdir + "captured"
    tcpdump_log=tmpdir + "tcpdump.log"
    tcpdump_cap=tmpdir + "tcpdump.cap"
    Result=DelFile(captured_pcap + "*","0")
    Result=DelFile(tcpdump_cap + "*","0")
    TimeOut=TIMEOUT

    mcmd1="airodump-ng " + SELECTED_MON + " -w " + str(captured_pcap) + " > /dev/null 2>&1"
    mcmd2="tshark -i " + str(SELECTED_MON) + " -w " + str(tcpdump_cap) +  " -n -t ad > /dev/null 2>&1"
    ps1=subprocess.Popen(mcmd1 , shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)	
    ps2=subprocess.Popen(mcmd2 , shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)	
    printc ("@",fcolor.SGreen + "Refreshing after " + fcolor.BYellow + str(TimeOut) + fcolor.SGreen + " seconds... please wait..",TimeOut)
    pid1=ps1.pid
    pid2=ps2.pid
    os.killpg(pid1, signal.SIGTERM)
    os.killpg(pid2, signal.SIGTERM)

    ps=subprocess.Popen("ps -A | grep 'airodump-ng' > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE)	
    Process=ps.stdout.read()
    if Process!="":
        ps=subprocess.Popen("killall 'airodump-ng' > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE)	
        Process=ps.stdout.read()

    statinfo = os.stat(tcpdump_cap)
    filesize=statinfo.st_size
    if filesize<300:
        printc ("!!!", "Captured packets size is too small... please make sure the monitoring interfaceing is working..","")


def GetMACDetail(FrMAC,ToMAC,AType):
    global CList
    CList=[]
    global Privacy
    global Cipher
    Privacy=""
    Cipher=""
    CLIENTS=0
    captured_csv=tmpdir + "CapturedListing.csv"
    ESSID_log=tmpdir + "ESSID.log"

    if IsFileDirExist(captured_csv)=="F":
#        print "Exist"
        ModiESSID=""
        with open(captured_csv,"r") as f:
            for line in f:
                line=line.replace("\n","")
                line=line.replace("\00","")
                if len(line)>10:
                    line=line + " ., ., ., ., ., ., ., ., ., ., ., ., ., ., ., ., ., ., ., ., ., "
                    line=line.replace("\r","")
                    CList=line.split(",")
                    FMAC=line.split()[0].replace(',','')
                    FS1=line.split()[0].replace(',','')
                    FS2=line.split()[1].replace(',','')
                    FS=str(FS1) + " " + str(FS2)
                    Privacy=CList[5].lstrip().rstrip()
                    Cipher=CList[6].lstrip().rstrip()
                    Authentication=CList[7].lstrip().rstrip()
                    Power=CList[8].lstrip().rstrip()
                    ESSID=CList[13].lstrip().rstrip().replace("\n","")
                    SMAC=CList[5].lstrip().rstrip()
                    Privacy=Privacy.replace('WPA2WPA OPN','WPA2WPA (OPN)')
                    Privacy=Privacy.replace('WPA2 OPN','WPA2 (OPN)')
                    Privacy=Privacy.replace('WPA OPN','WPA (OPN)')
                    Privacy=Privacy.replace('WPA2WPA','WPA2/WPA')
                    Privacy=Privacy.replace('WEP OPN','WEP (OPN)')
                    Cipher=Cipher.replace('CCMP TKIP','CCMP/TKIP')

                    if FS=="Station MAC":
                        CLIENTS=1


                    if len(FMAC)==17:
                        if FrMAC.find(str(FMAC))!=-1:
                            if CLIENTS!=1:
                                printc (" ",fcolor.BWhite + "[" + fcolor.BBlue + str(FMAC) + fcolor.BWhite + " ] is AP Name [ " + fcolor.BBlue + str(ESSID) + fcolor.BWhite + " ] and Privicy=" + fcolor.BRed + str(Privacy) + fcolor.BWhite + " Cipher=" + fcolor.BRed + str(Cipher) + fcolor.BWhite + " Authentication=" + fcolor.BRed + str(Authentication) + fcolor.BWhite + " Power=" + fcolor.BRed + str(Power) + fcolor.BWhite + "","")
                            else:
                                printc (" ",fcolor.BWhite + "[" + fcolor.BCyan + str(FMAC) + fcolor.BWhite + " ] is a client of [ " + fcolor.BCyan + str(SMAC) + fcolor.BWhite + " ]","")

                    if ToMAC.find(str(FMAC))!=-1:
                            if CLIENTS!=1:
                                printc (" ",fcolor.BWhite + "[" + fcolor.BBlue + str(FMAC) + fcolor.BWhite + " ] is AP Name [ " + fcolor.BBlue + str(ESSID) + fcolor.BWhite + " ] and Privicy=" + fcolor.BRed + str(Privacy) + fcolor.BWhite + " Cipher=" + fcolor.BRed + str(Cipher) + fcolor.BWhite + " Authentication=" + fcolor.BRed + str(Authentication) + fcolor.BWhite + " Power=" + fcolor.BRed + str(Power) + fcolor.BWhite + "","")
                            else:
                                printc (" ",fcolor.BWhite + "[" + fcolor.BCyan + str(FMAC) + fcolor.BWhite + " ] is a client of [ " + fcolor.BCyan + str(SMAC) + fcolor.BWhite + " ]","")

                    ESSID=ESSID.lstrip().rstrip().replace("\r","").replace("\n","")
                    if CLIENTS!=1:
                        SkipESSID=0
                        if IsFileDirExist(ESSID_log)!="F":
                            open(ESSID_log,"wb").write("" )
                        else:
                            with open(ESSID_log,"r") as f:
                                for line in f:                         
                                    line=line.replace("\n","")
                                    if len(line)>=18:
                                        if line.find(FMAC)!=-1:
                                            SkipESSID=1
                                            FileESSID=line.replace(FMAC,"").replace("\t","")
                                            FileESSID=FileESSID.lstrip().rstrip().replace("\r","").replace("\n","")
                        if SkipESSID==0 and ESSID!="":
                            if FMAC!="BSSID":
                                open(ESSID_log,"a+b").write("" + str(FMAC) + "\t" + str(ESSID) + "\n")
                        if SkipESSID==1 and ESSID!="":
                            if FileESSID!=ESSID:
                                ModiESSID=ModiESSID + fcolor.BGreen + "ESSID of [ " + fcolor.BBlue + str(FMAC) + fcolor.BGreen + " ] changed from [ " + fcolor.BRed + str(FileESSID) + fcolor.BGreen + " ] to [ " + fcolor.BRed + str(ESSID) + fcolor.BGreen + " ].\n"
    return ModiESSID;
    
     

def AnalyseCaptured():
    global List_FrMAC
    global List_ToMAC
    global List_Data
    global List_Auth
    global List_Deauth
    global List_Assoc
    global List_Reassoc
    global List_Disassoc
    global List_RTS
    global List_CTS
    global List_ACK
    global List_EAPOL
    global List_WPS

    List_FrMAC=[]
    List_ToMAC=[]
    List_Data=[]
    List_Auth=[]
    List_Deauth=[]
    List_Assoc=[]
    List_Reassoc=[]
    List_Disassoc=[]
    List_RTS=[]
    List_CTS=[]
    List_ACK=[]
    List_EAPOL=[]
    List_WPS=[]

    tcpdump_log=tmpdir + "tcpdump.log"
    resultlog=tmpdir + "Result.log"
    resultlist=tmpdir + "ResultList.log"

    linecount=0
    time.sleep(3)
    if IsFileDirExist(tcpdump_log)!="F":
        print "Another 3 Second"
        time.sleep(3)

    open(resultlog,"wb").write(tcpdump_log + "\n")

    TotalLine=GetFileLine(tcpdump_log,"0")
    BRes=0
    DisplayCt=0
    with open(tcpdump_log,"r") as f:
        for line in f:
            linecount=linecount+1
            DisplayCt=DisplayCt+1
            if DisplayCt>30:
                completed=Percent(linecount / float(TotalLine),2)
                BRes=printl(fcolor.SGreen + "Analysing Packets : " + str(completed) + ".." ,"2",BRes)
                DisplayCt=0
            line=line.replace("\n","")
            line=line.replace("(TA)","")
            line=line.replace("(RA)","")
            line=line.replace("(BSSID)","")
            sl=len(line)
            if sl>=15:
                line=line + " . . . . . . . . . . . . . . . . . . . . . . . . . . ."
                line=line.replace("\r","")
                FoundType=""

                STYPE=""
                DTYPE=""
                DTYPE2=""
                DTYPE3=""


                FR_MAC=line.split()[3].replace(',','').upper()
                TO_MAC=line.split()[5].replace(',','').upper()
                TO_MAC2=line.split()[4].replace(',','').upper()
                DTYPE=line.split()[8].replace(',','').replace(')','').upper()
                DTYPE2=line.split()[7].replace(',','').replace('(','').upper()
                DTYPE3=line.split()[9].replace(',','').replace('(','').upper()
                WPS1=line.split()[6].replace(',','').replace('(','').upper()
                WPS2=line.split()[11].replace(',','').replace('(','').upper()
                WPS3=line.split()[12].replace(',','').replace('(','').upper()


                if line.find(str('EAPOL'))!=-1:
                    DTYPE=line.split()[6].replace(',','').replace(')','').upper()

                if len(FR_MAC)==17 and len(TO_MAC)==17:
                    FoundType=1
                    STYPE=DTYPE
                if len(TO_MAC2)==17:
                    FoundType=2
                    STYPE=DTYPE2
                if len(FR_MAC)!=17 and len(TO_MAC)!=17 and len(TO_MAC2)!=17:
                    FoundType=3
                    STYPE=DTYPE2
                    DTYPEA=str(DTYPE2) + " " + str(DTYPE)
                    if DTYPEA=="RESERVED FRAME":
                        STYPE=DTYPEA

                DTYPEA=str(DTYPE) + " " + str(DTYPE3)
                if DTYPEA=="PROBE RESPONSE":
                    STYPE=DTYPEA
                if DTYPEA=="PROBE REQUEST":
                    STYPE=DTYPEA

                if WPS1=="EAP" and WPS2=="WPS":
                    STYPE="WPS"

                if str(TO_MAC)=="FF:FF:FF:FF:FF:FF":
                    BCast=1
                else:
                    BCast=0

                if len(FR_MAC)!=17:
                    FR_MAC=""
                if len(TO_MAC)!=17 and len(TO_MAC2)==17:
                    TO_MAC=TO_MAC2
                if len(TO_MAC2)!=17:
                    TO_MAC2=""
                if len(TO_MAC)!=17:
                    TO_MAC=""

                open(resultlog,"a+b").write("Line : " + str(line) + "\n")
                open(resultlog,"a+b").write("FoundType : " + str(FoundType) + "\n")
                open(resultlog,"a+b").write("STYPE : " + str(STYPE) + "\n")
                open(resultlog,"a+b").write("BCast  : " + str(BCast) + "\n")
                open(resultlog,"a+b").write("FR_MAC : " + str(FR_MAC) + " = " + str(len(FR_MAC))+ "\n")
                open(resultlog,"a+b").write("TO_MAC : " + str(TO_MAC) + str(len(TO_MAC)) +  "\n")
                open(resultlog,"a+b").write("TO_MAC2 : " + str(TO_MAC2) + str(len(TO_MAC2)) +"\n")
                open(resultlog,"a+b").write("DTYPE  : " + str(DTYPE) + "\n")
                open(resultlog,"a+b").write("DTYPE2  : " + str(DTYPE2) + "\n")
                open(resultlog,"a+b").write("DTYPE3  : " + str(DTYPE3) + "\n")
                open(resultlog,"a+b").write("WPS1  : " + str(WPS1) + "\n")
                open(resultlog,"a+b").write("WPS2  : " + str(WPS2) + "\n")
                open(resultlog,"a+b").write("WPS3  : " + str(WPS3) + "\n")
                open(resultlog,"a+b").write("-----------------------------------------------------" + "\n")

                GET_DATA="0"
                GET_AUTH="0"
                GET_DEAUTH="0"
                GET_DISASSOC="0"
                GET_REASSOC="0"
                GET_ASSOC="0"
                GET_RTS="0"
                GET_CTS="0"
                GET_ACK="0"
                GET_EAPOL="0"
                GET_WPS="0"

                if STYPE=="DATA" or STYPE=="QOS":
                    if TO_MAC=="FF:FF:FF:FF:FF:FF":
                        GET_DATA="1"
                if STYPE=="AUTHENTICATION":
                    GET_AUTH="1"
                if STYPE=="DEAUTHENTICATION":
                    GET_DEAUTH="1"
                if STYPE=="DISASSOCIATE":
                    GET_DISASSOC="1"
                if STYPE=="ASSOCIATION":
                    GET_ASSOC="1"
                if STYPE=="REASSOCIATION":
                    GET_REASSOC="1"
                if STYPE=="REQUEST-TO-SEND":
                    GET_RTS="1"
                if STYPE=="CLEAR-TO-SEND":
                    GET_CTS="1"
                if STYPE=="ACKNOWLEDGEMENT":
                    GET_ACK="1"
                if STYPE=="EAPOL":
                    GET_EAPOL="1"
                if STYPE=="WPS":
                    GET_WPS="1"

                if STYPE=="DATA" or STYPE=="QOS" or STYPE=="AUTHENTICATION" or STYPE=="DEAUTHENTICATION" or STYPE=="ASSOCIATION" or STYPE=="DISASSOCIATE" or STYPE=="REASSOCIATION" or STYPE=="REQUEST-TO-SEND" or STYPE=="CLEAR-TO-SEND" or STYPE=="ACKNOWLEDGEMENT" or STYPE=="EAPOL" or STYPE=="WPS":
                    ListSR=0
                    ExistList=-1
                    ListLen=len(List_FrMAC)
                    if ListLen!=0:
                        while ListSR<ListLen:
                            if List_FrMAC[ListSR]==FR_MAC and len(FR_MAC)==17:
                                    ExistList=ListSR
                                    if List_ToMAC[ListSR]=="" and TO_MAC!="":
                                        List_ToMAC[ListSR]=str(TO_MAC)
 
                                    if List_ToMAC[ListSR].find(TO_MAC)==-1 and len(TO_MAC)==17:
                                        List_ToMAC[ListSR]=List_ToMAC[ListSR] + " / " + str(TO_MAC)
                            if List_ToMAC[ListSR]==TO_MAC and len(TO_MAC)==17 and TO_MAC!="FF:FF:FF:FF:FF:FF":
                                ExistList=ListSR
                            if ExistList!=-1:
                                ListSR=ListLen

                            ListSR=ListSR+1
                    if ExistList==-1 and len(FR_MAC)==17 and len(TO_MAC)==17:		# NOT FOUND ON LIST
                        List_FrMAC.append(str(FR_MAC))
                        List_ToMAC.append(str(TO_MAC))
                        List_Data.append(str(GET_DATA))
                        List_Auth.append(str(GET_AUTH))
                        List_Deauth.append(str(GET_DEAUTH))
                        List_Assoc.append(str(GET_ASSOC))
                        List_Reassoc.append(str(GET_REASSOC))
                        List_Disassoc.append(str(GET_DISASSOC))
                        List_RTS.append(str(GET_RTS))
                        List_CTS.append(str(GET_CTS))
                        List_ACK.append(str(GET_ACK))
                        List_EAPOL.append(str(GET_EAPOL))
                        List_WPS.append(str(GET_WPS))

                    if ExistList!=-1:		# FOUND ON LIST
                        GET_DATA=List_Data[ExistList]
                        GET_AUTH=List_Auth[ExistList]
                        GET_DEAUTH=List_Deauth[ExistList]
                        GET_ASSOC=List_Assoc[ExistList]
                        GET_REASSOC=List_Reassoc[ExistList]
                        GET_DISASSOC=List_Disassoc[ExistList]
                        GET_RTS=List_RTS[ExistList]
                        GET_CTS=List_CTS[ExistList]
                        GET_ACK=List_ACK[ExistList]
                        GET_EAPOL=List_EAPOL[ExistList]
                        GET_WPS=List_WPS[ExistList]

                        if STYPE=="DATA" or STYPE=="QOS":
                            if TO_MAC=="FF:FF:FF:FF:FF:FF":
                                GET_DATA=str(int(GET_DATA) + 1)
                        if STYPE=="AUTHENTICATION":
                            GET_AUTH=str(int( GET_AUTH) + 1)
                        if STYPE=="DEAUTHENTICATION":
                            GET_DEAUTH=str(int(GET_DEAUTH) + 1)
                        if STYPE=="DISASSOCIATE":
                            GET_DISASSOC=str(int(GET_DISASSOC) + 1)
                        if STYPE=="ASSOCIATION":
                            GET_ASSOC=str(int(GET_ASSOC) + 1)
                        if STYPE=="REASSOCIATION":
                            GET_REASSOC=str(int(GET_REASSOC) + 1)
                        if STYPE=="REQUEST-TO-SEND":
                            GET_RTS=str(int(GET_RTS) + 1)
                        if STYPE=="CLEAR-TO-SEND":
                            GET_CTS=str(int(GET_CTS) + 1)
                        if STYPE=="ACKNOWLEDGEMENT":
                            GET_ACK=str(int(GET_ACK) + 1)
                        if STYPE=="EAPOL":
                            GET_EAPOL=str(int(GET_EAPOL) + 1)
                        if STYPE=="WPS":
                            GET_WPS=str(int(GET_WPS) + 1)
                        List_Data[ExistList]=GET_DATA
                        List_Auth[ExistList]=GET_AUTH
                        List_Deauth[ExistList]=GET_DEAUTH
                        List_Assoc[ExistList]=GET_ASSOC
                        List_Reassoc[ExistList]=GET_REASSOC
                        List_Disassoc[ExistList]=GET_DISASSOC
                        List_RTS[ExistList]=GET_RTS
                        List_CTS[ExistList]=GET_CTS
                        List_ACK[ExistList]=GET_ACK
                        List_EAPOL[ExistList]=GET_EAPOL
                        List_WPS[ExistList]=GET_WPS

                    ExistList=-1
    printl(fcolor.BRed + "                                           ","","")
    printl(fcolor.BRed + "     Analysing Completed..\r","","")


    if IsFileDirExist(resultlist)!="F":
        open(resultlist,"wb").write("" + "\n")
    ts = time.time()
    DateTimeStamp=datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')
    open(resultlist,"wb").write(tcpdump_log + "\n")
    open(resultlist,"a+b").write("Date/Time\t:" + str(DateTimeStamp) + "\n")
    open(resultlist,"a+b").write("SN\tFR MAC \t\t\tData \tAuth \tDeauth \tAssoc \tR.Asc \tD.Asc \tRTS \tCTS \tACK \tEAPOL \tWPS \tTo MAC" + "\n")
    x=0
    l=len(List_FrMAC)
    while x<l:
        open(resultlist,"a+b").write(str(x) + "\t" + List_FrMAC[x] + "\t" + List_Data[x] + "\t"  + List_Auth[x] + "\t"  + List_Deauth[x] + "\t"  + List_Assoc[x] + "\t"  + List_Reassoc[x] + "\t"  + List_Disassoc[x] + "\t"  + List_RTS[x] + "\t"  + List_CTS[x] + "\t"  + List_ACK[x] + "\t"   + List_EAPOL[x] + "\t"   + List_WPS[x] + "\t" + List_ToMAC[x] + "\n")
        x=x+1
    open(resultlist,"a+b").write("" + "\n\n")

    listlen=len(List_FrMAC)
    listsr=0
    Concern=0
    WPSDetected=0
    if listlen!=0:
        printl(fcolor.BRed + "\r","","")
        while listsr<listlen:
            if int(List_Deauth[listsr])>=10:
                FrMAC=str(List_FrMAC[listsr]).replace(" / FF:FF:FF:FF:FF:FF","").replace("FF:FF:FF:FF:FF:FF / ", "").replace("FF:FF:FF:FF:FF:FF","")
                ToMAC=str(List_ToMAC[listsr]).replace(" / FF:FF:FF:FF:FF:FF","").replace("FF:FF:FF:FF:FF:FF / ", "").replace("FF:FF:FF:FF:FF:FF","")
                Concern=Concern+1
                if ToMAC=="":
                    ToMAC = fcolor.BRed + "Broadcast"
                print ""
                printc (".",fcolor.BGreen + "Deauth Flood detected calling from [ " + fcolor.BBlue + str(FrMAC) + fcolor.BGreen + " ] to [ " + fcolor.BBlue + str(ToMAC) + fcolor.BGreen + " ]  with " + fcolor.BYellow + str(List_Deauth[listsr]) + fcolor.BGreen + " deauth packets","")
                AType="DEAUTH"
                RtnESSID=GetMACDetail(FrMAC,ToMAC,AType)
#                if str(Privacy)=="WPA" or str(Privacy)=="WPA2" or str(Privacy)=="WPA2" or str(Privacy)=="WPA2WPA (OPN)" or str(Privacy)=="WPA2 (OPN)" or str(Privacy)=="WPAOPN" or str(Privacy)=="WPA2OPN" or str(Privacy)=="WPA (OPN)" or str(Privacy)=="WPA2/WPA" or Cipher=="CCMP/TKIP" or Cipher=="CCMP" or Cipher=="TKIP":
                printc (" ",fcolor.BGreen + "Handshake Found [ " + fcolor.BBlue + str(List_EAPOL[listsr]) + fcolor.BGreen + " ] ","")

            if int(List_Data[listsr])>=200:
                Concern=Concern+1
                FrMAC=str(List_FrMAC[listsr]).replace(" / FF:FF:FF:FF:FF:FF","").replace("FF:FF:FF:FF:FF:FF / ", "").replace("FF:FF:FF:FF:FF:FF","")
                ToMAC=str(List_ToMAC[listsr]).replace(" / FF:FF:FF:FF:FF:FF","").replace("FF:FF:FF:FF:FF:FF / ", "").replace("FF:FF:FF:FF:FF:FF","")
                ToMAC=str(ToMAC).replace(" / FF:FF:FF:FF:FF:7F","").replace("FF:FF:FF:FF:FF:7F / ", "").replace("FF:FF:FF:FF:FF:7F","")
                print ""
                printc (".",fcolor.BGreen + "Unusual Data sending from from [ " + fcolor.BBlue + str(FrMAC) + fcolor.BGreen + " ] to [ " + fcolor.BBlue + str(ToMAC) + fcolor.BGreen + " ] with " + fcolor.BYellow + str(List_Data[listsr]) + fcolor.BGreen +  " Broadcast data packets","")
                AType="BCDATA"
                RtnESSID=GetMACDetail(FrMAC,ToMAC,AType)
            if int(List_Auth[listsr])>=5:
                Concern=Concern+1
                FrMAC=str(List_FrMAC[listsr]).replace(" / FF:FF:FF:FF:FF:FF","").replace("FF:FF:FF:FF:FF:FF / ", "").replace("FF:FF:FF:FF:FF:FF","")
                ToMAC=str(List_ToMAC[listsr]).replace(" / FF:FF:FF:FF:FF:FF","").replace("FF:FF:FF:FF:FF:FF / ", "").replace("FF:FF:FF:FF:FF:FF","")
                ToMAC=str(ToMAC).replace(" / FF:FF:FF:FF:FF:7F","").replace("FF:FF:FF:FF:FF:7F / ", "").replace("FF:FF:FF:FF:FF:7F","")
                print ""
                printc (".",fcolor.BGreen + "Unusual amount of authentication sent from [ " + fcolor.BBlue + str(FrMAC) + fcolor.BGreen + " ] to [ " + fcolor.BBlue + str(ToMAC) + fcolor.BGreen + " ] with " + fcolor.BYellow + str(List_Auth[listsr]) + fcolor.BGreen + " authentication request detected","")
                AType="AUTH"
                RtnESSID=GetMACDetail(FrMAC,ToMAC,AType)
            if int(List_WPS[listsr])>=3:
                Concern=Concern+1
                WPSDetected=1
                FrMAC=str(List_FrMAC[listsr]).replace(" / FF:FF:FF:FF:FF:FF","").replace("FF:FF:FF:FF:FF:FF / ", "").replace("FF:FF:FF:FF:FF:FF","")
                ToMAC=str(List_ToMAC[listsr]).replace(" / FF:FF:FF:FF:FF:FF","").replace("FF:FF:FF:FF:FF:FF / ", "").replace("FF:FF:FF:FF:FF:FF","")
                ToMAC=str(ToMAC).replace(" / FF:FF:FF:FF:FF:7F","").replace("FF:FF:FF:FF:FF:7F / ", "").replace("FF:FF:FF:FF:FF:7F","")
                print ""
                printc (".",fcolor.BGreen + "EAP communication between AP and client sending from [ " + fcolor.BBlue + str(FrMAC) + fcolor.BGreen + " ] to [ " + fcolor.BBlue + str(ToMAC) + fcolor.BGreen + " ] with " + fcolor.BYellow + str(List_WPS[listsr]) + fcolor.BGreen + " EAP packets detected","")
                printc (" ",fcolor.SWhite + "Note: If constantly seeing EAP communication between this two devices, it is likely that a EAP bruteforce is in progress..","")
                AType="EAP"
                RtnESSID=GetMACDetail(FrMAC,ToMAC,AType)
            listsr = listsr +1
#    if RtnESSID!="":
#        Concern=Concern+1
#        print ""
#        printc ("i",RtnESSID,"")
#        printc (" ",fcolor.SWhite + "Note : If ESSID constantly changing, it is likely to be a rogue access point..","")
    if Concern==0:
        Result=printc ("i","<$rs$>" + fcolor.BYellow + DateTimeStamp + fcolor.SGreen + " - Did not detect any suspicious activity ...","")
#        printc ("i",fcolor.BBlue + DateTimeStamp + fcolor.SGreen + "\tDid not detect any suspicious activity ...","")
    else:
        Result=printc ("i","<$rs$>" + fcolor.BBlue + DateTimeStamp + fcolor.BRed + " - " + str(Concern) + fcolor.BWhite + " concerns found...","")

    if Concern!=0:
        print ""
    printl(fcolor.BRed + "                                           ","","")
    printl(fcolor.BRed + "" + Result,"","")
    if Concern!=0:
        print ""
    print ""

def ConvertPackets():
    captured_pcap=tmpdir + "captured"
    captured_pcap=tmpdir + "tcpdump.cap"
    tcpdump_log=tmpdir + "tcpdump.log"
    Result=DelFile(tcpdump_log,"0")
    printl(fcolor.SGreen + "     Converting captured packets... Please wait...","","")
    RewriteCSV()
    ps=subprocess.Popen("tshark -r " + str(captured_pcap) + " -n -t ad > " + str(tcpdump_log), shell=True, stdout=subprocess.PIPE,stderr=open(os.devnull, 'w'))
    ps.wait()
    if ps.returncode==0:
        return;
            
def RewriteCSV():
    captured_csv=tmpdir + "captured-01.csv"
    newcaptured_csv=tmpdir + "CapturedListing.csv"
    open(newcaptured_csv,"wb").write("" )
    if IsFileDirExist(captured_csv)=="F":
        with open(captured_csv,"r") as f:
            for line in f:
                line=line.replace("\n","")
                line=line.replace("\00","")
                open(newcaptured_csv,"a+b").write(line + "\n")





from random import randrange
from math import floor
global NullOut
DN = open(os.devnull, 'w')
DebugMode="0"
printd("Main Start Here -->")
cmdline=len(sys.argv)
TWidth=103
ProxyType="0"
tmpfile='/tmp/ipinfo'
global InfoIP
InfoIP=""
InfoIPVia=""
InfoIPFwd=""
TimeStart=""
appdir="/SYWorks/WIDS/"
PathList = ['tmp/']
tmpdir=appdir + "tmp/"
#global PrevIconCount
PrevIconCount=0
NullOut=" > /dev/null 2>&1"

 

try:
    global MONList
    MONList = []
    global MONListC
    MONListC = []
    MonCt = GetInterfaceList("MON")
    MONList=IFaceList
    GetAppName()
    CheckLinux()
    CheckPyVersion("2.6")
    os.system('clear')
    DisplayAppDetail()
    DisplayDescription()
    CheckAdmin()
    CheckAppLocation()
    CheckRequiredFiles()
    GetParameter("1")
    RETRY=0
    
    ps=subprocess.Popen("ps -A | grep 'airodump-ng'" , shell=True, stdout=subprocess.PIPE)	
    Process=ps.stdout.read()
    if Process!="":
        ps=subprocess.Popen("killall 'airodump-ng'" , shell=True, stdout=subprocess.PIPE)	
        Process=ps.stdout.read()
    ps=subprocess.Popen("ps -A | grep 'aireplay-ng'" , shell=True, stdout=subprocess.PIPE)	
    Process=ps.stdout.read()
    if Process!="":
        ps=subprocess.Popen("killall 'aireplay-ng'" , shell=True, stdout=subprocess.PIPE)	
        Process=ps.stdout.read()

    printc ("i","Monitor","")
    MonCt = GetInterfaceList("MON")
    WLANCt = GetInterfaceList("WLAN")
    if MonCt==0 and WLANCt==0:
        printc (".",fcolor.SRed + "No wireless interface detected !","")
        exit(1)

    if MonCt==0 and WLANCt!=0:
        if SELECTED_IFACE=="":
            SELECTED_IFACE=SelectInterfaceToUse()
        else:
            Rund="iwconfig " + SELECTED_IFACE + " > /dev/null 2>&1"
            result=os.system(Rund)
            if result==0:
                printc(">",fcolor.BIGray + "Interface Selection Bypassed....","")
            else:
                printc ("!!!", fcolor.BRed + "The interface specified [ " + fcolor.BWhite + SELECTED_IFACE + fcolor.BRed + " ] is not available." ,"")
                print ""
                SELECTED_IFACE=SelectInterfaceToUse()
        printc (" ", fcolor.SWhite + "Selected Interface ==> " + fcolor.BRed + str(SELECTED_IFACE),"")
        print ""
        ps=subprocess.Popen("ifconfig " + str(SELECTED_IFACE) + " up  > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE,stderr=open(os.devnull, 'w'))

    if MonCt==0:
        printc (".",fcolor.SGreen + "Enabling monitoring for [ " + fcolor.BRed + SELECTED_IFACE + fcolor.SGreen + " ]...","")
        ps=subprocess.Popen("airmon-ng  check kill  > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE,stderr=open(os.devnull, 'w'))
        ps=subprocess.Popen("airmon-ng start " + str(SELECTED_IFACE) + " > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE,stderr=open(os.devnull, 'w'))
        time.sleep (0.5)
        MonCt = GetInterfaceList("MON")

        if MonCt>=1:
            if SELECTED_MON=="":
                SELECTED_MON=SelectMonitorToUse()
            else:
                Rund="iwconfig " + SELECTED_MON + " > /dev/null 2>&1"
                result=os.system(Rund)
                if result==0:
                    printc(">",fcolor.BIGray + "Monitor Selection Bypassed....","")
                else:
                    printc ("!!!", fcolor.BRed + "The monitoring interface specified [ " + fcolor.BWhite + SELECTED_MON + fcolor.BRed + " ] is not available." ,"")
                    print ""
                    SELECTED_MON=SelectMonitorToUse()
    else:
        SELECTED_MON=SelectMonitorToUse()

    printc (" ", fcolor.SWhite + "Selected Monitoring Interface ==> " + fcolor.BRed + str(SELECTED_MON),"")
    print ""
    ps=subprocess.Popen("ifconfig " + str(SELECTED_MON) + " up  > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE,stderr=open(os.devnull, 'w'))

    x=0

    captured_pcap=tmpdir + "captured"
    while x<9999999:
        CaptureTraffic()
        ConvertPackets()
        AnalyseCaptured()
        time.sleep(1)
        x=x+1
    exit()



except (KeyboardInterrupt, SystemExit):
    printd("KeyboardInterrupt - " + str(KeyboardInterrupt) + "\n        SystemExit - " + str(SystemExit))
    print ""
    printc ("*", fcolor.BRed + "Application shutdown !!","")
    if TimeStart!="":
        result=DisplayTimeStamp("summary-a","")
    print ""
    MonCt = GetInterfaceList("MON")
    X=0
    while X<MonCt:
        PM=len(MONList)
        Y=0
        while Y<PM:
            if MONList[Y]==IFaceList[X]:
                IFaceList[Y]=""
            Y=Y+1
        X=X+1
    PM=len(IFaceList)
    Y=0
    while Y<PM:
        if IFaceList[Y]!="":
            printc (".", "Stopping " + str(IFaceList[Y]) + "....","")
            ps=Popen("airmon-ng stop " + str(IFaceList[Y]) + " > /dev/null 2>&1", shell=True, stdout=subprocess.PIPE, stderr=open(os.devnull, 'w'),preexec_fn=os.setsid)
            time.sleep(0.5)
#            ps=subprocess.Popen("airmon-ng stop " + str(IFaceList[Y]) + " > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE,stderr=open(os.devnull, 'w'))
        Y=Y+1
    ps=subprocess.Popen("killall 'airmon-ng' > /dev/null 2>&1" , shell=True, stdout=subprocess.PIPE)	
    time.sleep(0.5)

   


