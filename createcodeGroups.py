import sys
import clr
import inspect
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference(r"C:\Program Files\Autodesk\Robot Structural Analysis Professional 2024\Dynamo\2.17\Rsa\package\SAD\bin\RSA\interop.RobotOM.dll")
from RobotOM import *
# Inputs.
group_data = IN[1] # codegroups described in excel

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
        
        RDmServer = IRDimServer(application.Kernel.GetExtension("RDimServer"))
        RDmServer.Mode = 1  # Steel design mode
        RDmStream = RDmServer.Connection.GetStream()
        RDmGrps = RDmServer.GroupsService
        
        #Delete any existing groups
        group_ids = [RDmGrps.Get(i).UsrNo for i in range(1, RDmGrps.Count + 1)]
        for group_id in reversed(group_ids):
            try:
                RDmGrps.Delete(group_id)  # Delete the group
            except Exception as e:
                OUT = f"❌ Error deleting Steel Group {group_id}: {e}"
                
        for group_name, bar_list in group_data.items():
            RDmStream = RDmServer.Connection.GetStream()  # Get a new stream
            RDmStream.Clear()  # Clear previous assignments

            # Create a new group
            group_id = RDmGrps.Count + 1  # Unique ID for each group
            RDmGrp = RDmGrps.New(0, group_id) 
            RDmGrp.Name = group_name  # Assign group name
            RDmStream.WriteText(bar_list)  # Convert list to text format for Robot
            RDmGrp.SetMembList(RDmStream)
            
            RDmGrps.Save(RDmGrp)

        #GroupNo = 10  # Unique ID for the group
        #RDmGrp1 = RDmGrps.New(0, GroupNo)  # Default settings
        #RDmGrp1.Material = "S275"  # Steel Grade S275
        #RDmGrp1.Name = "Beams"
        #RDmStream = RDmServer.Connection.GetStream()
        #RDmStream.Clear()
        #RDmStream.WriteText(GROUP)  # Assign bars 1, 2, 3 to this group
        #RDmGrp1.SetMembList(RDmStream)
        
        #RDmGrps.Save(RDmGrp1) 
        #selection = structure.Selections.Create(IRobotObjectType.I_OT_BAR)
        #selection.FromText("all")
        #selectedBars = IRobotCollection(structure.Bars.GetMany(selection))     
        #bars = IRobotCollection(structure.Bars.GetAll())
        
            #section_data = application.Project.Preferences.Sections.Get(section_name)

            #section_label = structure.Labels.Sections.Get(br.SectionID)  # Get assigned section label
            #section_label = structure.Labels.Get(I_LT_BAR)  # Get assigned section label
            
            #flange_width = section_label.GetValue(IRobotBarSectionDataValue.I_BSDV_BF)
            #bar_flange_widths.append([bar_id, section_label.Name, flange_width])
            #end_node_id = br.get_EndNode()
            #node = IRobotNode(structure.Nodes.Get(end_node_id))
            #x, y, z = node.X, node.Y, node.Z
            #end_node_data.append([end_node_id, x, y, z])
            #barLength.append(br.GetLabel(length))
            #barsList.append(br.get_EndNode())
        #enumerator = bars.GetEnumerator()
        #while enumerator.MoveNext():
            #bar = enumerator.Current
            #barsList.append(bar)
        
        #listBarNumbers = []
        OUT = RDmGrps
        #OUT = dir(br.GetLabelName(IRobotLabelType.))
    except Exception as e:
        OUT = f"{e}"
