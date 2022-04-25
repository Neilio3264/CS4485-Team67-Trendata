class History:
    def __init__(self, time, inpatient, creatinine, aki):
        self._time = time
        self._inpatient = inpatient
        self._creatinine = creatinine
        self._aki = aki
    
    def time(self):
        '''
        The datetime string for the record
        '''
        return self._time
    
    def inpatient(self):
        '''
        The boolean value of if the patient was an inpatient or not
        '''
        return self._inpatient
    
    def creatinine(self):
        '''
        The recorded c level for the patient
        '''
        return self._creatinine
    
    def aki(self):
        '''
        The aki classification for this record
        '''
        return self._aki