import  mysql.connector as mycon

con=mycon.connect(host='bzhwycvxazf9gx13focv-mysql.services.clever-cloud.com',user='ujdw7mbcfwibgnu8',password='WwaSxxPbROpjMLle7M8p',database='bzhwycvxazf9gx13focv')
curs=con.cursor()

try:
    bcode=int(input('Enter book code : '))
    bookname=input('Enter books name : ')
    auther=input('Enter auther : ')
    pubn=(input(' enter publication : '))
    edtn=int(input('Enter edition: '))
    prc=int(input('Enter price : '))
    lang=input('enter language :')
    cat=input('enter category : ')
    


    curs.execute("insert into books values(%d,'%s','%s','%s','%d','%d','%s','%s')" %(bcode,bookname,auther,pubn,edtn,prc,lang,cat,rev))
    con.commit()
    print('Book is added')
except:
    print('book is not added')
con.close()
