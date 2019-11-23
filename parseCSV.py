import csv


if __name__ == "__main__":

    f = open('bdlp_db_def.csv', 'r', encoding="latin-1")
    reader = csv.reader(f)

    for row in reader:
        row[0] = row[0].replace('"', '')
        row[0] = row[0].replace(';', ',')
        row[1] = row[1].replace(';', ',')
        row[2] = row[2].replace(';', ',')
        row[3] = row[3].replace(';', ',')
        row[4] = row[4].replace('"', '')
        row[4] = row[4].replace('[', '')
        row[4] = row[4].replace(']', '')


        if len(row[0]) == 0:
            row[0] = "None"
        if len(row[1]) == 0:
            row[1] = "None"
        if len(row[2]) == 0:
            row[2] = "None"
        if len(row[3]) == 0:
            row[3] = "None"
        if len(row[4]) == 0:
            row[4] = "None"

        print_text = row[0] + ";"  + row[1] + ";" + row[2] + ";" + row[3] + ";" +row[4]
        print(print_text)
        
    f.close()




