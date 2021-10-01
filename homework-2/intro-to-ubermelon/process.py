# Open the um-server-01.txt 
log_file = open("um-server-01.txt")

# This is a function
def sales_reports(log_file):
    # Read each line in the file 
    for line in log_file:
        # Remove the blank spaces to the right of the line
        line = line.rstrip()
        # Strip out the first three characters and store the value in day
        day = line[0:3]
        # if the day is "Mon" then print out that line
        if day == "Mon":
            print(line)


sales_reports(log_file)
