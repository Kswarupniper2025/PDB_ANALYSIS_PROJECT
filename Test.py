from Pdb_io import read_pdb

residue_list = read_pdb("6B1E.pdb")
# print(residue_list[:10])
residue1 = residue_list[2]
residue2 = residue_list[55]
min_dist = residue1.minimum_dist(residue2)
print(min_dist)

