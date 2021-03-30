class Hospital():
    def __init__(self,capacity):
        self.bed_cap=capacity
        self.patients= []
    
    #method check for availabe beds 
    def available_beds(self):
        return self.bed_cap-len(self.patients)
    
    #method to admit patient
    def admit_patient(self,name):
        if not self.available_beds():
             return False
        self.patients.append(name)
        return True
Hospital1 = Hospital(5)
patient_list= ["g","a","g","a","n","d"]
for patient in patient_list:
    if Hospital1.admit_patient(patient):
        print(f"admitted {patient} to the hospital.")
    else:
        print(f"failed to be admitted {patient} to the hospital.")
    
