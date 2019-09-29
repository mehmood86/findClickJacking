import sys
import urllib.request

def main():
    fin = open("input.txt", "r")
    fout = open("output.txt", "w+")

    f1 = fin.readlines()
    fout.write('No.\t  |Vuln\t\t|URL\n\n' )
    count = 0
    for i, url in enumerate(f1):
        global vulnerable

        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        f = urllib.request.urlopen(req)
        # print(f.info())
        if "X-Frame-Options" in f.info():
            # print("Not Vulnerable to Clickjacking")
            vulnerable = 'No  '
        else:
            # print("Vulnerable to Clickjacking")
            vulnerable = 'Yes'
            count += 1
        print("Processing website " + str(i+1) + "...")
        fout.write(str(i+1) + '    \t|' + vulnerable + '\t\t|' + url)

    print("\nTotal " + str(len(f1)) + " websites are processed\n")
    print(str(count) + " websites are vulnerable to clickjacking.")

    fin.close()
    fout.close()

if __name__ == "__main__":
    main()
