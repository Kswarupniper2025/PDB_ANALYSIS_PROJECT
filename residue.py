from atom import Atom

def create_res_id(resname, resnum, chain):
    return f"{resname}.{resnum}.{chain}"

class Residue:
    
    def __init__(self):
        self.id = None
        self.atoms = []
        self.resname = None
        self.resnum = None
        self.chain = None

    def set_data(self, pdb_line):
        self.resname = pdb_line[17:20].lstrip().rstrip()
        self.resnum = pdb_line[22:26].lstrip().rstrip()
        self.chain = pdb_line[21]
        self.id = create_res_id(self.resname, self.resnum, self.chain)
        # print(self)

    def minimum_dist(self, other_res):
        min_dist = 9999  
        for a1 in self.atoms:
            for a2 in other_res.atoms:
                d = a1.distance(a2)
                if d < min_dist:
                    min_dist = d
        return min_dist

       

    def __repr__(self):
        return f"<name= {self.resname}, num= {self.resnum}, chain= {self.chain}, numAtoms = {len(self.atoms)}>"
