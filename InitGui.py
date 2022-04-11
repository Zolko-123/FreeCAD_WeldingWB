# -*- coding: utf-8 -*-
###################################################################################
#
#  InitGui.py
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
###################################################################################


import os

import WeldingWB_locator
global WeldingWB_icon, WeldingWB_path
WeldingWB_path = os.path.dirname( WeldingWB_locator.__file__ )
WeldingWB_icon = os.path.join( WeldingWB_path , 'Resources/icons/Welding.svg' )



"""
    +-----------------------------------------------+
    |            Initialize the workbench           |
    +-----------------------------------------------+
"""
class WeldingWorkbench(Workbench):

    global WeldingWB_icon
    global selectionFilter
    global _atr, QT_TRANSLATE_NOOP
    MenuText = "Welding"
    ToolTip = "Welding workbench"
    Icon = WeldingWB_icon

    def __init__(self):
        "This function is executed when FreeCAD starts"
        pass

    def Activated(self):
        "This function is executed when the workbench is activated"
        # FreeCAD.Console.PrintMessage("Activating Welding WorkBench" + '\n')
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        # FreeCAD.Console.PrintMessage("Leaving Welding WorkBench" + "\n")
        return

    def GetClassName(self):
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"

        """
    +-----------------------------------------------+
    |        This is where all is defined           |
    +-----------------------------------------------+
        """
    def Initialize(self):
        # Assembly4 version info
        # with file VERSION
        versionPath = os.path.join( WeldingWB_path, 'VERSION' )
        versionFile = open(versionPath,"r")
        version = versionFile.readlines()[1]
        WeldingWB_version = version[:-1]
        versionFile.close()
        '''
        # with file package.xml
        packageFile  = os.path.join( Asm4_path, 'package.xml' )
        metadata     = FreeCAD.Metadata(packageFile)
        Asm4_date    = metadata.Date
        Asm4_version = metadata.Version
        '''

        # check that the Assembly4 workbench is installed
        if not self.checkWorkbench('Assembly4Workbench'):
            from PySide import QtGui
            text = "This Welding workbench needs the Assembly4 workbench, please install it"
            FreeCAD.Console.PrintMessage(text+"\n")
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle( 'FreeCAD Warning' )
            msgBox.setIcon( QtGui.QMessageBox.Critical )
            msgBox.setText( text )
            msgBox.exec_()
            # FreeCADGui.updateGui()
            return
        else:
            FreeCAD.Console.PrintMessage("Initializing Welding workbench"+ ' ('+WeldingWB_version+') \n')
            # FreeCADGui.updateGui()
        
        # import all stuff
        import newFrameCmd      # creates a new App::Part container called 'Model'

        # check that the Assembly4 WB has been loaded before:
        if not 'Asm4_newLCS' in Gui.listCommands():
            Gui.activateWorkbench('Assembly4Workbench')
            Gui.activateWorkbench('WeldingWorkbench')

        # Define Menus
        # commands to appear in the Assembly4 menu 'Assembly'
        self.appendMenu("&Welding", self.weldingMenuItems())

        # Define Toolbars
        # commands to appear in the Assembly4 toolbar
        self.appendToolbar("Welding", self.weldingToolbarItems())

        # build the selection toolbar
        self.appendToolbar("Selection Filter", self.selectionToolbarItems())

        # reload GUI and workbench
        FreeCADGui.updateGui()
        Gui.activateWorkbench('Assembly4Workbench')
        Gui.activateWorkbench('WeldingWorkbench')


    """
    +-----------------------------------------------+
    |            Assembly Menu & Toolbar            |
    +-----------------------------------------------+
    """
    def weldingMenuItems(self):
        commandList = [ "Weld_newFrame",
                        "Asm4_newPart", 
                        "Asm4_newBody", 
                        "Asm4_newGroup", 
                        "Asm4_newSketch", 
                        'Asm4_createDatum',
                        "Separator",
                        "Asm4_insertLink", 
                        "Asm4_mirrorPart", 
                        "Asm4_circularArray", 
                        "Separator",
                        "Asm4_infoPart", 
                        "Asm4_makeBOM", 
                        "Asm4_Measure", 
                        'Asm4_showLcs',
                        'Asm4_hideLcs',
                        "Asm4_addVariable", 
                        "Asm4_delVariable", 
                        "Asm4_openConfigurations", 
                        ]
        return commandList

    def weldingToolbarItems(self):
        commandList = [ "Weld_newFrame",
                        "Asm4_newPart", 
                        "Asm4_newBody", 
                        "Asm4_newGroup", 
                        "Asm4_infoPart", 
                        "Asm4_mirrorPart", 
                        "Separator",
                        "Asm4_newSketch", 
                        'Asm4_createDatum',
                        "Asm4_shapeBinder",
                        "Separator",
                        "Asm4_updateAssembly",
                        "Separator",
                        'Asm4_showLcs',
                        'Asm4_hideLcs',
                        "Asm4_makeBOM", 
                        "Asm4_Measure", 
                        "Asm4_variablesCmd",
                        "Asm4_openConfigurations", 
                        ]
        return commandList


    """
    +-----------------------------------------------+
    |                 Selection Toolbar             |
    +-----------------------------------------------+
    """
    def selectionToolbarItems(self):
        # commands to appear in the Selection toolbar
        commandList =  ["Asm4_SelectionFilterVertexCmd",
                        "Asm4_SelectionFilterEdgeCmd",
                        "Asm4_SelectionFilterFaceCmd",
                        "Asm4_selObserver3DViewCmd" ,
                        "Asm4_SelectionFilterClearCmd"]
        return commandList


    """
    +-----------------------------------------------+
    |                Contextual Menus               |
    +-----------------------------------------------+
    """
    def ContextMenu(self, recipient):
        # This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        contextMenu  = ['Asm4_gotoDocument'  ,
                        'Asm4_showLcs'       ,
                        'Asm4_hideLcs'       ,
                        'Asm4_applyConfiguration']

        self.appendContextMenu("", "Separator")
        self.appendContextMenu("", contextMenu)  # add commands to the context menu
        self.appendContextMenu("", "Separator")



    """
    +-----------------------------------------------+
    |               helper functions                |
    +-----------------------------------------------+
    """
    def checkWorkbench( self, workbench ):
        # checks whether the specified workbench (a 'string') is installed
        listWB = Gui.listWorkbenches()
        hasWB = False
        for wb in listWB.keys():
            if wb == workbench:
                hasWB = True
        return hasWB


    def dot(self):
        FreeCAD.Console.PrintMessage(".")
        FreeCADGui.updateGui()


    
"""
    +-----------------------------------------------+
    |          actually make the workbench          |
    +-----------------------------------------------+
"""
wb = WeldingWorkbench()
Gui.addWorkbench(wb)



