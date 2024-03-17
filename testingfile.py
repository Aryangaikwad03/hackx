import pytesseract
import PIL.Image
import mysql.connector
import cv2

myconfig=r"--psm 6 --oem 3"
text=pytesseract.image_to_string(PIL.Image.open("test9.jpg"), config=myconfig)
text1=text.strip()
print(text1)
pairs = text1.split("\n")

dict = {}
for pair in pairs :
    key, value = pair.split(":", 1)
    key=key.strip()
    value=value.strip()
    dict[key] = value
print(dict)
dict1= list(dict.values())


mydb = mysql.connector.connect(host ="localhost",user="root",password="root",port ="3306",database="Hackx")
mycursor = mydb.cursor()

value_list =[dict1]


#mycursor.execute('CREATE TABLE test1(Name varchar(255),Sap_id varchar(255));')

query = "INSERT INTO test1(Name,Sap_id)VALUES(%s,%s)"
mycursor.executemany(query, value_list)

#mycursor.execute('CREATE TABLE Data(ID INT,Name varchar(255));')
# a = [(2,"Ayan"),(3,"Sharu")]

#
# #
mycursor.execute('SELECT*FROM test1;')
test1s = mycursor.fetchall()
for Stu in test1s:
     print(Stu)