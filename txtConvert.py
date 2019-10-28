import csv

# convert txt file to csv
with open('accounts.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('accounts.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('title', 'intro'))
        writer.writerows(lines)


# open csv file, loop through file and save output to new file
open_csv = open('accounts.csv','r')
output_file = open('accounts02.csv','w')

for row in open_csv:
    if row.__contains__ ('"ACCT"'):
        print(row)
        output_file.write(row+'\n')