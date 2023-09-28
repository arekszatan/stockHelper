import urllib.request


class StockObject:
    def __init__(self, stock_name, div_url):
        self.stock_name = stock_name
        self.have_div = None
        self.div_url = div_url
        self.div_dictionary = []

        if self.div_url == "NONE":
            self.have_div = False
        else:
            self.have_div = True

        self.__div_url_get_information()

    def __str__(self):
        return self.stock_name

    def is_has_div(self):
        return self.have_div

    def get_history_div(self):
        return self.div_dictionary

    def __div_url_get_information(self):
        req = urllib.request.urlopen(self.div_url)
        my_bytes = req.read()
        my_str = my_bytes.decode("utf8")
        req.close()
        num = my_str.find('</thead>')
        my_str = my_str[num:]
        num_end = my_str.find('</table>')
        my_str = my_str[:num_end]

        num1 = 0
        counter = 0
        div_dictionary_tmp = []
        while num1 != -1:
            num1 = my_str.find('</td>')
            my_str_tmp = my_str[:num1]
            my_str = my_str[num1 + 5:]
            my_str_tmp_reverse = my_str_tmp[::-1]
            num = my_str_tmp_reverse.find('>')
            my_str_tmp_reverse = my_str_tmp_reverse[:num]
            my_str_tmp = my_str_tmp_reverse[::-1]

            div_dictionary_tmp.append(my_str_tmp)
            counter += 1
            if counter == 5:
                self.div_dictionary.append(div_dictionary_tmp)
                div_dictionary_tmp = []
                counter = 0
