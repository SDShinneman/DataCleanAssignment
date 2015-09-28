import csv

# Open our input and output files
csvfile = open('/Users/shawnshinneman/advanced-data-journalism/assignments/data-cleaning/data/cleanme.csv', 'r')
outfile = open('/Users/shawnshinneman/advanced-data-journalism/assignments/data-cleaning/data/cleanme-clean.csv', 'w')

# Now a DictReader and DictWriter
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

# Write headers
writer.writeheader()

 # Clean and write the data to output
for row in reader:
    row['first_name'] = row['first_name'].upper()
    row['zip'] = row['zip'].zfill(5)
    row['city'] = row['city'].replace('&nbsp;', ' ')

    if int(row['amount']) > 999:
        writer.writerow(row)