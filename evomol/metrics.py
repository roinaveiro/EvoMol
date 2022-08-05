from rdkit import DataStructs, Chem
from rdkit.Chem import AllChem
import numpy as np

from rdkit.Chem import RDConfig
from rdkit.Chem.rdmolfiles import MolToSmiles, MolFromSmiles
import os
import sys


class SimilarityTrain():

    self.smis_train = np.loadtxt("datasets/millad.txt", dtype=object)
    self.mols_train  = [MolFromSmiles(smi) for smi in smis_train]

    def similarity(self, ref_mol):

        ref_mol = AllChem.GetMorganFingerprintAsBitVect(ref_mol, 3, 2048) 
        mol_list = [AllChem.GetMorganFingerprintAsBitVect(x, 3, 2048) for x in self.mols_train] 
        
        sims = DataStructs.BulkTanimotoSimilarity(ref_mol, mol_list)
        
        return np.mean(sims)

    def get_similarity(self, ref_mol):


        similarity = self.similarity(ref_mol)
        return similarity



if __name__ == "__main__":
    pass

