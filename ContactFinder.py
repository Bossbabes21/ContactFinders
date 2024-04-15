import csv

year = 'organizations-1000.csv'


def contact_manager(file):
    sum = 0

    contacts = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            # get name, country, description, founded, industry
            name = row[2]
            country = row[4]
            description = row[5]
            founded = int(row[6])



            contact = (name, country, description, founded)

            if founded == 1980:
             contacts.append(contact)
    print(f"all conatacts founded in 1980")
    print('')
    return contacts


print(contact_manager(f'organizations-1000.csv'))
