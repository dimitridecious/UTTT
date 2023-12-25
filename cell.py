class Cell:
    #constructor for cell class, has a value (string) and occupied status (bool)
    def __init__(self, width, height, occupied:bool, value:str = 'Z'):
        self.width = width
        self.height = height
        self.value = value
        self.occupied = occupied


    #Cell methods go here
    
    