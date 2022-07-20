class haralickResult:
    
    def __init__(self, gcm, ener, entr, homog, cont, dis, ASM, cor):
        self.matriz_cooc = gcm
        self.energy = ener
        self.entropy = entr
        self.homogeneity = homog
        self.contrast = cont
        self.dissimilarity = dis
        self.ASM = ASM
        self.correlation = cor
        