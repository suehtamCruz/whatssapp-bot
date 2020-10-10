from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "oi sou so um bot de whatsapp!!"
        self.grupos = ["My word","Contas"] 
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        
    def EnviarMSG(self):
        # <span dir="auto" title="Contas" class="_3ko75 _5h6Y_ _3Whw5">Contas </span> // 
        # <div tabindex="-1" class="_3uMse">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo in self.grupos : 
            
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(1)
            grupo.click()
            time.sleep(1)
            chatBox = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(1)
            chatBox.click()
            time.sleep(1)
            chatBox.send_keys(self.mensagem)
            time.sleep(1)
            botaoEnviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(1)
            botaoEnviar.click()
            time.sleep(4)
            
bot = WhatsappBot()
bot.EnviarMSG()