from atom import Atom
# from residue import Residue,create_res_id

def read_pdb(filename):
    atoms = []
    residue_list = []
    current_residue = []
    prev_resid = None

    with open(filename) as f:
        for line in f:
            line = line.lstrip().rstrip()
            if not line:
                continue

            if line.startswith("ATOM") or line.startswith("HETATM"):
                atom = Atom()
                atom.set_data(line)

                if prev_resid is None:
                    prev_resid = atom.resid
                    current_residue.append(atom)
                else:
                    if atom.resid == prev_resid:
                        current_residue.append(atom)
                    else:
                        residue_list.append(current_residue)
                        current_residue = [atom]
                        prev_resid = atom.resid

        if current_residue:
            residue_list.append(current_residue)

    return residue_list


