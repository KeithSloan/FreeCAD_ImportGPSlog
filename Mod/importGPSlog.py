# -*- coding: utf8 -*-

#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2017 Keith Sloan <keith@sloan-home.co.uk>               *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         * 
#*   Acknowledgements :                                                    *
#*                                                                         *
#*                                                                         *
#***************************************************************************
__title__="FreeCAD - Glider GPS Log importer"
__author__ = "Keith Sloan <keith@sloan-home.co.uk>"
__url__ = ["https://github.com/KeithSloan/FreeCAD_ImportGPSlog"]

printverbose = False

import FreeCAD, os, sys, re
if FreeCAD.GuiUp:
    import FreeCADGui
    gui = True
else:
    if printverbose: print("FreeCAD Gui not present.")
    gui = False


import Part


if open.__module__ == '__builtin__':
    pythonopen = open # to distinguish python built-in open function from the one declared here


#try:
#    _encoding = QtGui.QApplication.UnicodeUTF8
#    def translate(context, text):
#        "convenience function for Qt translator"
#        from PySide import QtGui
#        return QtGui.QApplication.translate(context, text, None, _encoding)
#except AttributeError:
#    def translate(context, text):
#        "convenience function for Qt translator"
#        from PySide import QtGui
#        return QtGui.QApplication.translate(context, text, None)

def open(filename):
    "called when freecad opens a file."
    global doc
    global pathName
    docname = os.path.splitext(os.path.basename(filename))[0]
    doc = FreeCAD.newDocument(docname)
    if filename.lower().endswith('.igc'):
        processGPSlog(filename)
    return doc

def insert(filename,docname):
    "called when freecad imports a file"
    global doc
    global pathName
    groupname = os.path.splitext(os.path.basename(filename))[0]
    try:
        doc=FreeCAD.getDocument(docname)
    except NameError:
        doc=FreeCAD.newDocument(docname)
    if filename.lower().endswith('.igc'):
        processGPSlog(filename)


def processGPSlog(filename):
    global doc

    FreeCAD.Console.PrintMessage('Import GPS logfile : '+filename+'\n')
    if printverbose: print ('ImportGPSlog Version 0.1')
    # f = pythonopen(filename, 'r')
    with pythonopen(filename,'rb') as f:
       while True:
          line=f.readline()
          if not line: break
          processLine(line)
    f.close()
    if printverbose:
        print('End ImportGPSlog')
    FreeCAD.Console.PrintMessage('End processing GPS log file\n')
    doc.recompute()

class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

def processLine(line):
    while switch(line[0]):
        if case('A'):
           processA(line) 
           break

        if case('B'):
           processB(line) 
           break

        if case('C'):
           processC(line) 
           break
        
        if case('D'):
           processD(line) 
           break

        if case('E'):
           processE(line) 
           break

        if case('F'):
           processF(line) 
           break

        if case('G'):
           processG(line) 
           break

        if case('H'):
           processH(line) 
           break

        if case('I'):
           processI(line) 
           break

        if case('J'):
           processJ(line) 
           break

        if case('K'):
           processK(line) 
           break

        if case('L'):
           processL(line) 
           break

        print "Default"
        break

def processA(line) :
	print "Manufacturer ID"

def dm2dd(degrees, minutes, direction):
#    print minutes
#    print degrees
    dd = float(degrees) + float(minutes)/60;
    if direction == 'E' or direction == 'N':
        dd *= -1
    return dd;

def processB(line) :
    	print "Fix  :"
	print "Lat  : "+line[7:9]+" "+line[9:11]+"."+line[11:14]+" "+line[14]
	lat = dm2dd(line[7:9],line[9:11]+"."+line[11:14],line[14])
	print "Lat degrees : "+str(lat) 
	print "Long : "+line[15:18]+" "+line[18:20]+"."+line[20:23]+" "+line[23]
	long = dm2dd(line[15:18],line[18:20]+"."+line[20:23],line[23])
	print "Long degrees : "+str(long)
 
def processC(line) :
	print "Task/Declaration"

def processD(line) :
	print "Diffrential GPS"

def processE(line) :
	print "Pilot Event" 

def processF(line) :
	print "Inital Satellite Constellation"

def processG(line) :
        print "Security"

def processH(line) :
	print "Header : "+line

def processI(line) :
	print "Fix extension"

def processJ(line) :
 	print "Data List"

def processK(line) :
	print "Extension Data"

def processL(line) :
	print "Logbook"
