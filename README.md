# 💊 Bot de Suplementos

> **Bot de rastreamento de estoque e preços.** Um script de Web Scraping que monitora automaticamente a disponibilidade de suplementos (Creatina, Whey) e notifica via Telegram.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Bot-Telegram_API-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

---

## 🎯 O Problema

Quem consome suplementos sabe que itens populares (como a Creatina da Growth) esgotam rapidamente. Ficar entrando no site e dando F5 o dia todo é improdutivo.

---

## 💡 A Solução

Desenvolvi um robô autônomo que:
1.  **Acessa o site** da Growth Supplements simulando um navegador real (para evitar bloqueios simples e carregar elementos dinâmicos).
2.  **Verifica o estoque:** Procura por botões de "Avise-me" ou textos de "Indisponível".
3.  **Captura o preço:** Se houver estoque, ele extrai o valor atualizado.
4.  **Notifica:** Envia um alerta instantâneo para o meu celular via Telegram.

---

## 🛠️ Arquitetura e Tecnologias

O projeto utiliza uma abordagem híbrida de scraping para garantir precisão e performance.

```mermaid
graph TD
    Start[🚀 Início do Script] -->|Lista de URLs| Selenium[🤖 Selenium WebDriver];
    Selenium -->|Headless Browser| Site[🌍 Site Growth Supplements];
    Site -->|Renderiza HTML| Soup[🍜 BeautifulSoup Parser];
    Soup -->|Analisa| Logic{Tem Estoque?};
    Logic -- Não --> Result1[Retorna: Esgotado];
    Logic -- Sim --> Result2[Extrai Preço R$];
    Result1 & Result2 -->|Envia Mensagem| Telegram[📱 API Telegram Bot];
    Telegram --> User((👤 Usuário));
