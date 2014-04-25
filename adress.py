def main():
    adress1="200.34.55.0/24"
    adress2="200.34.54.0/23"
    adress3="200.33.0.0/16"
    range1=""
    range2=""
    range3=""
    count=0
    number=0
    dict1={}
    
    listadress=[adress1, adress2, adress3]
    for index in listadress:
        for index2 in range(len(index)):
            if index[12]=="4":
                if index[index2]==".":
                    count=count+1
                if count==3:
                    range1=index.strip("/24")
                    test=list(index)
                    test[10]="255"
                    index="".join(test)
                    range2=index
                    break
            if index[13]=="3":
                if index[index2]==".":
                    count=count+1
                if count==2:
                    range1=index.strip("/23")
                    number=int(float(index[7]))*10+ int(float(index[8]))
                    number=number+1
                    result=int(number/10)
                    index[7]=str(result)
                    result=number%10
                    index[8]=str(result)
                    index[10]="255"
                    range2=index
                    break
            if index[13]=="6":
                if index[index2]==".":
                    count=count+1
                if count==2:
                    range1=index.strip("/16")
                    index[7]="255"
                    index[11]="255"
                    range2=index
                    break                 
    dict1[index]=[range1,range2]
    print (dict1)   
main()
