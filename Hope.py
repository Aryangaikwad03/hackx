import pytesseract
import PIL.Image
import mysql.connector

myconfig=r"--psm 6 --oem 3"
mydb = mysql.connector.connect(host="localhost", user="root", password="root", port="3306", database="Hackx")
mycursor = mydb.cursor()
# mycursor.execute('CREATE TABLE fir(name varchar(255), date varchar(255), year_of_birth varchar(355), nationality '
#                  'varchar(255),uid int, pass_no varchar(255),adhar_no int,adress varchar(255),occupation varchar(255),'
#                  'phone_no int,reason_for_delay varchar(255),cpmplaint varchar(2556)); ')

for i in range(1,4) :
    res = input("Do you want to upload the image? :")
    if res == "no":
        break
    else :
        path = input("enter the path to the document : ")
        text = pytesseract.image_to_string(PIL.Image.open(path), config=myconfig)
        text1 = text.strip()
        print(text1)
        pairs = text1.split("\n")
        print(pairs)

        dict = {}
        for pair in pairs:
            pair_split = pair.split(":", 1)
            if len(pair_split) == 2:
                key, value = pair.split(":", 1)
                key = key.strip()
                value = value.strip()
                dict[key] = value

        print(dict)
        dict1 = list(dict.values())
        value_list = [dict1]
        query = ("INSERT INTO fir(name , date , year_of_birth , nationality ,uid, pass_no,adhar_no,adress,"
                 "occupation ,phone_no,reason_for_delay,cpmplaint)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
        mycursor.executemany(query, value_list)
        mydb.commit()
        mycursor.execute('SELECT*FROM fir;')
        test1s = mycursor.fetchall()
        for Stu in test1s:
            print(Stu)

for j in range(1,4) :
    print("Do you want to enter the list of suspects ?")
    ans = input("Enter the answer :")
    if ans == "no":
        print("okay, thank you")
        break
    else :
        # mycursor.execute('CREATE TABLE suspect(Sr_no int,Name varchar(255), Alias varchar(255),Relative_name varchar('
        #                  '255));')
        for k in range(1, 4):
            path1 = input("enter the path to the document for suspects : ")
            text3 = pytesseract.image_to_string(PIL.Image.open(path1), config=myconfig)
            text4 = text3.strip()
            pairs1 = text4.split("\n")

            dict1 = {}
            for pair in pairs1:
                pair_split = pair.split(":", 1)
                if len(pair_split) == 2:
                    key, value = pair.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    dict1[key] = value

            print(dict1)
            dict2 = list(dict1.values())

            value_list1 = [dict2]

            query1 = "INSERT INTO suspect(Sr_no,Name , Alias ,Relative_name)VALUES(%s,%s,%s,%s);"
            mycursor.executemany(query1, value_list1)
            mydb.commit()
