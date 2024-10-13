from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

url = 'http://127.0.0.1:5500/'
driver.get(url)
driver.maximize_window()

sleep(1)

date = driver.find_element('id', 'date').send_keys('13.10.2024')
city = driver.find_element('id', 'city').send_keys('Иркутск')

fio_pro = driver.find_element('id', 'fio_pro').send_keys('Тепляков Владислав Алексеевич')
date_birth_pro = driver.find_element('id', 'date_birth_pro').send_keys('25.04.1992')
pasport_pro_s = driver.find_element('id', 'pasport_pro_s').send_keys('00 00')
pasport_pro_n = driver.find_element('id', 'pasport_pro_n').send_keys('000001')
pasport_pro_kod = driver.find_element('id', 'pasport_pro_kod').send_keys('000-001')
pasport_pro_date = driver.find_element('id', 'pasport_pro_date').send_keys('00.00.0001')
pasport_pro_reg = driver.find_element('id', 'pasport_pro_reg').send_keys('УВД №1')

fio_po = driver.find_element('id', 'fio_po').send_keys('Крафилов Крафил Некрафилович')
date_birth_po = driver.find_element('id', 'date_birth_po').send_keys('00.00.0000')
pasport_po_s = driver.find_element('id', 'pasport_po_s').send_keys('00 00')
pasport_po_n = driver.find_element('id', 'pasport_po_n').send_keys('000002')
pasport_po_kod = driver.find_element('id', 'pasport_po_kod').send_keys('000-002')
pasport_po_date = driver.find_element('id', 'pasport_po_date').send_keys('00.00.0002')
pasport_po_reg = driver.find_element('id', 'pasport_po_reg').send_keys('УВД №2')

model = driver.find_element('id', 'model').send_keys('Honda Fit Shuttle')
vin = driver.find_element('id', 'vin').send_keys('ОТСУТСТВУЕТ')
type = driver.find_element('id', 'type').send_keys('Универсал')
year = driver.find_element('id', 'year').send_keys('2014')
engine_m = driver.find_element('id', 'engine_m').send_keys('NNN')
engine_n = driver.find_element('id', 'engine_n').send_keys('666666')
frame = driver.find_element('id', 'frame').send_keys('123 1234 12345')
body = driver.find_element('id', 'body').send_keys('NN0-000000')
km = driver.find_element('id', 'km').send_keys('500 000')
color = driver.find_element('id', 'color').send_keys('БЕЛЫЙ')

pts_s = driver.find_element('id', 'pts_s').send_keys('11')
pts_n = driver.find_element('id', 'pts_n').send_keys('111111')
pts_date = driver.find_element('id', 'pts_date').send_keys('00.00.0000')
pts_reg = driver.find_element('id', 'pts_reg').send_keys('№1')

sts_s = driver.find_element('id', 'sts_s').send_keys('22')
sts_n = driver.find_element('id', 'sts_n').send_keys('222222')
sts_date = driver.find_element('id', 'sts_date').send_keys('00.00.0000')
sts_reg = driver.find_element('id', 'sts_reg').send_keys('№2')

number = driver.find_element('id', 'number').send_keys('B 777 OP 777')
price = driver.find_element('id', 'price').send_keys('1 050 000')

sleep(200)
