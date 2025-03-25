import clr
clr.AddReference(r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2024\Dynamo\2.17\Rsa\package\SAD\bin\RSA\interop.RobotOM.dll")
from RobotOM import *

# Start Robot Application
robot = RobotApplicationClass()
project = robot.Project
structure = project.Structure

# Retrieve all existing member definition labels
member_labels = structure.Labels.GetAvailableNames(IRobotLabelType.I_LT_BAR_RELEASE)

# Create a dictionary to store retrieved data

#existing_definitions = {}
labels= []
# Loop through labels and extract data
for i in range(member_labels.Count):
    label = member_labels.Get(i + 1)  # Robot index starts at 1
    
#    label_name = label.Data
    labels.append(label )
#    label_data = label.Data  # Get buckling data

    # Extracting buckling parameters
#    Ly = label_data.GetValue(IRDimLengthDataType.I_DMDLDT_LENGTH_Y)
#    Lz = label_data.GetValue(IRDimLengthDataType.I_DMDLDT_LENGTH_Z)
#    SwayY = label_data.GetValue(IRDimBucklingDataType.I_DMDBDT_BUCKLING_Y)
#    SwayZ = label_data.GetValue(IRDimBucklingDataType.I_DMDBDT_BUCKLING_Z)

    # Store in dictionary
#    existing_definitions[label_name] = {
#        "Buckling_Length_Y": Ly,
#        "Buckling_Length_Z": Lz,
#        "Sway_Y": SwayY,
#        "Sway_Z": SwayZ
#    }

OUT = labels
