
class persona:
    def __init__(self,apellido,nombre) -> None:
        self.apellido = apellido 
        self.nombre = nombre
    def __str__(self) -> str:
        return f"Apellido: {self.apellido} Nombre: {self.nombre}"
    
class alumno (persona):
    def __init__(self,apellido,nombre,numalum) -> None:
        super().__init__(apellido,nombre,numalum)
        self.numalum = numalum
    def __str__(self) -> str:
        return super().__str__() + f"Número de alumno: {self.numalum}"

alumno1 = alumno ("Amaya","Jeremias",1)
alumno2 = alumno ("Bulacio","Santiago",2)
alumno3 = alumno ("Carunchio","Julieta",3)
alumno4 = alumno ("Castillo","Maximiliano",4)
alumno5 = alumno ("Cordoba","Joaquin",5)
alumno6 = alumno ("Cordoba","Solange",6)
alumno7 = alumno ("Corzo","Juan",7)
alumno8 = alumno ("Diaz","Tobias",8)
alumno9 = alumno ("Espindola","Ludmila",9)
alumno10 = alumno ("Giupponi","Kevin",10)
alumno11 = alumno ("Lazzarini","Emiliano",11)
alumno12 = alumno ("Loza","Fabrizio",12)
alumno13 = alumno ("Luna","Ulises",13)
alumno14 = alumno ("Medina","Lucas",14)
alumno15 = alumno ("Pedraza","Tiago",15)
alumno16 = alumno ("Pedraza","Thomas",16)
alumno17 = alumno ("Quinteros","Azul",17)
alumno18 = alumno ("Riachi","Zahir",18)
alumno19 = alumno ("Rodriguez","Esteban",19)
alumno20 = alumno ("Soria","Mateo",20)
alumno21 = alumno ("Strauss","Kevin",21)
alumno22 = alumno ("Vera","Mateo",22)
alumno23 = alumno ("Vergara","Nelson",23)
print (alumno2)




    

