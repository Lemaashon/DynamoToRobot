import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference(r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2025\Dynamo\3.0\Rsa\package\SAD\bin\Interop.RobotOM.dll")
from RobotOM import *
# The inputs to this node will be stored as a list in the IN variables.
if IN[0]:
    try:
        # Start Robot Application
        application = RobotApplicationClass()
        
        # Ensure Robot is visible and interactive
        if not application.Visible:
            application.Visible = True
            application.Interactive = 1
        
        project = application.Project
        structure = project.Structure
        labels = structure.Labels
        loads = structure.Cases
        ProjectPrefs = project.Preferences
         
         # list load cases
        loadCases = loads.GetAll()
        for i in range(loadCases.Count):
            try: 
                load = IRobotSimpleCase(structure.Cases.Get(i+1))
                loadCount = load.Records.Count
                for i in range(loadCount):
                    load.Records.Delete(i+1)
            except Exception as e:
                OUT = f"{e}"
    except Exception as e:
        OUT = f"{e}"
