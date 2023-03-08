import sqlite3

db = sqlite3.connect("books")

cursor = db.cursor()

# Creating a table called books
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    qty INTEGER)
""")

#   ==========Functions==============


def lists():
    list_book = []
    cursor.execute("""
                    SELECT * FROM books """)
    for row in cursor:
        list_book.append(str(row[0]))
    return list_book


db.commit()


def enter_book():
    """ Function to create a new book """
    id_number = input("Please enter the id number of the new book:")
    new_title = input("Please enter the title of the book:")
    new_author = input("Author of the book:")
    new_qty = input("Quantity of books: ")
    cursor.execute("""
    INSERT INTO books(id, title, author, qty)
    VALUES(?,?,?,?)""", (id_number, new_title, new_author, new_qty))


db.commit()


def update_book():
    """Function to update book"""
    id_number2 = input("Please enter the id number of the book you want to update:")
    if id_number2 in lists():
        option = input("What would you like to update title or quantity?")

        # If statement to update the selected books title.
        if option == "title":
            new_title = input("What would you like to change the title to?")
            cursor.execute("""
                UPDATE books
                SET title  = ?
                WHERE id = ?""", (new_title, id_number2))

        # If statement to update the selected book's quantity.
        elif option == "quantity":
            new_qty = input("What would you like to change the quantity to?")
            cursor.execute("""
                UPDATE books
                SET qty  = ?
                WHERE id = ?""", (new_qty, id_number2))

        else:
            print("Sorry wrong input!")
    else:
        print("ID does not exist!")


db.commit()


def delete_book():
    """Function to delete book"""
    delete_id = input("Please enter the id number for the book you wish to delete.")
    if delete_id in lists():
        cursor.execute("""
                DELETE FROM books
                WHERE id = ?""", (delete_id,))

        print(f"You have deleted ID:{delete_id} from the database.")

    else:
        print("Book does not exist in database")


db.commit()


def search_book():
    """ Function to search book"""
    select_book = input("Please enter the id number for the book you wish to find.")
    if select_book in lists():
        cursor.execute("""
            SELECT id, title, author, qty
            FROM books
            WHERE id = ?""", (select_book,))
        for row in cursor:
            print(f"ID number {row[0]}: Title {row[1]}:  Author {row[2]}: Quantity {row[3]}")

    else:
        print("ID does not exists.")


db.commit()


def all_books():
    """ Function to print table"""
    cursor.execute('''SELECT * FROM books''')
    books = cursor.fetchall()
    for i in books:
        print(i)


#   ==========Values inside the table==============
id_num = 3001
title = "A Tale of Two Cities"
author = "Charles Dickens"
qty = 30

id_num2 = 3002
title2 = "Harry Potter and the Philosopher's Stone"
author2 = "J.K.Rowling"
qty2 = 40

id_num3 = 3003
title3 = "The Lion, the Witch and the Wardrobe"
author3 = "C.S.Lewis"
qty3 = 25

id_num4 = 3004
title4 = "The Lord of the Rings"
author4 = "J.R.R Tolkien"
qty4 = 37

id_num5 = 3005
title5 = "Alice in Wonderland"
author5 = "Lewis Carroll"
qty5 = 12

#   ==========Inserting values into books table==============
cursor.execute("""
    INSERT INTO books(id, title, author, qty)
    VALUES(?,?,?,?)""", (id_num, title, author, qty))

cursor.execute("""
    INSERT INTO books(id, title, author, qty)
    VALUES(?,?,?,?)""", (id_num2, title2, author2, qty2))

cursor.execute("""
    INSERT INTO books(id, title, author, qty)
    VALUES(?,?,?,?)""", (id_num3, title3, author3, qty3,))

cursor.execute("""
    INSERT INTO books(id, title, author, qty)
    VALUES(?,?,?,?)""", (id_num4, title4, author4, qty4,))

cursor.execute("""
    INSERT INTO books(id, title, author, qty)
    VALUES(?,?,?,?)""", (id_num5, title5, author5, qty5,))


#   ==========Main Menu==============

while True:
    menu = input(""" Select one of the following options below:
    1 - New book 
    2 - Update book 
    3 - Delete book
    4 - Search Book 
    5 - Display all books
    0 - Exit
    :""").lower()

    # Enter book
    if menu == "1":
        enter_book()

    # Update book
    elif menu == "2":
        update_book()

    # Delete book
    elif menu == "3":
        delete_book()

    # Search book
    elif menu == "4":
        search_book()

    # All books
    elif menu == "5":
        all_books()

    # Exit program
    elif menu == "0":
        exit()

    else:
        print("You have inputted a wrong number, please try again.")
