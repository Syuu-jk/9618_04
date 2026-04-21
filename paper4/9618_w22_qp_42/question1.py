global Jobs
Jobs = [[None for _ in range(2)] for _ in range(100)] #OF TYPE INTEGER

def Initialise():
    for i in range(100):
            for j in range(2):
                    Jobs[i][j] = -1
    global NumberOfJobs
    NumberOfJobs = 0 #OF TYPE INTEGER


def AddJob(JobID, JobPriority): #JobID and JobPriority OF TYPE INTEGER
    for i in range(100):
        if Jobs[i][0] == -1:
            Jobs[i][0] = JobID
            Jobs[i][1] = JobPriority
            print("Added")
            return
    print("Not Added")




def InsertionSort():
    #insert_index OF TYPE INTEGER
    #current_row a list of 2 elements OF TYPE INTEGER
    #current_value OF TYPE INTEGEr
    #insert_index OF TYPE INTEGER
    for i in range(100):
        insert_index = i
        current_row = Jobs[i]      
        current_value = Jobs[i][1]

        for j in range(i-1, -1, -1):
            if Jobs[j][1] > current_value:
                Jobs[j+1] = Jobs[j]   
                insert_index = j
            else:
                break

        Jobs[insert_index] = current_row 


  

def PrintArray():

    for i in range(100):
        for j in range(2):
            if Jobs[i][j] != -1:
                print(f"{Jobs[i][0]} priority {Jobs[i][1]}")
            else:
                 continue

Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)            
InsertionSort()
PrintArray()