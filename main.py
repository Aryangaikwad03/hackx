import pytesseract
import PIL.Image
import mysql.connector
import cv2



myconfig=r"--psm 6 --oem 3"
mydb = mysql.connector.connect(host="localhost", user="root", password="root", port="3306", database="Hackx")
mycursor = mydb.cursor()
#mycursor.execute('CREATE TABLE test1(Name varchar(255),Sap_id varchar(255));')
for i in range(1,4) :
    path = input("enter the path to the docment : ")
    text = pytesseract.image_to_string(PIL.Image.open(path), config=myconfig)
    text1 = text.strip()
    print(text1)
    pairs = text1.split("\n")

    dict = {}
    for pair in pairs:
        key, value = pair.split(":", 1)
        key = key.strip()
        value = value.strip()
        dict[key] = value
    print(dict)
    dict1 = list(dict.values())



    value_list = [dict1]



    query = "INSERT INTO test1(Name,Sap_id)VALUES(%s,%s)"
    mycursor.executemany(query, value_list)
    mydb.commit()
    # mycursor.execute('CREATE TABLE Data(ID INT,Name varchar(255));')
    # a = [(2,"Ayan"),(3,"Sharu")]

    #
    #
    mycursor.execute('SELECT*FROM test1;')
    test1s = mycursor.fetchall()
    for Stu in test1s:
        print(Stu)

