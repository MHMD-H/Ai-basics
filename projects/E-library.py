import datetime

class Elibrary:
    def __init__(self, book):
        self.book = book
        self.lst = []

    def add_book(self):
        self.lst.append(self.book)
        file = r"C:\Users\moham_f78sqay\Desktop\library.txt"
        with open(file, "a") as f:  # append بدال w
            for l in self.lst:
                f.write(l + "\n")
        print("Book added successfully ✅")

    def add_time(self):
        year = int(input("The year: "))
        month = int(input("The month: "))
        day = int(input("The day: "))

        borrow_date = datetime.datetime(year, month, day)  # تاريخ الاستعارة
        deadline = borrow_date + datetime.timedelta(weeks=1)  # بعد أسبوع

        # حساب الغرامة لو اتأخر
        now = datetime.datetime.now()
        if now > deadline:
            days_late = (now - deadline).days
            fine = days_late * 20
            print(f"❌ Sorry sir, you should pay {fine}$ (late by {days_late} days).")
        else:
            print("✅ Thank you sir, you returned the book on time.")
    
# تجربة

for i in range(4) :
    book = Elibrary(input("Enter the book name : "))
    book.add_book()
    book.add_time()
