# Task_1_python
fedex detail


Documentation:
	
			refrence:	https://stackoverflow.com/questions/18817185/parsing-html-does-not-output-desired-datatracking-info-for-fedex

	Step 1:

			import requests    : to request the details
			import json		   : for json array
	Step 2:
			to read tracking number
						t_num = raw_input("Enter the number? ")
	Step 3:
			take complete detail for given number from fedex website

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



	Step 4:	To read that detail from json

			packageDetail = detail["TrackPackagesResponse"]["packageList"][0]
			mainData = packageDetail["statusWithDetails"]
			rawShipDate = packageDetail["displayTenderedDt"].split('/')


	Step 4:	To read date

			from datetime import date as dt
			import calendar as cl

			def retrieve_date(day, month, year):
    		dy, mth, yr = int(day), int(month), int(year)
    		new_Date = dt(yr, mth, dy)
    		date = cl.day_name[new_Date.weekday()]
    		return date[:3]

    		dayNameShipment = retrieve_date(rawShipDate[1], rawShipDate[0], rawShipDate[2])
			desiredShipDate = rawShipDate[1] + '/' + rawShipDate[0] + '/' + rawShipDate[2]


    Step 5: At last print the info

    		output = "{\ntracking no: " + t_num + ",\nship date: " + dayNameShipment + " " + desiredShipDate + ",\nstatus: " + status + ',\nschedule delivery: ' + dayNameDelivery + " " + deliveryDate + " " + time + "\n}"

			print(output) 
