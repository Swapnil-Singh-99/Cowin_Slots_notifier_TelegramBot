import requests
import datetime
import jsons
import bot
from settings import app_secrets

# This function get the date according to this means temedelta
def get_date(this):
	global date_got
	x = datetime.date.today()+ datetime.timedelta(days = this) 
	day = str(x.day).zfill(2)
	month = str(x.month).zfill(2)
	year = str(x.year).zfill(2)
	y = [day , month , year]
	date_got = str("-".join(y))
	return date_got

# This request is for fiding out session on a particular date
def request_one(RequestDate):
	global list_sessions
	url1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=664&date="
	url = url1 + RequestDate
	url = url.strip()
	head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
	head1 = {"User-Agent":"Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0"}
	response = requests.get(url , headers=head1)
	data = response.json()
	l = jsons.load(data)
	a = l["sessions"]
	list_sessions = []
	for i in a:
		if i["available_capacity"] >= 30:
			lst = []
			name = i["name"]
			if "/" in name :
				name = name.replace("/" , "")
			address = i["address"]
			pincode = i["pincode"]
			date_new = i["date"]
			allow_all_age = i["allow_all_age"]
			fee_new = i["fee_type"]
			fee = i["fee"]
			if fee_new == "Paid":
				fee_new = fee_new+" ( "+fee+" )"
			dose1 = i["available_capacity_dose1"]
			dose2 = i["available_capacity_dose2"]
			age_min = i["min_age_limit"]
			vaccine = i["vaccine"]
			tot_dose = i["available_capacity"]
			lst.append(name)
			lst.append(address)
			lst.append(fee_new)
			lst.append(date_new)
			lst.append(vaccine)
			lst.append(age_min)			
			lst.append(dose1)
			lst.append(dose2)
			lst.append(tot_dose)
			lst.append(pincode)
			lst.append(allow_all_age)
			if tot_dose != 0:
				list_sessions.append(lst)

#This request shows the the whole week slots of a particular district
def request_two(RequestDate):
	global list_sessions
	url1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=664&date="
	url = url1 + RequestDate
	url = url.strip()
	head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
	head1 = {"User-Agent":"Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0"}
	response = requests.get(url , headers=head1)
	data = response.json()
	l = jsons.load(data)
	a = l["centers"]
	list_sessions = []
	for i in a:
		name = i["name"]
		if "/" in name :
				name = name.replace("/" , "")
		address = i["address"]
		pincode = i["pincode"]
		fee_new = i["fee_type"]
		if fee_new == "Paid":
			w = i["vaccine_fees"]
			for qq in w:
				fee = qq["fee"]
			fee_new = fee_new+" ( "+fee+" )"
		b = i["sessions"]
		z = b[0]
		if z["available_capacity"] >= 30 :
			bg_list = []
			datet = z["date"]
			vaccine = z["vaccine"]
			age = z["min_age_limit"]
			allow_all_age = z["allow_all_age"]
			dose1 = z["available_capacity_dose1"]
			does2 = z["available_capacity_dose2"]
			bg_list.append(name)
			bg_list.append(address)
			bg_list.append(fee_new)
			bg_list.append(datet)
			bg_list.append(vaccine)
			bg_list.append(age)
			bg_list.append(dose1)
			bg_list.append(does2)
			bg_list.append(z["available_capacity"])
			bg_list.append(pincode)
			bg_list.append(allow_all_age)
			list_sessions.append(bg_list)


# ///////////////////////////////////////////////////////////////
# If you run this request.py then only the available slots in the present time will be printed
if __name__ == "__main__":
	request_one(get_date(0))
	for i in list_sessions:
		text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nPincode : *{i[9]}*\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*'
		print(text ,"\n")
	request_two(get_date(0))
	for i in list_sessions:
		text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nPincode : *{i[9]}*\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*'
		print(text , "\n")