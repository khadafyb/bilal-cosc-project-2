#Put your name, contact info and date
#khadafy bilal khadafy.bilal@marquette.edu 10/3/19

#Make sure you change the file name to First_Name_Last_Name_Project_2.py
#Do not upload a TXT file for your projects
#defines the pay output of package 1
def s1(hours, overtimehour,medicalcost,dentalcost,visioncost,retire):
    pay=((hours*17.00)+(overtimehour*25.5)*14)
    print(pay, "is you net pay")
    print(overtimehour*25.5, "is your overtime pay")
    print((hours*17.00)*14 ,"is your base pay")
    print(pay, "is your gross pay")
    print(17,"is hourly rate")
    if retire==1:
            retirecost=pay-(.3*pay)
    else:
        retirecost=0
    payf=((hours*17.00)+(overtimehour*25.5)*14)
    return payf
#defines the pay output of package 2
def s2(hours, overtimehour,medicalcost,dentalcost,visioncost,retire):
    pay=((hours*22.00)+(overtimehour*33.00))*14-dentalcost-medicalcost-visioncost
    print(pay, "is your net pay")
    print((overtimehour*33.00)*14, "is your overtime pay")
    print((hours*22.00)*14, "is your base pay")
    print(dentalcost+medicalcost+visioncost, "total deductions")
    print((((hours*22.00)+(overtimehour*33.00))*14),"is gross pay")
    print("medical deductable: ", medicalcost)
    print("vision deductable: ", visioncost)
    print("retire cost:",retirecost)
    print("dental deductable: ", dentalcost)
    print(22, "is hourly rate")
    payf=((hours*22.00)+(overtimehour*33.00))*14-dentalcost-medicalcost-visioncost-retirecost
    if retire==1:
            retirecost=pay-(.3*pay)
    else:
        retirecost=0
    return payf
#defines the pay output of package 3

def s3(hours, overtimehour,medicalcost,dentalcost,visioncost,retire):
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
    payf=((hours*22.00)+(overtimehour*33.00))*14-dentalcost-medicalcost-visioncost-retirecost
    if retire==1:
            retirecost=pay-(.3*pay)
    else:
        retirecost=0
    return payf
#ask user for information about a new worker and returns a list that
#represent a worker
def get_worker():
    
        name=input("enter worker's name or enter quit")
        if name!='quit':
                skill = int(input("choose compesation package 1, 2, or 3"))
                hours=int(input("enter number of regular hours"))
                minsure=int(input("input medical insurance package 1,2,3"))
                dinsure=int(input("input dental insurance package 1,2,3"))
                vinsure=int(input("input visual insurance package 1,2"))
                retirementplan=int(input("input retirement option 1:yes 2:no"))
                overtimehour=int(input("enter number of overtime hours"))
                
                
        else:
                print("program terminated")
        w=[name,skill,minsure,dinsure,vinsure,retirementplan,overtimehour,hours]
        return w
       

#compute the total payroll of an individual and returns the net pay
#w is a list that represents a worker.
def compute_net_pay(worker):
        skill=worker[1]
        hours=int(worker[-1])
        overtimehour=int(worker[-2])
        medical=worker[2]
        dental=worker[3]
        vision=worker[4]
        retire=worker[-3]
        if medical ==2:
                medicalcost=75
        elif medical ==3:
                medicalcost=100
        else:
                medicalcost=0
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
        
        if skill ==1:
                return s1(hours, overtimehour,medicalcost,dentalcost,visioncost,retire)
        elif skill ==2:
                return s2(hours, overtimehour,medicalcost,dentalcost,visioncost,retire)
        elif skill==3:
                return s3(hours, overtimehour,medicalcost,dentalcost,visioncost,retire)
        else:
                print("You don't work for us")

#prints all the information about the worker w to the screen
#w is a list that represents a worker.
def print_worker(n):
        for w in worker_list:
                if n in w:
                        print(w)
                else:
                        print("worker not in list")
                



#computes the total hours of all the workers in the w_list
#w_list is a list of workers.
def compute_total_hours(worker_list):
        accumulatorhour=0
        for w in worker_list:
                accumulatorhour+=int(w[-2]+w[-1])
        return accumulatorhour


#computes the total net pay of all the workers in the w_list
#w_list is a list of workers.
def compute_total_net_pay(worker_list):
        accumulatorpay=0
        for worker in worker_list:
                accumulatorpay+=compute_net_pay(worker)
        return accumulatorpay

#returns the first occurrence of worker in w_list whose name is n.
#if no worker with a name n exists in w_list, return an empty list (i.e., [])
#n is a string to store a name
#w_list is a list of workers
def search_worker(name, worker_list):
    for w in worker_list:
        if name in w:
                return w
        else:
                print("does not work here")






#############MAIN PROGRAM STARTS HERE#####################
#start with an empty worker list.
worker_list = []

#complete the code below to fill in ?????
s='q'
while s !='quit' :
    worker = get_worker()
    worker_list.append(worker)
    s = input("Press y/Y to add another worker or any other key to quit")
print(worker_list)

#Searching for workers and printing detailed information about them. Fill in ???? below.
name = input("Please enter a worker name to print.")
while name in worker:
    #Demonstration of the usage of search_worker_function.
        worker = search_worker(name, worker_list) #write the appropriate arguments for this function call.

    #printing the net pay of the worker if the search was successful
        if len(worker) > 0:
                print("Here is the detailed info about worker:", worker)
                compute_net_pay(worker)
                break#only one line to a function call...
        else:
                print("No worker named", name)
        s = input("Press y/Y to search another worker or any other key to quit")


#write a code below to print the detailed information of each worker in the workers_list
#utilize the print function.
#Write yor code below.

#printing the total hours of all workers. Complete the print statement below.
totalcompute=compute_total_hours(worker_list)
print ("Total hours of all workers",totalcompute )

#printing the total net pay to all workers. Complete the print statement below.
totalpay=compute_total_net_pay(worker_list)
print("Total net pay to all workers", totalpay)



