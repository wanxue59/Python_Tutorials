import addressbook_pb2    # 从当前文件夹导入模块

def ListPeople(address_book):
    for person in address_book.people:
        print("Person ID:", person.id)
        print("  Name:", person.name)
        print("  Person email:", person.email)

        for phone_number in person.phones:
            if phone_number.type == addressbook_pb2.MOBILE:
                print("  Mobile phone #: ")
            elif phone_number.type == addressbook_pb2.HOME:
                print("  Home phone #: ")
            elif phone_number.type == addressbook_pb2.WORK:
                print("  Work phone #: ")
            print(phone_number.number)

def read_test():
    address_book = addressbook_pb2.AddressBook()
    address_book_file = "./data/addressbook.txt"

    f = open(address_book_file, "rb")
    address_book.ParseFromString(f.read())

    f.close()
    ListPeople(address_book)

if __name__ == '__main__':
    read_test()