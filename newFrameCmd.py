#!/usr/bin/env python3
# coding: utf-8
# 
# newAssemblyCmd.py 



import math, re, os

from PySide import QtGui, QtCore
import FreeCADGui as Gui
import FreeCAD as App
import Part

import Asm4_libs as Asm4
import WeldingWB_libs as Weld




class makeFrame:
    """
    +-----------------------------------------------+
    |          creates the Assembly4 Model          |
    |             which is an App::Part             |
    |    with some extra features and properties    |
    +-----------------------------------------------+
    
def makeAssembly():
    assembly = App.ActiveDocument.addObject('App::Part','Assembly')
    assembly.Type='Assembly'
    assembly.addProperty( 'App::PropertyString', 'AssemblyType', 'Assembly' )
    assembly.AssemblyType = 'Part::Link'
    assembly.newObject('App::DocumentObjectGroup','Constraints')
    return assembly

    """
    def GetResources(self):
        tooltip  = "Create a new frame for welding\n"
        iconFile = os.path.join( Weld.iconPath , 'Welding.svg')
        return {"MenuText": "New Frame", "ToolTip": tooltip, "Pixmap" : iconFile }


    def IsActive(self):
        if App.ActiveDocument:
            return(True)
        else:
            return(False)


    # the real stuff
    def Activated(self):
        # check whether there is already Model in the document
        frame = App.ActiveDocument.getObject('WeldFrame')
        if frame:
            if frame.TypeId=='App::Part':
                Asm4.warningBox("This document already contains a valid welding frame, please use it")
                # set the Type to Assembly
                frame.Type = 'WeldFrame'
            else:
                message  = "This document already contains another FreeCAD object called \"Frame\", "
                message += "but it's of type \""+frame.TypeId+"\", unsuitable for welding frame. Aborting."
                Asm4.warningBox(message)
            # abort
            return

        # there is no object called "Assembly"
        # create a group 'Parts' to hold all parts in the assembly document (if any)
        # must be done before creating the assembly
        sectionsGroup = App.ActiveDocument.getObject('Sections')
        if sectionsGroup is None:
            sectionsGroup = App.ActiveDocument.addObject( 'App::DocumentObjectGroup', 'Sections' )

        # create a new App::Part called 'Assembly'
        frame = App.ActiveDocument.addObject('App::Part','WeldFrame')
        # set the type as a "proof" that it's an Assembly
        frame.Type='WeldFrame'
        # add an LCS at the root of the Model, and attach it to the 'Origin'
        lcs0 = frame.newObject('PartDesign::CoordinateSystem','LCS_Origin')
        lcs0.Support = [(frame.Origin.OriginFeatures[0],'')]
        lcs0.MapMode = 'ObjectXY'
        lcs0.MapReversed = False
        
        # move existing parts and bodies at the document root to the Parts group
        # not nested inside other parts, to keep hierarchy
        if sectionsGroup.TypeId != 'App::DocumentObjectGroup':
            Asm4.warningBox( 'There seems to already be a Sections object, you might get unexpected behaviour' )

        # recompute to get rid of the small overlays
        frame.recompute()
        App.ActiveDocument.recompute()



# add the command to the workbench
Gui.addCommand( 'Weld_newFrame', makeFrame() )



