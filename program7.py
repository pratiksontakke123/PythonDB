import  mysql.connector as mycon

con=mycon.connect(host='bzhwycvxazf9gx13focv-mysql.services.clever-cloud.com',user='ujdw7mbcfwibgnu8',password='WwaSxxPbROpjMLle7M8p',database='bzhwycvxazf9gx13focv')
curs=con.cursor()


curs.execute('alter table books add review varchar(500)')
data=curs.fetchone
print(data)
