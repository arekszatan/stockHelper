import urllib.request

fp = urllib.request.urlopen("https://strefainwestorow.pl/notowania/gpw/handlowy-bhw/dywidendy")
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()
num = mystr.find('</thead>')
mystr = mystr[num:]
num_end = mystr.find('</table>')

print(mystr[:num_end])


class StockObject:
    def __init__(self, stock_name, div_url):
        self.stock_name = stock_name
        self.have_div = None
        self.div_url = div_url

        if self.div_url == "NONE":
            self.have_div = False
        else:
            self.have_div = True

    def __str__(self):
        return self.stock_name

    def is_has_div(self):
        return self.have_div

    def get_history_div(self):
        fp = urllib.request.urlopen(self.div_url)
        my_bytes = fp.read()
        my_str = my_bytes.decode("utf8")
        fp.close()


test = StockObject("Handlowy", "https://strefainwestorow.pl/notowania/gpw/handlowy-bhw/dywidendy")

