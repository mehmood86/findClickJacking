# This program will show all header information in a homepage
# of specified website

# Change the value of 'url' in the code below
# To run the program, use 'python test.py' in console

import sys
import urllib.request

def main():
    url ="https://www.notebooksbilliger.de/index.php/action/login"

    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': '''   Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)
                                AppleWebKit/537.36 (KHTML, like Gecko)
                                Chrome/35.0.1916.47 Safari/537.36   ''' })
    f = urllib.request.urlopen(req)
    print(f.info())
    if "X-Frame-Options" in f.info():
        print("Not Vulnerable to Clickjacking")
    else:
        print("Vulnerable to Clickjacking")
    # print(f.read().decode('utf-8'))

if __name__=="__main__":
    main()

n = 123
print ('asa%s'%n+1)
