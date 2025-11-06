from atom import Atom
from residue import Residue, create_res_id

def read_pdb(filename):
    residue_list = []
    curr_residue = None

    with open(filename) as f:
        for line in f:
            line=line.lstrip().rstrip()
            if not line:
                continue

            if line.startswith("ATOM") or line.startswith("HETATM"):
                atom = Atom()
                atom.set_data(line)

                atom_res_id = create_res_id(atom.resname,atom.resnum,atom.chain)
                if curr_residue is None or curr_residue.id != atom_res_id:
                    residue = Residue()
                    residue.set_data(line)
                    residue.atoms.append(atom)
                    curr_residue = residue
                    residue_list.append(residue)
                else:
                    curr_residue.atoms.append(atom)
    return residue_list


            