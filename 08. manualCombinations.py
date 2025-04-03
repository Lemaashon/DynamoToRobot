from RobotOM import *

app = RobotApplicationClass()
project = app.Project
structure = project.Structure


load_combinations = {
    "SLS": {"1": 1, "2": 1, "3": 1},
    "ULS": {"1": 1.35, "2": 1.35, "3": 1.5},
    "ALS": {"1":1, "2": 1, "3": 0.3}
}

if IN[0]:
    i= structure.Cases.FreeNumber
    for caseName, factors in load_combinations.items():
    
        if "SLS" in caseName:
               comb = IRobotCaseCombination(structure.Cases.CreateCombination(i,caseName, IRobotCombinationType.I_CBT_SLS, IRobotCaseNature.I_CN_PERMANENT, IRobotCaseAnalizeType.I_CAT_COMB )) 
        elif "ULS" in caseName:
               comb = IRobotCaseCombination(structure.Cases.CreateCombination(i,caseName, IRobotCombinationType.I_CBT_ULS, IRobotCaseNature.I_CN_PERMANENT, IRobotCaseAnalizeType.I_CAT_COMB ))  
        elif "ALS" in caseName:
               comb = IRobotCaseCombination(structure.Cases.CreateCombination(i,caseName, IRobotCombinationType.I_CBT_ALS, IRobotCaseNature.I_CN_PERMANENT, IRobotCaseAnalizeType.I_CAT_COMB ))                

        for caseNumber, factor in factors.items():

            comb.CaseFactors.New(int(caseNumber), factor)
        i+=1
