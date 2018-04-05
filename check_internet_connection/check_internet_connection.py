# -*- coding: utf-8 -*-
# python 2

# test connnection time to multiple IPs or addresses
# writes results to csv
# use plot_internet_connection.py to see results in graph

import csv
import httplib
import os
import time
import sys


INTERVAL = 10
TEST_LIST = ["8.8.8.8", "1.1.1.1", "google.com", "walla.com"]
PATH_TO_CSV = './conn_test.csv'


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def time_connection(connect_to):
    conn = httplib.HTTPConnection(connect_to, timeout=3)
    start = time.time()
    try:     
        conn.request("HEAD", "/")
        conn.close()
        return time.time() - start
    except:
        conn.close()
        return time.time() - start


def handle_test(c):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print("test #{} - {}".format(c, current_time))
    csv_line = [c, current_time]
    # test each IP / Address
    for test in TEST_LIST:
        csv_line.append("{0:.4f}".format(time_connection(test)))
    
    # append line to csv
    with open(PATH_TO_CSV, 'ab') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_line)
    
    time.sleep(INTERVAL)


def main(test_limit):
    # add headers to csv
    if not os.path.isfile(PATH_TO_CSV):
        header = ["#", "test time"] + TEST_LIST
        with open(PATH_TO_CSV, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)

    if test_limit:
        print("{} tests will run.".format(test_limit))
        for c in xrange(1, test_limit+1):
            handle_test(c)

    else:
        print("tests will run until Ctrl+C")
        c = 1    
        while True:
            handle_test(c)
            c+=1


if __name__ == "__main__":
    if len(sys.argv) == 2 and RepresentsInt(sys.argv[1]):
        test_limit = int(sys.argv[1])
    elif len(sys.argv) == 1:
        test_limit = False
    else:
        print("Too many arguments or argument is not an integer.\nplease use only one number for test limit")
        sys.exit(1)

    main(test_limit)

