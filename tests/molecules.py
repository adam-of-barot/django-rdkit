SMILES_SAMPLE = (
    'NN=C(c1ccccc1)c1ccccc1',
    'COc1ccc(C=NO)cc1',
    'c1ccc(C(=NC(c2ccccc2)c2ccccc2)c2ccccc2)cc1',
    'c1ccc(N=C(c2ccccc2)c2ccccc2)cc1',
    'Cc1nc2ccccc2c(O)c1-c1ccccc1',
    'CCC1=[O+][Cu]2([O+]=C(CC)C1)[O+]=C(CC)CC(CC)=[O+]2',
    'O=C(O)C(Cc1ccccc1)c1ccccc1',
    'CCc1cnc(C)cc1N',
    'Cc1nc2ccccc2c(Oc2ccccc2)c1-c1ccccc1',
    'N#CC(c1ccccc1)C(c1ccccc1)c1ccccc1',
    'CC(C#N)N(C)C',
    'CC(=O)C1Cc2ccccc2C1=O',
    'O=S(Cc1ccccc1)Cc1ccccc1',
    'CC(c1ccccc1)C(C)(C#N)c1ccccc1',
    'Cc1nc(O)nc2c1CCCC2',
    'c1ccc(C(NC(c2ccccc2)c2ccccc2)c2ccccc2)cc1',
    'Oc1nnc(-c2ccccc2)c2ccccc12',
    'CC(C)(C(N)=O)c1ccccc1',
    'O=C(O)C(c1ccccc1)(c1ccccc1)c1ccccc1',
    'CCC[N+](CCC)(CCC)Cc1ccccc1',
    'Cc1cc(C)c(CC(=O)c2ccccc2)c(C)c1',
    'COC(c1ccccc1)(c1ccccc1)c1ccccc1',
    'CCC(CC)(CC)C(OC(=O)c1ccccc1C(=O)O)c1ccccc1',
    'CC(=O)C(Cc1ccccc1)(c1ccccc1)c1ccccc1',
    'O=S(=O)(Cc1ccccc1)Cc1ccccc1',
    'CC(C)(C)OC(=O)C(c1ccccc1)c1ccccc1',
    'N#CC(Cc1ccccc1)(c1ccccc1)c1ccccc1',
    'CC(=Cc1ccccc1)c1ccccc1',
    'N#CC(Cc1ccccc1)c1ccccc1',
    'CC(O)(c1ccccc1)C(C(=O)O)c1ccccc1',
    'CC(c1ccccc1)C(C(=O)O)c1ccccc1',
    'ON=Cc1ccc(Cl)cc1',
    'COC(c1ccccc1)c1ccccc1',
    'O=C(NC(c1ccccc1)c1ccccc1)c1ccccc1',
    'C[N+](C)(Cc1ccccc1)Cc1ccccc1',
    'C(=CC1=[O+][Cu]2([O+]=C(C=Cc3ccccc3)CC(c3ccccc3)=[O+]2)[O+]=C(c2ccccc2)C1)c1ccccc1',
    'ON=Cc1ccc2c(c1)OCO2',
    'CCOC(=O)C(NC(=O)c1ccccc1)C(=O)OCC',
    'Nc1ccc(Cl)nc1',
    'c1ccc(C(c2ccccc2)N2CCCCC2)cc1',
    'CCOC(=O)c1cnc2c(C)c(Cl)ccc2c1O',
    'CCN(CC)C(=O)C=Cc1ccccc1',
    'C[N+](C)(C)Cc1ccc([N+](=O)[O-])cc1',
    'C[N+](C)(C)Cc1cccc([N+](=O)[O-])c1',
    'O=C(CC(c1ccccc1)N1CCCCC1)c1ccccc1',
    'COC(c1ccccc1)(c1ccccc1)N(C)C',
    'CN(C)CCC(=O)c1ccccc1',
    'CCCCN(CCCC)C(C)=O',
    'Cc1ccccc1CO',
    'CCN(CC)CCC(=O)OC',
    'ClC(Cc1ccccc1)c1ccccc1',
    'CC(=O)CC(=O)CC(C)C',
    'CCN(CC)CCC#N',
    'COc1ccc(CC#N)cc1',
    'CN(Cc1ccccc1)c1ccccc1',
    'COc1ccc(C(C)(C)C#N)cc1',
    'CCC(CC)(c1ccccc1)C(O)c1ccccc1',
    'CC(=Cc1ccccc1)OC(=O)c1ccccc1',
    'CCN(CC)C(C)=O',
    'CCCCOC(c1ccccc1)N1CCCCC1',
    'CCCCCCCCN(CC)CC',
    'CCOC(C)c1ccccc1',
    'CCC(=O)N(CC)CC',
    'CCCCOC(OCCCC)c1ccccc1',
    'C[Si](C)(C)Cc1ccccc1',
    'CCN(CC)CCCCCCNc1ccnc2cc(Cl)ccc21',
    'CC(=O)c1cc(C)c(O)c(C)c1',
    'CCOC(=O)c1ccc(S(=O)(=O)N(CC)CC)cc1',
    'CC(=O)c1ccncc1',
    'Cc1cc(C)c(C[N+](C)(C)C)c(C)c1C',
    'OCC(F)(F)C(F)F',
    'OCC(F)(F)C(F)(F)C(F)(F)C(F)F',
    'OCC(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)F',
    'O=C(CCCC(=O)OCC(F)(F)C(F)(F)C(F)(F)C(F)F)OCC(F)(F)C(F)(F)C(F)(F)C(F)F',
    'CC(CC(=O)OCC(F)(F)C(F)(F)C(F)(F)C(F)F)CC(=O)OCC(F)(F)C(F)(F)C(F)(F)C(F)F',
    'CC(C)(C)O[Si](OCC(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)F)(OCC(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)F)OC(C)(C)C',
    'O=C(OCC(F)(F)C(F)(F)C(F)(F)C(F)F)c1ccccc1C(=O)OCC(F)(F)C(F)(F)C(F)(F)C(F)F',
    'CN1c2ccccc2Sc2ccccc21',
    'CCN1c2ccccc2Sc2ccccc21',
    'CCN1c2ccccc2S(=O)c2cc([N+](=O)[O-])ccc21',
    'CN1c2ccccc2S(=O)c2ccccc21',
    'O=C(CCl)c1ccc2c(c1)Nc1ccccc1S2',
    'CC[N+]([O-])(CC)CCCN1c2ccccc2S(=O)c2ccccc21',
    'COC(=O)c1cccc2c1Nc1ccccc1S2',
    'CC(=O)N1c2ccccc2Sc2ccc(C(=O)CCl)cc21',
    'CC(=O)N1c2ccccc2Sc2c3ccccc3ccc21',
    'c1ccc(-c2nc3cc4ccccc4cc3s2)cc1',
    'O=C1CSc2ccccc2N1',
    'C1CN([Se][Se]N2CCOCC2)CCO1',
    'CCN(CC)N=O',
    'CCCN(CCC)N=O',
    'CC(C)CN(CC(C)C)N=O',
    'CCCCN(CC)N=O',
    'CCCCC(CC)CN(CC(CC)CCCC)N=O',
    'CN(N=O)c1ccccc1',
    'O=NN1CCCCC1',
    'O=NN1CCOCC1',
    'CCCCOC(=O)C=CC(=O)OCCCC',
    'O=C(O)CBr',
    'O=C(O)CCl',
)
