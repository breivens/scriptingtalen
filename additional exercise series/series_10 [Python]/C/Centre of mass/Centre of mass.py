class Atom:
    elements = {'Ru': 101.07, 'Re': 186.207, 'Rf': 261.0, 'Rg': 272.0, 'Ra': 226.0254,
                'Rb': 85.4678, 'Rn': 222.0, 'Rh': 102.9055, 'Be': 9.012182, 'Ba': 137.327,
                'Bh': 262.0, 'Bi': 208.9804, 'Bk': 247.0, 'Br': 79.904, 'Uuh': 292.0,
                'H': 1.00794, 'P': 30.97376, 'Os': 190.2, 'Es': 252.0, 'Hg': 200.59,
                'Ge': 72.61, 'Gd': 157.25, 'Ga': 69.723, 'Pr': 140.9077, 'Pt': 195.08,
                'Pu': 244.0642, 'C': 12.011, 'Pb': 207.2, 'Pa': 213.0359, 'Pd': 106.42,
                'Cd': 112.411, 'Po': 208.9824, 'Pm': 145.0, 'Hs': 265.0, 'Uuq': 289.0,
                'Uup': 288.0, 'Uus': 293.0, 'Uuo': 294.0, 'Ho': 164.9303, 'Hf': 178.49,
                'K': 39.0983, 'He': 4.002602, 'Md': 258.0, 'Mg': 24.305, 'Mo': 95.94,
                'Mn': 54.93805, 'O': 15.9994, 'Mt': 266.0, 'S': 32.066, 'W': 183.85,
                'Zn': 65.39, 'Eu': 151.965, 'Zr': 91.224, 'Er': 167.26, 'Ni': 58.6934,
                'No': 259.0, 'Na': 22.98977, 'Nb': 92.90638, 'Nd': 144.24, 'Ne': 20.1797,
                'Np': 237.0482, 'Fr': 223.0, 'Fe': 55.847, 'Fm': 257.0, 'B': 10.811,
                'F': 18.9984, 'Sr': 87.62, 'N': 14.00674, 'Kr': 83.8, 'Si': 28.0855,
                'Sn': 118.71, 'Sm': 150.36, 'V': 50.9415, 'Sc': 44.95591, 'Sb': 121.757,
                'Sg': 263.0, 'Se': 78.96, 'Co': 58.9332, 'Cn': 285.0, 'Cm': 247.0,
                'Cl': 35.4527, 'Ca': 40.078, 'Cf': 251.0, 'Ce': 140.115, 'Xe': 131.29,
                'Lu': 174.967, 'Cs': 132.9054, 'Cr': 51.9961, 'Cu': 63.546,
                'La': 138.9055, 'Li': 6.941, 'Tl': 204.3833, 'Tm': 168.9342, 'Lr': 260.0,
                'Th': 232.0381, 'Ti': 47.88, 'Te': 127.6, 'Tb': 158.9253, 'Tc': 98.0,
                'Ta': 180.9479, 'Yb': 173.04, 'Db': 262.0, 'Dy': 162.5, 'Ds': 271.0,
                'I': 126.9045, 'U': 238.0289, 'Y': 88.90585, 'Ac': 227.0728,
                'Ag': 107.8682, 'Uut': 284.0, 'Ir': 192.22, 'Am': 243.0614,
                'Al': 26.98154, 'As': 74.92159, 'Ar': 39.948, 'Au': 196.9665,
                'At': 209.9871, 'In': 114.818}

    def __init__(self, element, position):
        self.element = element
        self.position = position

    def __repr__(self):
        x, y, z = self.position
        return f"Atom('{self.element}', ({x:.2f}, {y:.2f}, {z:.2f}))"

    def __str__(self):
        return f"{self.element}-atom with mass {self.mass():.3f} on position {self.position}"

    def mass(self):
        return Atom.elements.get(self.element, None)


class Molecule:
    def __init__(self, name=""):
        self.name = name
        self.atoms = list()

    def addAtom(self, atom):
        self.atoms.append(atom)

    def readPDB(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            while line := file.readline():
                if line[:6] == "ATOM  ":
                    x, y, z = map(lambda l: float(l.strip()), (line[31:39], line[39:47], line[47:55]))
                    self.addAtom(Atom(line[77:79].strip(), (x, y, z)))

    def mass(self):
        return sum(atom.mass() for atom in self.atoms)

    def masscentre(self):
        x, y, z = 0, 0, 0
        for atom in self.atoms:
            x += atom.mass() * atom.position[0]
            y += atom.mass() * atom.position[1]
            z += atom.mass() * atom.position[2]
        return x / self.mass(), y / self.mass(), z / self.mass()
