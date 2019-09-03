from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import datetime


class MyApp(App):
	def build(self):
		self.formula = ''
		bl = BoxLayout(orientation = 'vertical')
		bl.add_widget(Button(text = 'Расписание',
					on_press = self.btn_press,
					background_color = [0,0,0,1],
					background_normal = '',
					))
		return bl
	def btn_press(self, instance):
		otvet = ''
		x=''
		n = datetime.datetime.now()
		weekday = datetime.date.weekday(n)
		n = str(n)
		date, time = n.split()
		hour,minute,second = time.split(':')
		year, month, day = date.split('-')
		weekday+=1
		hour=int(hour)
		minute = int(minute)
		date_base = [["8.30","9.10","9.20","10.00","10.20","11.00","11.20","12.00","12.15","12.55","13.5","13.45","13.55","14.35","14.50","15.30"]]
		if weekday <= 5:
			for i in range (15):
				hour1, minute1 = date_base[0][i].split('.')
				hour2, minute2 = date_base[0][i+1].split('.')
				hour1= int(hour1)
				hour2=int(hour2)
				minute2=int(minute2)
				minute1=int(minute1)
				time1 = hour1 * 60 + minute1
				time2 = hour2*60 + minute2
				time = hour*60 + minute
				if time <= time2 and time >= time1:
					otvet = ('Осталось '+str(time2 - time)+' м'+'\n'+"Прошло "+ str(time - time1) + ' м') 
					break
				if time > 930:
					otvet = ('Уроки закончились')
					break
		
		elif weekday == 7:
			otvet = ('Sunday Funday')
		instance.text = otvet


if __name__ == '__main__':
	MyApp().run()