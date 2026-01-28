import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import asyncio
from telegram import Bot
import os
import dotenv
import time
import re

# Carregar variáveis de ambiente do arquivo .env
dotenv.load_dotenv()
TELEGRAM_TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Criando a classe de Selenium + Scraper
class SeleniumScraper:
    def __init__(self, url):
        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless=new")
        # Desabilitar GPU e logs para melhorar a performance
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(options=self.options)

    def scraper(self):
        self.driver.get(self.url)
        time.sleep(15) # Espera 15 antes de fechar a página
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        self.driver.quit()
        return soup

# Criando a classe de envio de mensagem no Telegram
class TelegramBot:
    def __init__(self, token):
        self.bot = Bot(token=token)
        self.token = token

    async def send_message(self, chat_id, message):
        await self.bot.send_message(chat_id=chat_id, text=message)

# Criando a classe de extração de preço
class PriceExtractor:
    def __init__(self, url):
        self.url = url
    
    # Função para conseguir o preço
    def get_price(self, product_name):
        print(f"Buscando preço em: {self.url}...")
        scraper = SeleniumScraper(self.url)
        soup = scraper.scraper()
        # Aqui fazemos uma verificação de estoque
        if soup.find("input", {"value": "Avise-me quando chegar"}) or \
           soup.find(string=lambda t: t and "Indisponível" in t):
            return "Produto Esgotado/Indisponível"
        price_element = soup.find("span", string=re.compile(r"R\$"))
        # Verificando se o elemento foi encontrado
        raw_price = price_element.get_text(strip=True) if price_element else "Preço não encontrado"  # O get_text() pega todo o texto dentro da tag
        #print(f"Preço encontrado: {raw_price}")
        return f"{product_name}: {raw_price}"

    # Função para enviar a mensagem no telegram
    def send_message(self, chat_id, message):
        bot = TelegramBot(token=TELEGRAM_TOKEN)
        asyncio.run(bot.send_message(chat_id=chat_id, message=message))

# Função principal
urls = {
    'Creatina Growth 250g': "https://www.gsuplementos.com.br/creatina-monohidratada-250gr-growth-supplements-p985931",
    'Medium Whey Protein': "https://www.gsuplementos.com.br/medium-whey-protein-1kg-growth-supplements-p986001"
}
if __name__ == "__main__":
    for product_name, url in urls.items():
        result = PriceExtractor(url).get_price(product_name)
        PriceExtractor(url).send_message(CHAT_ID, result)
        #print(f"Resultado Final: {result}")
