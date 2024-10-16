with open("smhi-opendata.csv","r",encoding="utf-8") as WD:

    for line in WD:
        split_data = line.split(";")
        date = split_data[0].split("-")
    
        if date[0] == "2001":
            print(date)