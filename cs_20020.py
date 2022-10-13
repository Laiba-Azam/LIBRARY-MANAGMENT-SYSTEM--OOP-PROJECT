class library_system:
    record_of_book=[]
    def add_book(self):
        while True:
            name=input('book name ')
            Aname=input('writer name ')
            year=input('Year of publishing ')
            price=int(input('Price RS '))
            code=input('book code ')
        #making list
            library_system.record_of_book.append([name,Aname,year,price,code])
        #giving option to user for further addition on the list
            choice=input('enter c to continue or any alphabet to exit')
            if choice!='c' and choice!='C':
                break
    # code for displaying record
    def display_book(self):
        e='book code'
        a='BOOK NAME:'
        b='BOOK WRITER:'
        c='PRICE IN PKR:'
        d='Published in '
        print(f'{e:20} {a:20} {b:28} {c:23} {d:20}')
        f=open('book.txt','r')
        for i in f:
            i=i.split(',')
            print(f'{i[4]:23} {i[0]:20} {i[1]:30} {i[3]:20} {i[2]:20}')
        f.close()
    def save_book(self):
        f=open('book.txt','a')# use write to creat a file
        for i in library_system.record_of_book:
            f.write(i[0]+', ')
            f.write(i[1]+', ')
            f.write(i[2]+', ')
            f.write(str(i[3])+', ')
            f.write(str(i[4])+'\n')
        f.close()
    def remove_book(self): #This method removes product from the store
        f=open('book.txt','r')
        lines=f.readlines()
        f.close()

        new_file=open('book.txt','w')
        n=input('Enter the code of the book to be removed: ')
        p=n.title()
        for line in lines:
            if n not in line:
                new_file.write(line)
        new_file.close()
class customer(library_system):
    a=[]
    list_of_products=[]
    code=[]
    
    price=0
    def signup(self,name,password,email,phone_no,payment_method):
        self.name=name
        self.password=password
        self.email=email
        self.phone_no=phone_no
        self.payment_method=payment_method
        customer.a.append(self.name)
        customer.a.append(self.password)
        customer.a.append(self.email)
        customer.a.append(self.phone_no)
        customer.a.append(self.payment_method)
        self.info1=[]
        self.info1.append([self.name,self.password,self.email,self.phone_no,self.payment_method])
        f=open('customerinfo.txt','a')
        for p in self.info1:
            f.write(str(p[0])+',')
            f.write(p[1]+',')
            f.write(p[2]+',')
            f.write(str(p[3])+',')
            f.write(str(p[4])+'\n')
        f.close()
    def cancel_membership(self):
        #This method removes product from the store
        f=open('customerinfo.txt','r')
        lines=f.readlines()
        f.close()

        new_file=open('customerinfo.txt','w')
        n=input('Enter the password of the account to be removed: ')
        p=n.title()
        for line in lines:
            if n not in line:
                new_file.write(line)
        new_file.close()
    def search_book(self):
        t=True
        while True:
            n=input("name of book ")
            f=open('book.txt','r')
            for i in f:
                if n in i:
                    t=True
                    print ('your book is here ') 
                    break
                elif n not in i:
                    t=False
                    continue
            if t==False:
                 print(' your order is reserved we will inform you as soon as possible about new stock')
            else:
                choice=input('enter c to continue or any alphabet to exit')
                if choice!='c' and choice!='C':
                    break 
            f.close()

    def borrow_book(self):
        while True:
            t=False
            choice=input('Do you want to borrow more books press y')
            if choice=='Y' or choice=='y':
                n=input("name of book")
                f=open('book.txt','r')
                line=f.readlines()
                print(line)
                for i in line:
                    print(i)
                    if n in i:
                        item=i.strip()
                        item=i.split(',')
                        customer.price+=int(item[3])
                        continue
                    
                    elif n not in i:
                        continue
                    
            else:
                if customer.price==0 :
                    print(' your order is reserved we will inform you as soon as possible about new stock')
                    print('Thankyou')
                    break
                else:
                    print ('book is borrowed by', self.name)
                    print('Total borrow fee is',customer.price-50)
                    break
           
            
    def return_book(self):
        n=input('code of book')
        f=open('book.txt','a+')
        for i in f:
            if n in i :
                f.write(i[0]+', ')
                f.write(i[1]+', ')
                f.write(i[2]+', ')
                f.write(str(i[3])+', ')
                f.write(str(i[4])+'\n ')
        f.close()
    def  renew(self):
        t=False
        n=str(input('code of book'))
        f=open('book.txt','r')
        for i in f:
            if n in i:
                t=True
            elif n not in i:
                continue
                
        if t==True :
            print ('book is re-borrowed by', self.name)
        else:
            print(' your order is reserved we will inform you as soon as possible about new stock')
            
                
        f.close()
    def convert_from_file(self):         
        f=open('book.txt','r')
        for line in f:
            item=line.strip()
            item=item.split(',')
        #self.list_of_products=eval(f.read())
            customer.list_of_products.append(item)
            customer.code.append(item[4])
            
        f.close()
    def display_books(self):
        e='book code'
        a='BOOK NAME:'
        b='BOOK WRITER:'
        c='PRICE IN PKR:'
        d='Published in '
        print(f'{e:20} {a:30} {b:30} {c:23} {d:20}')
        f=open('book_sorted.txt','r')
        for i in f:
            i=i.split(',')
            print(f'{i[4]:20} {i[0]:30} {i[1]:30} {i[3]:23} {i[2]:20}')
        f.close()
    def bubbleSort(self):#cort the list of all the code of books stored names customer.code
        n = len(customer.code)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if customer.code[j] > customer.code[j + 1] :
                    customer.code[j], customer.code[j + 1] = customer.code[j + 1],customer.code[j]
       
        
        f=open('book.txt','r')#this code will match the code in sorted list to the code in book file and write it in a new sorted _book file
        lines=f.readlines()
        f.close()

        new_file=open('book_sorted.txt','w')
        for i in customer.code:
            n=i
            p=n.title()
            for line in lines:
                if n in line:
                    new_file.write(line)
                    break
        new_file.close()

n=input("Are you admin or customer")
if n=='admin' or n=='Admin' or n=='ADMIN':
    l=library_system()
    while True:
        a=input('''1: TO ADD BOOKS
2: TO REMOVE BOOKS
3: CHECK STOCK
4: LOG OUT ''')
        if a=='1' or a=='1':
            l.display_book()
            l.add_book()
            l.save_book()
            
            continue
        elif a=='2':
            l.display_book()
            l.remove_book()

            continue
        elif a=="3":
            l.display_book()
            continue
        else:
            break
        
        
    #this will display unsorted books 
elif n=='customer' or n=='Customer' or n=='CUSTOMER':
   
    n1=input('YOUR NAME ')
    n2=input('YOUR PASSWORD ')
    n3=input('YOUR EMAIL ')
    n4=input('YOUR CONTACT ')
    n5=input('PAYMENT CASH OR CREDIT CARD? ')
    c=customer()
    c.signup(n1,n2,n3,n4,n5)
    c.convert_from_file()
    c.bubbleSort()
    while True:
        a=input('''1: TO CANCEL MEMBERSHIP
2: REBORROW BOOK
3: BORROW BOOK
4: RETURN BOOK
5: Search BOOK
6: EXIT ''')
        if a=='1' or a=='1':
            c.cancel_membership()
            continue
        elif a=='2':
            c.display_books()
            c.renew()
            continue
        elif a=='3' :
            c.display_books()
            c.borrow_book()
            continue
        elif a=='4':
            c.return_book
            continue
        elif a=='5':
            c.search_book()
        else:
            break
        
  





        





    

    
