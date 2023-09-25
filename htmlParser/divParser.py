import urllib.request

fp = urllib.request.urlopen("https://strefainwestorow.pl/notowania/gpw/handlowy-bhw/dywidendy")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
num = mystr.find('</thead>')
mystr = mystr[num:]
num_end = mystr.find('</table>')

print(mystr[:num_end])


class DivParser:
    def __init__(self, stock_name):
        self.stock_name = stock_name

    def __str__(self):
        return self.stock_name


test = DivParser("Orlen")

