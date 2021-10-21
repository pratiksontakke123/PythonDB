import  mysql.connector as mycon

con=mycon.connect(host='bzhwycvxazf9gx13focv-mysql.services.clever-cloud.com',user='ujdw7mbcfwibgnu8',password='WwaSxxPbROpjMLle7M8p',database='bzhwycvxazf9gx13focv')
curs=con.cursor()
curs.execute("select * from books where category='romance'")
data=curs.fetchone()
print(data)


if data:
    print('Book is available ')

else:
    print('No books found')

con.close()
