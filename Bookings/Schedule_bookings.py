def availability(p,b):
    global person_dict , book_dict
    
    if  b in person_dict[p][0] :
        print("Person can book it only once.")
        return False

    elif 4 in book_dict[b][0]  :
        print("Bookings are full.")
        return False

    else :
        return True

def book_slot(p,b):
    if availability(p,b) :       
        book_dict[b][0].append(len(book_dict[str(b)][0]) + 1)
        book_dict[b][1].append(p)
        person_dict[p][0].append(b)
        person_dict[p][1].append(book_dict[b][0])
        print("Booked slot for book "+b+" by person "+p+" is "+date[book_dict[b][0][-1] - 1])

def book_booking(b): 
    for  j in range (len(book_dict[b][0])) : 
        print("Person "+ book_dict[b][1][j] + " : " +date[book_dict[b][0][j] - 1]) 


def person_booking(p):
    for j in range (len(person_dict[p][0])):
        print("Book name : "+str(person_dict[p][0][j])+ " -- Slot : "+ date[int(person_dict[p][1][j][0])-1])


date = ["1st Nov - 7th Nov","8th Nov - 14th Nov","15th Nov - 21st Nov","22nd Nov - 28th Nov"]
person_list = list(input("Enter person's name : ").split())
book_list = list(input("Enter book's name : ").split())
person_dict = {}
book_dict = {}
for i in person_list:
    person_dict[i] = [[],[]]
for j in book_list:
    book_dict[j] = [[],[]]
# print(person_dict)
# print(book_dict)
run = True
while run:
    print('''
1. Book the slot. 
2. Check book's booking.
3. Person booking
4. Quit
''')
    query = input("Enter the number : ")
    if query == "1":
        person,book = input("Enter person and book : ").split()
        book_slot(person,book)

    elif query == "2":
        buk = input("Enter book name : ")
        book_booking(buk)

    elif query == "3" :
        pers = input("Enter person name : ")
        person_booking(pers)

    elif query == "4":
        run = False
        print("Exited.")


    else :
        print("Entered number out of range.")