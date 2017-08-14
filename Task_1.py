import requests
import json
from datetime import date as dt
import calendar as cl



t_num = raw_input("Enter the number? ")

#t = '744668909687'

detail = requests.post('https://www.fedex.com/trackingCal/track', data={
    'data': json.dumps({
        'TrackPackagesRequest': {
            'appType': 'wtrk',
            'uniqueKey': '',
            'processingParameters': {
                'anonymousTransaction': True,
                'clientId': 'WTRK',
                'returnDetailedErrors': True,
                'returnLocalizedDateTime': False
            },
            'trackingInfoList': [{
                'trackNumberInfo': {
                    'trackingNumber': t_num,
                    'trackingQualifier': '',
                    'trackingCarrier': ''
                }
            }]
        }
    }),
    'action': 'trackpackages',
    'locale': 'en_US',
    'format': 'json',
    'version': 99
}).json()


packageDetail = detail["TrackPackagesResponse"]["packageList"][0]
mainData = packageDetail["statusWithDetails"]
rawShipDate = packageDetail["displayTenderedDt"].split('/')

def retrieve_date(day, month, year):
    dy, mth, yr = int(day), int(month), int(year)
    new_Date = dt(yr, mth, dy)
    date = cl.day_name[new_Date.weekday()]
    return date[:3]

dayNameShipment = retrieve_date(rawShipDate[1], rawShipDate[0], rawShipDate[2])
desiredShipDate = rawShipDate[1] + '/' + rawShipDate[0] + '/' + rawShipDate[2]

mainDataSplit = mainData.split(':')
status = mainDataSplit[0]
rawDeliveryDate = mainDataSplit[1][:10].split('/')
dayNameDelivery = retrieve_date(rawDeliveryDate[1], rawDeliveryDate[0], rawDeliveryDate[2])
deliveryDate = rawDeliveryDate[1] + '/' + rawDeliveryDate[0] + '/' + rawDeliveryDate[2]

time = mainDataSplit[1][-1] + ':' + mainDataSplit[2][1:6]

output = "{\ntracking no: " + t_num + ",\nship date: " + dayNameShipment + " " + desiredShipDate + ",\nstatus: " + status + ',\nschedule delivery: ' + dayNameDelivery + " " + deliveryDate + " " + time + "\n}"

print(output)