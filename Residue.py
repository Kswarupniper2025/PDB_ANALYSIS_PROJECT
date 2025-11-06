from pdb_io import read_pdb

residues = read_pdb("6B1E.pdb")
print("Total residues:", len(residues))
print("\nFirst residue atoms:")
for atom in residues[1]:
    print(atom)