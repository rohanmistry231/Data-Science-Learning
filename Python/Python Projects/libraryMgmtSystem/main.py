import datetime
import os


class LMS():
    """
    To keep books details.
    Modules: Display, Issue Books, Return Books, Add Books
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = 'list_of_books.txt'
        self.library_name = 'library_name'
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id): {"books_title": line.replace("\n", ""),
                                              "lender_name": "",
                                              "Issue_date": "",
                                              "status": "Available"}})
            Id = Id + 1

    def display_books(self):
        print("--List Of Books--")
        print("Books ID", "\t", "Title")
        print("")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("books_title"), "-", value.get('status'))

    def issue_books(self):
        books_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        if books_id in self.books_dict.keys():

            print(f"\nfor book {self.books_dict[books_id]['books_title']} .. .\n")
            # checking the status
            if not self.books_dict[books_id]['status'] == 'Available':
                print(f"This book has already been issued to {self.books_dict[books_id]['lender_name']}\
                on {self.books_dict[books_id]['issue_date']}")
                print("\n Try another book!")
            elif self.books_dict[books_id]['status'] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['issue_date'] = current_date
                self.books_dict[books_id]['status'] = "Issued"
                print(f"Book issued successfully to {your_name} on {self.books_dict[books_id]['issue_date']}")
        else:
            print("Book ID not found!!! Try Again..")


    def add_books(self):
        new_book = input("Enter book title to add in the library: ")
        if new_book == "":
            return self.add_books()
        elif len(new_book) > 25:
            print("Book title should be less than 25 characters!")
        else:
            with open(self.list_of_books, "a") as nb:
                nb.writelines(f"{new_book}\n")
                self.books_dict.update({str(int(max(self.books_dict))): {"books_title": new_book,
                                                          "lender_name": "",
                                                          "Issue_date": "",
                                                          "status": "Available"}})
                print(f"{new_book} has been added! Thank you!")


    def return_book(self):
        book_id = input("Enter the returning book ID: ")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]['status'] == "Available":
                print("This book is already available in the system!")
                return self.return_book()
            elif not self.books_dict[book_id]['status'] == "Available":
                self.books_dict[book_id]['lender_name'] = ""
                self.books_dict[book_id]['issue_date'] = ""
                self.books_dict[book_id]['status'] = "Available"
                print("Returned book updated in the system!")
        else:
            print("Wrong book ID! Try Again..")




try:
    myLMS = LMS("list_of_books.txt", "My Library")
    press_key_list = {'d':'Display Books',
                     'i': "Issue A Book",
                     'a': "Add A Book",
                     'r': "Return The Book",
                     'q' : 'quit'}
    key_press = False
    while not (key_press == 'q'):
        print(f"\n-------- Welcome to {myLMS.library_name} Management System.-------\n")
        for key, value in press_key_list.items():
            print("Press ", key, "To", value)
        key_press = input("Press Key: ").lower()
        if key_press == 'i':
            print("\n------Issue a Book-------")
            myLMS.issue_books()
        elif key_press == 'a':
            print("\n------Add a new Book-----")
            myLMS.add_books()
        elif key_press == 'd':
            print('\n-----Display Books-----')
            myLMS.display_books()
        elif key_press == "r":
            print("\n------Return your book-------")
            myLMS.return_book()
        elif key_press == 'q':
            break
        else:
            print("Enter the correct key!!!")
            continue
except Exception as e:
    print("Wrong key entered!")