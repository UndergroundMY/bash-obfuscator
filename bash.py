# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
BR = '\033[0;33m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

#Parent Directory
P = "/storage/emulated/0/"

os.system("clear")

banner = """
{} ╰╮╰╮╰╮
{}╭━━━━━━━╮╱ {}*╔═══❖•ೋ°  °ೋ•❖═══╗*
{}╰━━━━━━━╯╱   {}вaѕн  фвғυѕcaтфr
{}┃{}╭╭╮┏┏┏┏{}┣━╮{}*╚═══❖•ೋ°  °ೋ•❖═══╝*
{}┃{}┃┃┃┣┣┣┣{}┃╱┃  {}тeaм ➢ υпdergrфυпd cyвer тeaм
{}┃{}╰╰╯┃┃┗┗{}┣━╯  {}ѕcrιpт ➢ мade вy lyпхнacĸer
{}╰━━━━━━━╯ 
""".format(W,W,W,W,C,W,Y,W,W,W,Y,W,G,W,Y,W,G,W)

banner2 = """
{}[{}1{}]{} eпcrypт      {}[{}2{}]{} decrypт   	{}[{}3{}]{} eхιт
""".format(G,W,G,W,G,W,G,W,G,W,G,W)

print banner
print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + "ѕcrιpт" + G + " ➢ " + W + P )
       f = open(P + sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "фυтpυт" + G + " ➢ " + W + P )
       f = open(P + out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + P + out + " > tes.sh")
       os.remove(P + out)
       os.system("mv -f tes.sh " + P + out)
       print (sukses + "dфпe..")

   except KeyboardInterrupt:
       print (eror + " ѕтфpped!")
   except IOError:
       print (eror + " ғιle пфт ғфυпd!")

def enkrip():
   try:
       script = raw_input(ask + W + "ѕcrιpт" + G + " ➢ " + W + P )
       output = raw_input(ask + W + "фυтpυт" + G + " ➢ " + W + P )
       os.system("bash-obfuscate " + P + script + " -o " + P + output )
       print (sukses + "dфпe..")
   except KeyboardInterrupt:
       print (eror + " ѕтфpped!")
   except IOError:
       print (eror + " ғιle пфт ғфυпd!")

def exit():
	os.system("cd $HOME")

choose = raw_input(W + "Choose" + G + " ➢ ")

if choose == "1" or choose == "01":
   enkrip()
elif choose == "2" or choose == "02":
   dekrip()
elif choose == "3" or choose == "03":
	exit()
else:
   print (eror + " Wrong input")
