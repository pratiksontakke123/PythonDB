import  mysql.connector as mycon

con=mycon.connect(host='bzhwycvxazf9gx13focv-mysql.services.clever-cloud.com',user='ujdw7mbcfwibgnu8',password='WwaSxxPbROpjMLle7M8p',database='bzhwycvxazf9gx13focv')
curs=con.cursor()

no=int(input('Enter bookcode : '))
rv=input('enter review : ')
curs.execute("update books set bookcode= %d where review=%s" %(no,rv))
rec=curs.fetchone()
print(rec)


