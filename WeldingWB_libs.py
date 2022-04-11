#!/usr/bin/env python3
# coding: utf-8
#
# LGPL
# Copyright HUBERT Zoltán
#
# libraries for FreeCAD's Welding workbench



import os
wbPath   = os.path.dirname(__file__)
iconPath = os.path.join( wbPath, 'Resources/icons' )
libPath  = os.path.join( wbPath, 'Resources/library' )

from PySide import QtGui, QtCore
import FreeCADGui as Gui
import FreeCAD as App
from FreeCAD import Console as FCC



"""
    +-----------------------------------------------+
    |           Object helper functions             |
    +-----------------------------------------------+
"""
def cloneSection(obj):
    container = obj.getParentGeoFeatureGroup()
    result = None
    if obj.Document and container:
        #result = obj.Document.copyObject(obj, False)
        result = obj.Document.addObject('App::Link', obj.Name)
        result.LinkedObject = obj
        result.Label = obj.Label
        container.addObject(result)
        result.recompute()
        #container = result.getParentGeoFeatureGroup()
        #if container:
        container.recompute()
        #if result.Document:
        result.Document.recompute()
    return result



"""
    +-----------------------------------------------+
    |       Create default Welding properties       |
    +-----------------------------------------------+
"""
def makeWeldProperties( obj, reset=False ):
    # property AssemblyType
    if not hasattr(obj,'AssemblyType'):
        obj.addProperty( 'App::PropertyString', 'AssemblyType', 'Assembly' )
    # property AttachedBy
    if not hasattr(obj,'AttachedBy'):
        obj.addProperty( 'App::PropertyString', 'AttachedBy', 'Assembly' )
    # property AttachedTo
    if not hasattr(obj,'AttachedTo'):
        obj.addProperty( 'App::PropertyString', 'AttachedTo', 'Assembly' )
    # property AttachmentOffset
    if not hasattr(obj,'AttachmentOffset'):
        obj.addProperty( 'App::PropertyPlacement', 'AttachmentOffset', 'Assembly' )
    # property SolverId
    if not hasattr(obj,'SolverId'):
        obj.addProperty( 'App::PropertyString', 'SolverId', 'Assembly' )
    if reset:
        obj.AssemblyType = ''
        #obj.AttachedBy = ''
        #obj.AttachedTo = ''
        #obj.AttachmentOffset = App.Placement()
        obj.SolverId = ''
    return


class setCustomIcon():
    def __init__( self, obj, iconFile):
        #obj.Proxy = self
        self.customIcon = os.path.join( iconPath, iconFile )

    def getIcon(self):                                              # GetIcon
        return self.customIcon



# checks whether there is a FreeCAD Assembly at the root of the active document
def getWeldFrame():
    if App.ActiveDocument:
        # should we check for AssemblyType=='Part::Link' ?
        assy = App.ActiveDocument.getObject('Assembly')
        if assy and assy.TypeId=='App::Part'                        \
                and assy.Type == 'Assembly'                         \
                and assy.getParentGeoFeatureGroup() is None:
            return assy
        else:
            # legacy check for compatibility
            model = checkModel()
            if model:
                #FCC.PrintWarning('This is a legacy Asm4 Model\n')
                return model
    return None



