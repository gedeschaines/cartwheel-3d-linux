'''
Created on 2009-08-25

Basic controller editor

@author: beaudoin
'''
import sys
sys.path += ['.']

import OpenGL.GLUT
OpenGL.GLUT.glutInit(sys.argv)


try:
    import wx
except ImportError as ee:
    print("Error: wx installed improperly?! - {0}".format(ee.msg))
    sys.exit(1)

try:
    import App
except ImportError as ee:
    print("Error: App installed improperly ?! - {0}".format(ee.msg))
    sys.exit(1)

import math

movieResolution = (1280,720)
movieSetup = False  # True if we want a movie
glMovie = False     # True if we're only interested in recording the GL canvas
                    # False if we want a "screen cast"

glCanvasSize = wx.DefaultSize
size =  wx.DefaultSize

showConsole = True
if movieSetup:
    if glMovie:
        glCanvasSize = movieResolution
        showConsole = False
    else:
        size = movieResolution

app = App.SNMApp("Style Editor", glCanvasSize = glCanvasSize, size = size, showConsole = showConsole)

try:
    import UI
except ImportError as ee:
    print("Error: UI installed properly? - {0}".format(ee.msg))
    sys.exit(1)
    
try:
    import Utils
except ImportError as ee:
    print("Error: Utils installed properly? - {0}".format(ee.msg))
    sys.exit(1)

try:
    import MathLib
except ImportError as ee:
    print("Error: MathLib installed properly? - {0}".format(ee.msg))
    sys.exit(1)
    
try:
    import GLUtils
except ImportError as ee:
    print("Error: GLUtils installed properly? - {0}".format(ee.msg))
    sys.exit(1)

try:
    import Physics
except ImportError as ee:
    print("Error: Physics installed properly? - {0}".format(ee.msg))
    sys.exit(1)

try:
    import Core
except ImportError as ee:
    print("Error: Core installed properly? - {0}".format(ee.msg))
    sys.exit(1)
    
try:
    import PyUtils
except ImportError as ee:
    print("Error: PyUtils installed properly? - {0}".format(ee.msg))
    sys.exit(1)
    
from App import InstantChar

from App import KeyframeEditor

# Create the desired tool sets
print("Create desired tool sets")
toolPanel = app.getToolPanel()
print("Get animation ToolSet")
animationToolSet = UI.ToolSets.Animation(toolPanel)
if not movieSetup:
    optionsToolSet = UI.ToolSets.Options(toolPanel)
    optionsToolSet._toolSet.setOpen(False)
print("Get Camera ToolSet")  
cameraToolSet = UI.ToolSets.Camera(toolPanel)
cameraToolSet._toolSet.setOpen(False)

instantChar = InstantChar.Model()
if not movieSetup:
    print("Get Snapshot ToolSet")
    controllerSnapshotToolSet = UI.ToolSets.SnapshotTree(toolPanel)
    controllerSnapshotToolSet._toolSet.setOpen(False)
    app.setSnapshotToolSet(controllerSnapshotToolSet)
    print("Get Controller Tree ToolSet")
    controllerTreeToolSet = UI.ToolSets.ControllerTree(toolPanel)
    controllerTreeToolSet._toolSet.setOpen(False)

print("Add Curve Editor Tools")
glCanvas = app.getGLCanvas()
glCanvas.addGLUITool( UI.GLUITools.CurveEditorCollection )

#from Data.Frameworks import DefaultFramework
#from Data.Frameworks import DanceFramework
#from Data.Frameworks import WalkFramework


#####################
## BEGIN Custom for Instant Character
print("Create Instant Character")
character = instantChar.create()  # NOTE: this calls app.deleteAllObjects!!

#controller = PyUtils.load( "Characters.BipV3.Controllers.CartoonySneak", character )
#controller = PyUtils.load( "Characters.BipV3.Controllers.ZeroWalk", character )
#controller = PyUtils.load( "Characters.BipV3.Controllers.VeryFastWalk_5-43_0-4", character )
#controller = PyUtils.load( "Characters.BipV3.Controllers.jog_8-76_0-33", character )
#controller = PyUtils.load( "Characters.BipV3.Controllers.run_21-57_0-38_0-10", character )
#controller = PyUtils.load( "Characters.BipV3.Controllers.FastWalk_3-7_0-53", character )
controller = PyUtils.load( "Characters.BipV3.Controllers.EditableWalking", character )
#controller = PyUtils.load( "Data.Temp.EditableWalking1", character )
#controller = PyUtils.load( "Temp.Cartoony", character )
#controller = PyUtils.load( "Temp.TipToe", character )
print("Set controller stance")
controller.setStance( Core.LEFT_STANCE );
instantChar.connectController(False)

#character.loadReducedStateFromFile( "Data/Characters/BipV3/Controllers/runState.rs" )
###character.loadReducedStateFromFile( "Data/Temp/State_0.rs" )
print("Create keyframeEditor")
keyframeEditor = KeyframeEditor.Model()
keyframeEditor.displayInterface(False)

## END
#####################

######################
## BEGIN DUMMY STUFF

#staircase = App.Scenario.Staircase( position=(0,0,5), rightRampHeight = 1, stepCount = 22, leftRampHeight = 1, angle = math.pi/4.0 )
staircase = App.Scenario.Staircase( staircaseWidth = 0.9, threadDepth = 0.5 , riserHeight = 0.05,
                                    stepCount = 4, position=(0.0,0.0,3.0), angle = 0.0,   
                                    leftRampHeight = 1.0, rightRampHeight = 1.0 )
staircase.load()
app.setStaircase(staircase)

#PyUtils.convertController("../../scoros5/data/controllers/bipV3/fWalk_3.sbc")

#ctrl2 = PyUtils.copy( app.getController(0), char )

## END DUMMY STUFF
######################

try:
   # Initial snapshot was taken within instantChar.connectController(),
   # but take another if staircase instantiated.
   if staircase: 
       aSnapshot = app.getSnapshotTree().takeSnapshot()
       ###app.getSnapshotToolSet().update()  # not needed; handled by Observers
except NameError:
    pass


if movieSetup:
    app.captureScreenShots(True)

# ... And here we go!!
app.MainLoop()
app.Destroy()
