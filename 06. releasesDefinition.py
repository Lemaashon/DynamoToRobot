import clr
clr.AddReference(r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2024\Dynamo\2.17\Rsa\package\SAD\bin\RSA\interop.RobotOM.dll")
from RobotOM import *

# Start Robot Application
robot = RobotApplicationClass()
project = robot.Project
structure = project.Structure

# Inputs: List of member IDs and the predefined label name in Robot
member_ids = IN[0]  # Example: [1, 2, 3, 10, 12]
label_name = "Pinned-Pinned"  # Example: "Pinned-Pinned", "Fixed-Pinned"
member_labels = structure.Labels.GetAvailableNames(IRobotLabelType.I_LT_BAR_RELEASE)
labels= []
# Loop through labels and extract data
for i in range(member_labels.Count):
    label = member_labels.Get(i + 1)  # Robot index starts at 1
    labels.append(label)
# Check if the label exists
if label_name in labels:
    # Retrieve the existing label
    member_label = structure.Labels.Get(IRobotLabelType.I_LT_BAR_RELEASE, label_name)
    
    # Loop through the list of members and assign the label
    for member_id in member_ids:
        if structure.Bars.Exist(member_id):  # Ensure the bar exists
            bar = IRobotBar(structure.Bars.Get(member_id))
            bar.SetLabel(IRobotLabelType.I_LT_BAR_RELEASE, label_name)
    
    OUT = f"Label '{label_name}' assigned to members: {member_ids}"
else:
    OUT = f"Label '{label_name}' does not exist in Robot."
