import json, datetime, urllib.request
from pickle import FALSE, TRUE


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        jsonFile = open("ratios.json", "r")  # Open the JSON file for reading
        data = json.load(jsonFile)
        jsonFile.close()
        for nmr in data:
            if nmr['base_currency'] == self.base and nmr['target_currency'] == self.target and nmr['data_fetched'] != datetime.date.today():
                return True
        return False

        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        pass 

    def fetch_ratio(self):
        url = 'https://api.exchangerate.host/latest?base='+self.base+'&symbols='+self.target  # biblioteka  urllib f urlopen
        response = urllib.request.urlopen(url)
        read = response.read()
        datas = json.loads(read)
        
        print(datas['rates'][self.target])

        self.save_ratio((datas['rates'])[self.target])

        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        pass

    def save_ratio(self, ratio):
        jsonFile = open("ratios.json", "r")
        data = json.load(jsonFile) 
        jsonFile.close()
        
        #print(ratio)

        saved = False
        for nmr in data:
            if nmr['base_currency'] == self.base and nmr['target_currency'] == self.target and nmr['data_fetched'] != datetime.date.today():
                nmr['date_fetched'] = str(datetime.date.today())
                nmr['ratio'] = ratio
                saved = True
        if not saved:
            nmr = {
                'base_currency': self.base,
                'target_currency': self.target,
                'data_fetched': str(datetime.date.today()),
                'ratio': ratio
            }
            data.append(nmr)
        with open('ratios.json', 'w') as file:
            json.dump(data, file, indent=3)
            
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        pass

    def get_matched_ratio_value(self):
        jsonFile = open("ratios.json", "r")  # Open the JSON file for reading
        data = json.load(jsonFile)
        jsonFile.close()

        print(data)

        for nmr in data:
            if nmr['base_currency']== self.base and nmr['target_currency'] == self.target:
                print((nmr['ratio']))
                return nmr['ratio']
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        pass












