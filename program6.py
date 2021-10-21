import  mysql.connector as mycon

con=mycon.connect(host='bzhwycvxazf9gx13focv-mysql.services.clever-cloud.com',user='ujdw7mbcfwibgnu8',password='WwaSxxPbROpjMLle7M8p',database='bzhwycvxazf9gx13focv')
curs=con.cursor()
cho='yes'


try:
    no=int(input('Enter book code wants delete : '))
    curs.execute("select * from books where bookcode=%d" %no)
    data=curs.fetchall()
    cho=input("do u want to delete ?")

    if cho.upper()=='YES':
        curs.execute("delete from books where bookcode=%d" %no)
        con.commit()
        print('book deleted successfully')
    else:
        print('book is not delete')
except:
    print('error in deletion')


con.close()



