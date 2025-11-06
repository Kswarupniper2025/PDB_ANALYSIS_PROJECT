class Atom:
    def __init__(self):
        self.id = None
        self.x = None
        self.y = None
        self.z = None
        self.coord = None
        self.name = None
        self.serial = None
        self.resname = None
        self.resnum = None
        self.chain =  None
        self.occup = None
        self.bfactor = None

    def __repr__(self):
        return f'<serial={self.serial},name={self.name},resname={self.resname},resid={self.resnum}>'

    def set_data(self, pdb_line):
        self.x = float(pdb_line[30:38])
        self.y = float(pdb_line[38:46])
        self.z = float(pdb_line[46:54])
        self.coord =[self.x,self.y,self.z]
        self.occup = float(pdb_line[54:60].strip() or 0.0)
        self.name = pdb_line[12:16].strip()
        self.serial = pdb_line[6:11].strip()
        self.resname = pdb_line[17:20].strip()
        self.resnum = pdb_line[22:26].strip()
        self.bfactor = float(pdb_line[60:66].strip() or 0.0)
        self.chain = pdb_line[21].strip()

    def distance(self, atom):
        d2 = (self.x - atom.x) ** 2 + (self.y - atom.y) ** 2 + (self.z - atom.z) ** 2
        return d2 ** 0.5
