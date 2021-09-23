import addressbook_pb2

def PromptForAdrress(person):
    person.id = 1
    person.name = "RRN"
    person.email = "ranrn@qq.com"
    phone_number = person.phones.add()
    phone_number.number = "13244556677"
    phone_number.type = addressbook_pb2.MOBILE


def write_test():
    address_book = addressbook_pb2.AddressBook()
    person = address_book.people.add()
    PromptForAdrress(person)
    address_book_file = "./data/addressbook.txt"

    try:
        f = open(address_book_file, "wb")
        f.write(address_book.SerializeToString())
        print(address_book.SerializeToString())
        # address_book.ParseFromString(f.read())

        f.close()
    except IOError:
        print(address_book_file + ": Could not open file. Creating a new one")

if __name__ == "__main__":

    write_test()