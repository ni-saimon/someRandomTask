import csv


class GuestInformation:
    with open("G:\\information.csv", encoding='utf-8-sig') as f_input:
        csv_input = csv.DictReader(f_input)

        for row in csv_input:
            firstName = row['FirstName']
            lastName = row['LastName']
            email = row['Email']
            company = row['Company']
            city = row['City']
            street1 = row['Street1']
            zip = row['PostCode']
            phone = row['Mobile']
            fax = row['Fax']
    """
    firstName = "Nafiz"
    lastName = "Imtiaz"
    email = "n@email.com"
    company = "RandomCompany"
    city = "RandomCity"
    street1 = "RandomStreet"
    zip = "1212"
    phone = "01234567890"
    fax = "000-111-222"
    """
