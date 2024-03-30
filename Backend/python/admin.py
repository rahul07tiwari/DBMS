import mysql.connector
#-------------------------------------------------------------------Admin Login Panel-------------------------------------------------------------------------#

def add_rec():
    mydb = mysql.connector.connect(host="localhost",user="root", password="1234@",database="Kaushtubha")
    mycursor = mydb.cursor()
    sql="INSERT INTO admin values(%s,%s,%s)"
    sr_no = int(input("Enter The Sr_no"))
    admin_name = input("enter your name")
    admin_pass = input("enter your Password")
    val = (sr_no,admin_name,admin_pass)
    mycursor.execute(sql,val)
    mydb.commit()
add_rec()
