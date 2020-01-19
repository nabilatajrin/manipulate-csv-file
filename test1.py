import csv

with open('bkash_banner3.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    for row in csv_reader:
        if line_count == 1:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[1]} works in the {row[2]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')