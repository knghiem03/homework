def delivery_report(day, data_file):
    # Open the file to read
    print(f"Day {day}")
    the_file = open(data_file)
    # After opening the file, read read single line, strip off the blank space at the end of the line and split it 
    # by he "|"
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        melon, count, amount = words
        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

delivery_report(1,"um-deliveries-20140519.txt")
delivery_report(2,"um-deliveries-20140520.txt")
delivery_report(3,"um-deliveries-20140521.txt")