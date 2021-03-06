import bot
import personal
import request
import os

SEND_18PLUS_group = True
SEND_45PLUS_group = True

minimum_doses_under_18 = int(os.environ.get('MIN_DOSES_FOR_18PLUS'))
minimum_doses_above_45 = int(os.environ.get('MIN_DOSES_FOR_45PLUS'))
number_of_days_check_18 = int(os.environ.get('DAYS_TO_CHECK_FOR_18PLUS'))
number_of_days_check_45 = int(os.environ.get('DAYS_TO_CHECK_FOR_45PLUS'))


def text_18_one(this):
	global t18_text
	data_18 = []
	request.request_one(request.get_date(this))
	t18_text = []
	for i in request.list_sessions:
			if i[5] == 18 or i[5] == 15:
				l = []
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nPincode : *{i[9]}*\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				l.append(i[4])
				l.append(i[5])
				t18_text.append(l)


def text_18_two(this):
	global t18_text
	data_18 = []
	request.request_two(request.get_date(this))
	t18_text = []
	for i in request.list_sessions:
			if i[5] == 18 or i[5] == 15:
				l = []
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nPincode : *{i[9]}*\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{i[5]}*\nVaccine : *{i[4]}*'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				l.append(i[4])
				l.append(i[5])
				t18_text.append(l)


def text_45_one(this):
	global t45_text
	data_45 = []
	request.request_one(request.get_date(this))
	t45_text = []
	for i in request.list_sessions:
			if (i[5] == 45) or (i[5] == 18 and i[10] == True):
				l = []
				if i[10] == True:
					age = str(i[5]) + " (All Ages)"
				else:
					age = str(i[5])
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nPincode : *{i[9]}*\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{age}*\nVaccine : *{i[4]}*'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				l.append(i[4])
				l.append(i[5])
				t45_text.append(l)


def text_45_two(this):
	global t45_text
	data_45 = []
	request.request_two(request.get_date(this))
	t45_text = []
	for i in request.list_sessions:
			if (i[5] == 45) or (i[5] == 18 and i[10] == True):
				l = []
				if i[10] == True:
					age = str(i[5]) + " (All Ages)"
				else:
					age = str(i[5])
				text = f'Centre : *{i[0]}*\nAddress : {i[1]}\nPincode : *{i[9]}*\nDate : *{i[3]}*\n*Dose1* : {i[6]}\n*Dose2* : {i[7]}\nFee : *{i[2]}*\nMinAge : *{age}*\nVaccine : *{i[4]}*'
				l.append(text)
				l.append(i[0])
				l.append(i[8])
				l.append(i[3])
				l.append(i[4])
				l.append(i[5])
				t45_text.append(l)

def send_18_one():
	for this in range(number_of_days_check_18):
		text_18_one(this)
		for i in t18_text:
			try:
				if (i[2] > minimum_doses_under_18):
					doc_name = str(i[1]) + str(i[4]) + str(i[3])
					if i[5] == 18:
						doc = bot.db_under45.collection("18plus").document(doc_name)
					elif i[5] == 15:
						doc = bot.db_under45.collection("15plus").document(doc_name)
					a = doc.get().to_dict()
					c = int(a.get("total_dose"))
					d = str(a.get("date"))
				if (c+10 < i[2]) and (i[2] > minimum_doses_under_18):
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)
					if SEND_18PLUS_group:
						bot.bot.send_message( bot.app_secrets._18plus_groupid,i[0],parse_mode ="Markdown",reply_markup = bot.markup)
					# print(i[0])
					if personal.PERSONAL_RUN:
						personal.personal_notify(i[4] , i[3] , i[0] , i[5])

			except:
				if i[2]>minimum_doses_under_18:
					doc_name = str(i[1]) + str(i[4]) + str(i[3])
					if i[5] == 18:
						doc = bot.db_under45.collection("18plus").document(doc_name)
					elif i[5] == 15:
						doc = bot.db_under45.collection("15plus").document(doc_name)
					doc.set({"date" : i[3] , "total_dose" : i[2]})
					if SEND_18PLUS_group:
						bot.bot.send_message( bot.app_secrets._18plus_groupid,i[0],parse_mode ="Markdown",reply_markup = bot.markup)
					# print(i[0])
					if personal.PERSONAL_RUN:
						personal.personal_notify(i[4] , i[3] , i[0], i[5])

def send_18_two():
	for this in range(number_of_days_check_18):
		text_18_two(this)
		for i in t18_text:
			try:
				if (i[2] > minimum_doses_under_18):
					doc_name = str(i[1]) + str(i[4]) + str(i[3])
					if i[5] == 18:
						doc = bot.db_under45.collection("18plus").document(doc_name)
					elif i[5] == 15:
						doc = bot.db_under45.collection("15plus").document(doc_name)
					a = doc.get().to_dict()
					c = int(a.get("total_dose"))
					d = str(a.get("date"))
				if (c+10 < i[2]) and (i[2] > minimum_doses_under_18):
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)
					if SEND_18PLUS_group:
						bot.bot.send_message( bot.app_secrets._18plus_groupid,i[0],parse_mode ="Markdown",reply_markup = bot.markup)
					# print(i[0])
					if personal.PERSONAL_RUN:
						personal.personal_notify(i[4] , i[3] , i[0], i[5])

			except:
				if i[2]>minimum_doses_under_18:
					doc_name = str(i[1]) + str(i[4]) + str(i[3])
					if i[5] == 18:
						doc = bot.db_under45.collection("18plus").document(doc_name)
					elif i[5] == 15:
						doc = bot.db_under45.collection("15plus").document(doc_name)
					doc.set({"date" : i[3] , "total_dose" : i[2]})
					if SEND_18PLUS_group:
						bot.bot.send_message( bot.app_secrets._18plus_groupid,i[0],parse_mode ="Markdown",reply_markup = bot.markup)
					# print(i[0])
					if personal.PERSONAL_RUN:
						personal.personal_notify(i[4] , i[3] , i[0], i[5])

def send_45_one():
	for this in range(number_of_days_check_45):
		text_45_one(this)
		for i in t45_text:
			try:
				if (i[2] > minimum_doses_above_45):
					doc_name = str(i[1]) + str(i[4]) + str(i[3])
					doc = bot.db_above45.collection("45plus").document(doc_name)
					a = doc.get().to_dict()
					c = int(a.get("total_dose"))
					d = str(a.get("date"))
				if (c + 10 < i[2]) and (i[2] > minimum_doses_above_45):
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)
					if SEND_45PLUS_group:
						bot.bot.send_message( bot.app_secrets._45plus_groupid,i[0],parse_mode ="Markdown",reply_markup = bot.markup)
					# print(i[0])
					if personal.PERSONAL_RUN:
						personal.personal_notify(i[4] , i[3] , i[0], i[5])

			except:
				if i[2]>minimum_doses_above_45:
					doc_name = str(i[1]) + str(i[4]) + str(i[3])
					doc = bot.db_above45.collection("45plus").document(doc_name)
					doc.set({"date" : i[3] , "total_dose" : i[2]})
					if SEND_45PLUS_group:
						bot.bot.send_message( bot.app_secrets._45plus_groupid,i[0],parse_mode ="Markdown",reply_markup = bot.markup)
					# print(i[0])
					if personal.PERSONAL_RUN:
						personal.personal_notify(i[4] , i[3] , i[0], i[5])

def send_45_two():
	for this in range(number_of_days_check_45):
		text_45_two(this)
		for i in t45_text:
			try:
				if (i[2] > minimum_doses_above_45):
					doc_name = str(i[1]) + str(i[4]) + str(i[3])
					doc = bot.db_above45.collection("45plus").document(doc_name)
					a = doc.get().to_dict()
					c = int(a.get("total_dose"))
					d = str(a.get("date"))
				if (c + 10 < i[2]) and (i[2] > minimum_doses_above_45):
					b = {"total_dose": i[2]}
					a.update(b)
					doc.set(a)
					if SEND_45PLUS_group:
						bot.bot.send_message( bot.app_secrets._45plus_groupid,i[0],parse_mode ="Markdown",reply_markup = bot.markup)
					# print(i[0])
					if personal.PERSONAL_RUN:
						personal.personal_notify(i[4] , i[3] , i[0], i[5])

			except:
				if i[2]>minimum_doses_above_45:
					doc_name = str(i[1]) + str(i[4]) + str(i[3])
					doc = bot.db_above45.collection("45plus").document(doc_name)
					doc.set({"date" : i[3] , "total_dose" : i[2]})
					if SEND_45PLUS_group:
						bot.bot.send_message( bot.app_secrets._45plus_groupid,i[0],parse_mode ="Markdown",reply_markup = bot.markup)
					# print(i[0])
					if personal.PERSONAL_RUN:
						personal.personal_notify(i[4] , i[3] , i[0], i[5])

# /////////////////////////////////////////////////////

def RUN():
	if (SEND_18PLUS_group) or (personal.PERSONAL_RUN and personal.PERSONAL_SEND_AGE == 18) :
		send_18_one()
		send_18_two()
	if (SEND_45PLUS_group) or (personal.PERSONAL_RUN and personal.PERSONAL_SEND_AGE == 45) :
		send_45_one()
		send_45_two()



