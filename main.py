from bs4 import BeautifulSoup
import requests
import sys
import re
if __name__ == "__main__":
    n = len(sys.argv)

    if n >= 5:
        final = []
        for i in range(1, 5):
            final.append(sys.argv[i])
        url_option, url, output_option, output = final
        # reference https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/
        html = requests.get(url)
        bsoup_object = BeautifulSoup(html.text, "lxml")
        a_tag = bsoup_object.findAll('a', attrs={'href': re.compile("^https://")})
        if output == "stdout":
            for a in a_tag:
                print(a['href'])
        elif output == "json":
            test = {}
            for a in a_tag:
                u = str(a['href']).split(".com/")
                base = u[0]
                if base not in test.keys():
                    if not len(u) > 1:
                        test[base] = ['/']
                    else:
                        test[base] = [u[1]]
                else:
                    if not len(u) > 1:
                        test[base].append('/')
                    else:
                        test[base].append(u[1])

            print(test)
    else:
        print("Not enough arguments")
