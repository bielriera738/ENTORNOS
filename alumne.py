class Alumne:
    def __init__(self,nom,cognoms,edat, asignatura, nota):
        self.nom=nom
        self.cognoms=cognoms
        self.edat=edat
        self.asignatura=asignatura
        self.notes=nota


    def consultar_nota(self):
        print(f"El nom és {self.nom} i la nota és {self.nota}")
            
    def ficar_nota(self,nota):
        self.nota=nova_nota
        if nova_nota>10:
            self.nota=nova_nota
        else:
            print("La nota es erronea")

    def actualitzar_edad(self,nova_edat):
        self.edat=nova_edat
    
    def consultar_dades_alumne(self):
        print(f"Nom: {self.nom}, Cognoms: {self.cognoms}, Edat: {self.edat}, Asignatura: {self.asignatura}, Nota: {self.nota}")
    