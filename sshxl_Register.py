import requests
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from selenium.webdriver.support.ui import Select
import threading
from datetime import datetime, timedelta



# ******************************************************************
# *                                                                *
# *                    Copyright by Elsurnite                      *
# *                      Telegram: Elsurnite                       *
# *                                                                *
# ******************************************************************


def randevu_telegram_message():
        bot_token = "" # Bot Token
        chat_id = "" # Chat ID
        current_otp = "YURT RANDEVUSU AÇILDI!"  # Buraya göndermek istediğiniz mesajı ekleyin veya değişken olarak tanımlayın

        response = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={"chat_id": chat_id, "text": current_otp})

        if response.ok:
            print(f"Telegram mesajı gönderildi: {current_otp}")
        else:
            print(f"Telegram mesajı gönderme hatası: {response.status_code}")

        # Her dakika mesaj gönderme aralığı
        time.sleep(1)

def send_telegram_message():
    while True:
        bot_token = ""  #Bot Token
        chat_id = "" #Chat ID
        current_otp = "Hello World!"  # Buraya göndermek istediğiniz mesajı ekleyin veya değişken olarak tanımlayın

        response = requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={"chat_id": chat_id, "text": current_otp})

        if response.ok:
            print(f"Telegram mesajı gönderildi: {current_otp}")
        else:
            print(f"Telegram mesajı gönderme hatası: {response.status_code}")

        # Mesaj gönderme aralığı
        time.sleep(180)

# İş parçacığı oluşturup başlatma
telegram_thread = threading.Thread(target=send_telegram_message, daemon=True)
telegram_thread.start()



# SMS gönderme fonksiyonu
def send_sms():
    # SMS API bilgileri
    sms_url = "https://api.vatansms.net/api/v1/1toN"
    sms_data = {
        "api_id": "",
        "api_key": "",
        "sender": "",
        "message_type": "turkce",
        "message": " YURT KAYITLARI AÇILDI",
        "message_content_type": "bilgi",
        "phones": ["",""]
    }
    
    # SMS gönderme isteği
    try:
        response = requests.post(sms_url, json=sms_data)
        response.raise_for_status()  # Hata durumunda istisna fırlat
        print("SMS başarıyla gönderildi.")
    except requests.exceptions.RequestException as e:
        print("SMS gönderilirken bir hata oluştu:", e)


Edge_options = webdriver.EdgeOptions()
Edge_options.add_argument("--incognito")
Edge_options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Edge(options=Edge_options)
wait = WebDriverWait(driver, 3)



def load_page():
    driver.get("https://www.sshxl.nl/en/register/short-stay")
    driver.implicitly_wait(30)

# 2025 seçeneğine tıklayan ve ardından "123" değerini metin kutusuna yazan bir fonksiyon tanımlayın
def select_and_fill():
    try:
        time.sleep(1)
        radio_button = driver.find_element(By.ID, "radio-city--1fca77bb-5065-4185-8b16-0dbb57ecc1f7")
        driver.execute_script("arguments[0].click();", radio_button)
        time.sleep(1)

        erasmus_option = driver.find_element(By.XPATH, "//option[contains(text(), 'Erasmus University Rotterdam (EUR)')]")
        erasmus_option.click()
        time.sleep(1)

        ese_ibe_option = driver.find_element(By.XPATH, "//option[contains(text(), 'ESE/IBEB - Econometrics')]")
        ese_ibe_option.click()
        time.sleep(1)

        bachelor_option = driver.find_element(By.CSS_SELECTOR, "option[value='944c5e71-b029-487a-8931-dbf85c4f7d17']")
        bachelor_option.click()
        time.sleep(1)

        Housing_option = driver.find_element(By.XPATH, "//option[contains(text(), 'Bachelor Full Year 2024-2025')]")
        Housing_option.click()
        send_sms()
        randevu_telegram_message()

        # "2025" seçeneği tıklandığında, "123" değerini metin kutusuna gir
        student_number_input = driver.find_element(By.ID, "studentNumber")
        student_number_input.clear()
        student_number_input.send_keys("")# Öğrenci Numarası


        button = driver.find_element(By.XPATH,"//button[contains(@class, 'button--primary') and contains(text(), 'Next')]")
        button.click()
        driver.implicitly_wait(30)


        student_number_input = driver.find_element(By.ID, "firstname")
        student_number_input.clear()
        student_number_input.send_keys("")#İsim eğer varsa 2. isim
        time.sleep(1)

        student_number_input = driver.find_element(By.ID, "lastname")
        student_number_input.clear()
        student_number_input.send_keys("")#Soyad
        time.sleep(1)   
        
        radio_button = driver.find_element(By.ID, "radio-gender--Man")
        driver.execute_script("arguments[0].click();", radio_button)
        time.sleep(1)

        input_element = driver.find_element(By.CSS_SELECTOR, "input[name='Date of birthDay']")
        # İçeriği '4' olarak ayarla
        input_element.send_keys("")#Doğum Günü
        time.sleep(1)


        input_element = driver.find_element(By.CSS_SELECTOR, "input[name='Date of birthMonth']")
        # İçeriği '4' olarak ayarla
        input_element.send_keys("")#Doğum Ayı
        time.sleep(1)


        input_element = driver.find_element(By.CSS_SELECTOR, "input[name='Date of birthYear']")
        # İçeriği '4' olarak ayarla
        input_element.send_keys("")#Doğum Yılı
        time.sleep(1)

        radio_button = driver.find_element(By.ID, "radio-nationality--Niet Nederlands")
        driver.execute_script("arguments[0].click();", radio_button)
        time.sleep(1)

        button = driver.find_element(By.XPATH,"//button[contains(@class, 'button--primary') and contains(text(), 'Next')]")
        button.click()
        time.sleep(2)

        student_number_input = driver.find_element(By.ID, "email")
        student_number_input.clear()
        student_number_input.send_keys("")#Email
        time.sleep(1)

        number_option = driver.find_element(By.CSS_SELECTOR, "option[value='TR']")
        number_option.click()
        time.sleep(1)

        element = driver.find_element(By.CSS_SELECTOR, "input.phonefield__input")
        # İçeriği '123' olarak ayarlas
        element.clear()  # Mevcut değeri temizle
        element.send_keys("")#Telefon Numarası
        time.sleep(1)


        student_number_input = driver.find_element(By.ID, "password")
        student_number_input.clear()
        student_number_input.send_keys("")#Şifre
        time.sleep(1)

        student_number_input = driver.find_element(By.ID, "password-verify")
        student_number_input.clear()
        student_number_input.send_keys("")#Şifre tekrar
        time.sleep(1)

        time.sleep(1)
        checkbox_script = """   
var checkbox = document.getElementById('check-accepts-toc');
checkbox.click();
"""

        driver.execute_script(checkbox_script)
        time.sleep(1)

        button = driver.find_element(By.XPATH,"//button[contains(@class, 'button--primary') and contains(text(), 'Next')]")
        button.click()
        driver.implicitly_wait(30)

        print("Hesap Oluşturuldu")

    except Exception as e:
        print("Bir hata oluştu:", e)

# Sonsuz bir döngü oluşturun ve her seferinde sayfayı yükleyin ve ardından işlemleri gerçekleştirin
while True:
    load_page()     
    select_and_fill()
