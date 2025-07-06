class Garden:
    DEFAULT_STUDENTS = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]
    
    def __init__(self, diagram, students=None):
        # First do the validation checks
        valid_plants = {'C', 'G', 'R', 'V'}
        
        if not set(diagram.replace('\n', '')).issubset(valid_plants):
            raise ValueError("Diagram must consist of only letters CGRV.")
        
        self.rows = diagram.split('\n')
        self.students = sorted(students if students is not None else self.DEFAULT_STUDENTS)
          
    def plants(self, name): 
        '''
        get plants belonging to a given student
        TODO decide if it should be within a class or outside of it
        '''
        plant_map = {
            'V': 'Violets',
            'R': 'Radishes',
            'C': 'Clover',
            'G': 'Grass'
        }
        
        index = self.students.index(name)
        pos = index*2
        plants = []
        
        for row in self.rows:
            if pos < len(row):
                plants.extend(plant_map[p] for p in row[pos:pos+2])
        
        return plants