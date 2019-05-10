import xlrd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()

train = "train.xlsx"
Book1 = xlrd.open_workbook(train)
first_sheet = Book1.sheet_by_index(0)


def totalMales():
    totalMale = 0
    for row in range(first_sheet.nrows):
        if str(first_sheet.cell(row,4).value) == "male":
            totalMale = totalMale+1
        else:
            pass
    return(totalMale)
        
def totalFemales():
    totalFemale = 0
    for row in range(first_sheet.nrows):
        if str(first_sheet.cell(row,4).value) == "female":
            totalFemale = totalFemale+1
        else:
            pass
    return(totalFemale)
        
        
def MaleSurvive():
    maleSurvive = 0
    for row in range(first_sheet.nrows):
        if str(first_sheet.cell(row,4).value) == "male" and (first_sheet.cell(row,1).value)== 1:
            maleSurvive = maleSurvive+1
        else:
            pass
    return(maleSurvive)
        
def FemaleSurvive():
    femaleSurvive = 0
    for row in range(first_sheet.nrows):
        if str(first_sheet.cell(row,4).value) == "female" and (first_sheet.cell(row,1).value)==1:
            femaleSurvive=femaleSurvive+1
        else:
            pass
    return(femaleSurvive)
        

def plot():    
    y1= [totalMales()]
    x1=["Total Males"]
    y2= [totalFemales()]
    x2=["Total Females"]
    y3= [MaleSurvive()]
    x3=["Male Survivors"]
    y4= [FemaleSurvive()]
    x4=["Female Survivors"]

    plt.bar(x1, y1, label="Total Males")
    plt.bar(x2, y2, label="Total Females")
    plt.bar(x3, y3, label="Male Surviors")
    plt.bar(x4, y4, label="Female Surviors")
    plt.xlabel("Type of Passenger")
    plt.ylabel("Number of Passengers")
    plt.title("Titanic Data")
    plt.legend()

    plt.show()
    
    train = "train.xlsx"
    Book1 = xlrd.open_workbook(train)
    first_sheet = Book1.sheet_by_index(0)  
 
print(first_sheet.row_values(0))

plot()






