from pdb_io import read_pdb
atoms=read_pdb("6B1E.pdb")
print(atoms)


atoms = [Atom(1,2,3), Atom(4,5,6)]
dist = atoms[0].distance(atoms[1])  # ✅ access the Atom inside the list
print(dist)

print(dist)