from RobotOM import *

app = RobotApplicationClass()
project = app.Project
structure = project.Structure

# Define load cases
def create_mass_activation_records(case, records_dict):
    """
    Creates mass activation records in a Robot load case.

    Parameters:
        case (IRobotCase): The Robot load case where records will be added.
        records_dict (dict): Dictionary where values represent load case numbers to activate mass from.
    """
    for name, case_number in records_dict.items():
        rec = case.Records.Create(IRobotLoadRecordType.I_LRT_MASS_ACTIVATION)
        rec = IRobotLoadRecord(rec)  # Cast to correct interface if needed

        rec.SetValue(IRobotMassActivationRecordValues.I_MARV_ACTIVATION_DIR, 2)  # Use global direction (XYZ)
        rec.SetValue(IRobotMassActivationRecordValues.I_MARV_SIGN, -1)          # Use sign of global dir
        rec.SetValue(IRobotMassActivationRecordValues.I_MARV_INPUT_DIR_X, 1)
        rec.SetValue(IRobotMassActivationRecordValues.I_MARV_INPUT_DIR_Y, 1)
        rec.SetValue(IRobotMassActivationRecordValues.I_MARV_INPUT_DIR_Z, 1)
        rec.SetValue(IRobotMassActivationRecordValues.I_MARV_FACTOR, 1)
        rec.SetValue(IRobotMassActivationRecordValues.I_MARV_CASE_NUM, case_number)


load_cases = {
    "DL1": {
        "Name": "Self-weight",
        "Nature": IRobotCaseNature.I_CN_PERMANENT,
        "Analysis": IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR
    },
    "DL2": {
        "Name": "Ladder and cable weight",
        "Nature": IRobotCaseNature.I_CN_PERMANENT,
        "Analysis": IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR
    },
    "SW1": {
        "Name": "Ladder and cable Ice weight",
        "Nature": IRobotCaseNature.I_CN_SNOW,
        "Analysis": IRobotCaseAnalizeType.I_CAT_STATIC_LINEAR
    },
    "MOD4": {
        "Name": "Modal",
        "Nature": IRobotCaseNature.I_CN_PERMANENT,
        "Analysis": IRobotCaseAnalizeType.I_CAT_DYNAMIC_MODAL
    },
    "MOD5": {
        "Name": "Modal with ice",
        "Nature": IRobotCaseNature.I_CN_PERMANENT,
        "Analysis": IRobotCaseAnalizeType.I_CAT_DYNAMIC_MODAL  
    } 
}
if IN[0]:
# Add cases
    i = 1
    cases = []
    for Name, Properties in load_cases.items():
        case = structure.Cases.CreateSimple(i, Properties["Name"], Properties["Nature"], Properties["Analysis"])
        case.label = Name
        i += 1
        
        z = False
        cases.append(Name)
    
        modalCases = []
        if case.Number > 3:
            modalCases.append(Name)
            modalCase = IRobotModalAnalysisParams(case.GetAnalysisParams())
            modalCase.ModesCount = 20
            modalCase.SturmVerification = True
            modalCase.Tolerance = 0.0001
            modalCase.IterationsCount = 50
            modalCase.MassMatrix = IRobotModalAnalysisMassMatrixType.I_MAMMT_CONSISTENT
            case.SetAnalysisParams(modalCase)
           
            if case.Number == 4 :
                records = {"rec2":1, "rec4":2}
                create_mass_activation_records(case, records)
                
            elif case.Number == 5 :
                records = {"rec3":3 }
                create_mass_activation_records(case, records)
            
            
         
             
             
    #structure.Cases.CreateSimple(2, load_cases["PERM2"]["Name"], load_cases["PERM21111111111"]["Nature"], load_cases["PERM2"]["Analysis"])
    #z.SetLabel(z.Label, "PERM")
        #OUT = z
    #modal_case = structure.Cases.CreateSimple(15, "Modal",  IRobotCaseAnalizeType.I_CAT_DYNAMIC_MODAL)
        #case = structure.Cases.Get(idx)
        #case.Name = name
        #case.Notes = prefix
