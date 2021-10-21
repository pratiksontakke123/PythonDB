import  mysql.connector as mycon

con=mycon.connect(host='bzhwycvxazf9gx13focv-mysql.services.clever-cloud.com',user='ujdw7mbcfwibgnu8',password='WwaSxxPbROpjMLle7M8p',database='bzhwycvxazf9gx13focv')
curs=con.cursor()

curs.execute("select * from books ")
data=curs.fetchall()
#print(data)
if data:
    no=int(input('Enter book code : '))
    prc=int(input('Enter book price '))
    curs.execute("update books set price=%d where bookcode=%d " %(prc,no))

    data=curs.fetchall()
    print('Price updated successfully')
else:
    print('book not found')



print(data)

con.close()
