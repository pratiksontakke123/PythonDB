import  mysql.connector as mycon

con=mycon.connect(host='bzhwycvxazf9gx13focv-mysql.services.clever-cloud.com',user='ujdw7mbcfwibgnu8',password='WwaSxxPbROpjMLle7M8p',database='bzhwycvxazf9gx13focv')
curs=con.cursor()


no=int(input('Enter bookcode : '))
curs.execute("select * from books where bookcode = %d" %no)


rec=curs.fetchone()
print(rec)

if rec:
    print('book found')
else:
    print('No book available for this code ')
con.close()




#data=curs.fetchone()
#print(data)

