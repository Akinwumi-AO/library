class Library :
    def __init__(self,ListBooks):
        self.books = ListBooks

    def displayAvailableBooks(self):
        print(f"\nThere are {len(self.books)} books available\n")
        for book in self.books :
            print("->" + book)
            print("\n")

    def borrowBooks(self, name, bookname):
        if bookname not in self.books :
            print("\nthe book has been borrowed")
        else :
            track.append({name : bookname})
            print("You have successfully borrowed the book\n")
            self.books.remove(bookname)

    def returnBook(self, bookname):
        print("You have successfully returned the book")
        self.books.append(bookname)

    def donateBook(self, bookname):
        print("Thanks to you, we now have a book added to our catalog")
        self.books.append(bookname)

class Student():
    def borrowBook(self):
        print("Do you wanna borrow a book? \n")
        self.book = input("Please enter the book name you want")
        return self.book

    def returnBook(self):
        print("Wanna return a book\n")
        self.book = input("Please enter the book name you borrowed")
        if{name: self.book} in track :
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        print("You have a book to donate\n")
        self.book = input("Please enter the book name you wanna donate")


if __name__ == '__main__':

    mylibrary = Library(["Computer Science", "Business Info", "Fine Art", "Corruption"])
    Student = Student()
    track = []



    print("How can we help: \n1.View Books\n2.Borrow book\n3.Return book\n4.Donate book\n5.Track book\n6.Exit Application")

    while(True) :
        response = int(input("Please select an option\n"))

        if response == 1 :
            mylibrary.displayAvailableBooks()

        elif response == 2 :
            mylibrary.borrowBooks(input("Enter your name: \n"), Student.borrowBook())

        elif response == 3 :
            mylibrary.returnBook(Student.returnBook())

        elif response == 4 :
            mylibrary.donateBook(Student.donateBook())

        elif response == 5 :
            for i in track :
                for key, value in i.items() :
                    borrower = key
                    book = value
                    print(f"{book} book was borrowed by {borrower}")
                print("\n")
                if len(track) == 0 :
                    print("No book has been borrowed yet")

        elif response == 6 :
            print("Thanks for coming around today, We expect to see you soon")
            exit()

        else :
            print("Inappropriate option selected")

    print("Something went wrong")
