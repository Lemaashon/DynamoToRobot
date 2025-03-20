import clr
clr.AddReference(r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2024\Dynamo\2.17\Rsa\package\SAD\bin\RSA\interop.RobotOM.dll")
from RobotOM import *

# Start Robot Application
robot = RobotApplicationClass()
project = robot.Project
structure = project.Structure

# Inputs: List of member IDs and the predefined label name in Robot
member_ids = [145,146];  # List of member IDS
label_name = "0.95l"  # Member type name

# Check if the label exists
if structure.Labels.Exist(IRobotLabelType.I_LT_MEMBER_TYPE, label_name):
    # Retrieve the existing label
    member_label = structure.Labels.Get(IRobotLabelType.I_LT_MEMBER_TYPE, label_name)
    
    # Loop through the list of members and assign the label
    for member_id in member_ids:
        if structure.Bars.Exist(member_id):  # Ensure the bar exists
            bar = IRobotBar(structure.Bars.Get(member_id))
            bar.SetLabel(IRobotLabelType.I_LT_MEMBER_TYPE, label_name)
    
    OUT = f"Label '{label_name}' assigned to members: {member_ids}"
else:
    OUT = f"Label '{label_name}' does not exist in Robot."
