import clr
import sys
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Load Robot API
clr.AddReference(r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2024\Dynamo\2.17\Rsa\package\SAD\bin\RSA\interop.RobotOM.dll")
from RobotOM import *

def get_bar_properties():
    """
    Retrieves bar properties (Bar ID, Section Name, Material, Shape ID, Section Width) 
    from Robot Structural Analysis and stores them in a structured dictionary.

    Returns:
    dict: A dictionary containing bar properties.
    """
    try:
        # Start Robot Application
        application = RobotApplicationClass()
        
        # Ensure Robot is running
        if not application.Visible:
            application.Visible = True
            application.Interactive = 1
        
        project = application.Project
        structure = project.Structure

        # Select all bars
        selection = structure.Selections.Create(IRobotObjectType.I_OT_BAR)
        selection.FromText("all")
        selectedBars = IRobotCollection(structure.Bars.GetMany(selection))

        # Initialize dictionary
        bar_properties_dict = {}

        for i in range(selectedBars.Count):
            bar = IRobotBar(selectedBars.Get(i+1))  # Get bar object
            
            # Get Bar ID
            bar_id = bar.Number  
            bar_id_key = f"Bar_ID_{bar_id}"
            
            # Get Section Name
            try:
                section_name = bar.GetLabelName(IRobotLabelType.I_LT_BAR_SECTION)
                section_name = section_name if section_name else "N/A"
            except:
                section_name = "N/A"
                
            # Get Material Name
            try:
                material_name = bar.GetLabelName(IRobotLabelType.I_LT_MATERIAL)
                material_name = material_name if material_name else "N/A"
            except:
                material_name = "N/A"
            
            
            # Get Section Data
            try:
                section_label = IRobotLabel(structure.Labels.Get(IRobotLabelType.I_LT_BAR_SECTION, section_name))
                section_data = RobotBarSectionData(section_label.Data) if section_label else None
                
                # Extract Shape ID and Section Width
                shape_id = section_data.get_ShapeType() if section_data else -1
                shape_id = int(shape_id) if isinstance(shape_id, (int, float)) else -1
                
                section_width = section_data.GetValue(IRobotBarSectionDataValue.I_BSDV_BF) if section_data else -1.0
                section_width = float(section_width) if isinstance(section_width, (int, float)) else -1.0
                
                section_perimeter = section_data.GetValue(IRobotBarSectionDataValue.I_BSDV_SURFACE) if section_data else -1.0
                section_perimeter = float(section_perimeter) if isinstance(section_perimeter, (int, float)) else -1.0            
                
                nominal_weight = section_data.GetValue(IRobotBarSectionDataValue.I_BSDV_WEIGHT) if section_data else -1.0
                nominal_weight = float(nominal_weight/9.80665) if isinstance(nominal_weight, (int, float)) else -1.0            
                                
            except:
                shape_id = -1
                section_width = -1.0
                section_perimeter= -1.0
            
            
            # Store data in dictionary
            bar_properties_dict[bar_id_key] = {
                "Bar_ID": int(bar_id),
                "Section_Name": str(section_name) if section_name else "N/A",
                "Material": str(material_name) if material_name else "N/A",
                "Shape_ID": int(shape_id) if shape_id is not None else "Unknown",
                "Section_Width": float(section_width) if section_width is not None else "Unknown",
                "Section_perimeter": float(section_perimeter) if section_perimeter is not None else "Unknown",
                "Nominal_weight": float(nominal_weight) if nominal_weight is not None else "Unknown"
            }

        return bar_properties_dict
    
    except Exception as e:
        return f"Error: {str(e)}"

# Run function and output results to Dynamo
if IN[0]:
    OUT = get_bar_properties()
