import csv


class Information:
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
            category = row['Category']
            homepage = row['Homepage']
            keyword = row['Keyword']
            quantity = row['Quantity']
            delivery = row['Delivery']
            payment = row['Payment']
            successMessage = row['Message']
