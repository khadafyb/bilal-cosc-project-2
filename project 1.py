#user input
def user_input():
    name=input("enter worker's name")
    skill = int(input("choose compesation package 1, 2, or 3"))
    hours=int(input("enter number of regular hours"))
    minsure:(int(input("input medical insurance package 1,2,3"))
    dinsure:(int(input("input dental insurance package 1,2,3"))
    vinsure:(int(input("input visual insurance package 1,2"))
    retirementplan:(int(input("input retirement option 1:yes 2:no"))
    overtimehour=int(input("enter number of overtime hours"))
                    
#defining skill level packages additions

else:
    print("skill level does not include benefit package")
if medical ==2:
    medicalcost=75
    print(medicalcost)
elif medical ==3:
    medicalcost=100
    print(medicalcost)
else:
    medicalcost=0
    print(medicalcost)

if dental==2:
    dentalcost=20
elif dental==3:
    dentalcost=30
else:
    dentalcost=0

if vision==2:
    visioncost=5
else:
    visioncost=0
#calculating totals
                    
def s1():
    pay=((hours*17.00)+(overtimehour*25.5)*14)
    print(y, "is you net pay")
    print(overtimehour*25.5, "is your overtime pay")
    print((hours*17.00)*14 ,"is your base pay")
    print(y, "is your gross pay")
    print(17,"is hourly rate")
def s2():
    pay=((hours*22.00)+(overtimehour*33.00))*14-dentalcost-medicalcost-visioncost
    print(z, "is your net pay")
    print((overtimehour*33.00)*14, "is your overtime pay")
    print((hours*22.00)*14, "is your base pay")
    print(dentalcost+medicalcost+visioncost, "total deductions")
    print((((hours*22.00)+(overtimehour*33.00))*14),"is gross pay")
    print("medical deductable: ", medicalcost)
    print("vision deductable: ", visioncost)
    print("dental deductable: ", dentalcost)
    print(22, "is hourly rate")
def s3():
    pay=((hours*25.00)+(overtimehour*37.5)*14)-dentalcost-medicalcost-visioncost
    print(pay, "is your net pay")
    print((overtimehour*37.50)*14, "is your overtime pay")
    print((hours*25.00)*14, "is your base pay")
    print(dentalcost+medicalcost+visioncost, "total deductions")
    print((((hours*25.00)+(overtimehour*37.50)))*14,"is gross pay")
    print("medical deductable: ", medicalcost)
    print("vision deductable: ", visioncost)
    print("dental deductable: ", dentalcost)
    print(25, "is hourly rate")
#executing specific skill package calculations based on which skill package is chosen    
def compute_net_pay(w)
    if skill ==1:
        s1()
    elif skill ==2:
        s2()
    elif skill==3:
        s3()
    else:
        print("You don't work for us")
def compute_total_hours(w_list)
def compute_total_net_pay(w_list)

