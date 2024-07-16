from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import re

def news_verification():
    r = Request('https://br.investing.com/economic-calendar/', headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(r).read()
    soup = BeautifulSoup(response, "html.parser")
    table = soup.find_all(class_ = "js-event-item")

    result = []
    base = {}
    
    for bl in table:
        time = bl.find(class_ ="first left time js-time").text.strip()
        currency = bl.find(class_ ="left flagCur noWrap").text.split(' ')[1]
        event = bl.find(class_="left event").text.strip() if bl.find(class_="left event") else None
        
        actual = None
        previous = None

        # Usar expressão regular para encontrar a classe "bold act blackFont event-XXXX-actual"
        actual_elem = bl.find(class_=re.compile(r"bold act blackFont event-\d+-actual"))
        if actual_elem:
            actual = actual_elem.text.strip()

        # Usar expressão regular para encontrar a classe "prev blackFont event-XXXX-previous"
        previous_elem = bl.find(class_=re.compile(r"prev blackFont event-\d+-previous"))
        if previous_elem:
            previous = previous_elem.text.strip()
        
        intensity = bl.find_all(class_="left textNum sentiment noWrap")
        id_hour = currency + '_' + time
         
        if id_hour not in base:
            base.update({
                id_hour: {
                    'currency': currency,
                    'time': time,
                    'event': event,
                    'actual': actual,
                    'previous': previous,
                    'intensity': {"1": 0, "2": 0, "3": 0}
                }
            })
        
        intensity_counts = base[id_hour]['intensity']
        
        for intence in intensity:
            _true = intence.find_all(class_="grayFullBullishIcon")
            
            if len(_true) == 1:
                intensity_counts['1'] += 1
            elif len(_true) == 2:
                intensity_counts['2'] += 1
            elif len(_true) == 3:
                intensity_counts['3'] += 1
            
        base[id_hour].update({'intensity': intensity_counts})

    for b in base:
        result.append(base[b])

    return result

news = news_verification()

print(json.dumps(news, indent=2, ensure_ascii=False))
