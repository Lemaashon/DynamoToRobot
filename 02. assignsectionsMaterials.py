import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Line
clr.AddReference(r"C:\Users\BCS\AppData\Roaming\Dynamo\Dynamo Revit\2.19\packages\Structural Analysis for Dynamo\bin\DynamoSimulationRSA.dll")
from DynamoSimulation.RSA.AnalyticalModel import AnalyticalBar


# Inputs
panel_name = IN[0]  # Example: "Panel_2"
vertical_member_groups = IN[1]  # Dictionary of vertical members from the previous script
section_name = IN[2]  # Section name (e.g., "HEA 200")
material_name = IN[3]  # Material name (e.g., "S355")



def get_members_by_panel(panel_name, vertical_member_groups):
    """
    Retrieves all vertical member geometries in a given panel.

    Parameters:
    panel_name (str): Name of the panel (e.g., "Panel_1").
    vertical_member_groups (dict): Dictionary containing vertical members grouped by panel.

    Returns:
    list: List of Dynamo geometries for the specified panel.
    """
    return [member[0] for member in vertical_member_groups.get(panel_name, [])]

def assign_section_and_material(analytical_bars, section_name, material_name):
    """
    Assigns a section and material name to a list of analytical bars.

    Parameters:
    analytical_bars (list): List of analytical bars.
    section_name (str): Name of the section to assign.
    material_name (str): Name of the material to assign.

    Returns:
    list: Updated list of analytical bars.
    """
    if not analytical_bars:
        return "Error: No bars provided."

    if not section_name:
        return "Error: No section name provided."

    if not material_name:
        return "Error: No material name provided."

    try:
        # Apply section
        updated_bars = AnalyticalBar.SetSectionByName(analytical_bars, section_name)

        # Apply material
        updated_bars = AnalyticalBar.SetMaterialByName(updated_bars, material_name)

        return updated_bars
    except Exception as e:
        return f"Error: {str(e)}"

# Retrieve geometry for the specified panel
retrieved_geometry = get_members_by_panel(panel_name, vertical_member_groups)
assigned_geometry = assign_section_and_material(retrieved_geometry, section_name, material_name)

# Assign section and material 
OUT = vertical_member_groups
