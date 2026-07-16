# Discord Job Hunter Bot 🔍

A simple, functional Discord bot that pulls real-time job listings from LinkedIn, Indeed, and Glassdoor directly into your Discord server using the JSearch API. 

I built this script because manually checking multiple job boards every morning is exhausting and full of spam. With this bot, I can just type a command in my server and get the latest postings instantly.

I made only 5 jobs shwon, but you can change it in the code.

## ✨ Features
- **Real-time Search:** Fetches fresh job postings based on any keyword and location you want.
- **Clean UI:** Displays results nicely using Discord Embeds (Company, Location, Job Type, and Source).
- **Direct Apply:** One-click links that take you straight to the official application page.

## 🛠️ Built With
- **Python 3**
- [discord.py](https://discordpy.readthedocs.io/) - Discord API wrapper
- [Requests](https://pypi.org/project/requests/) - HTTP library
- [JSearch API](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) (via RapidAPI) - Job aggregator engine

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
```

### 2. Install dependencies
Make sure you have Python installed, then run:
~~~bash
pip install -r requirements.txt
~~~

### 3. Get your API Keys & Tokens (Free)
Before running the code, you need to grab two free credentials:

**A. Discord Bot Token:**
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a **New Application**.
2. Go to the **Bot** tab on the left menu, click **Reset Token**, and copy your token.
3. *Important:* Scroll down on the Bot tab and enable **Message Content Intent** so the bot can read your commands.
4. Go to **OAuth2 -> URL Generator**, check `bot` and `Send Messages`, then paste the generated URL in your browser to invite the bot to your Discord server.

**B. RapidAPI Key (JSearch):**
1. Create a free account on [RapidAPI](https://rapidapi.com/) and go to the [JSearch API page](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch).
2. Click **Subscribe to Test** and choose the **Basic (Free)** plan (gives you 200 free requests/month, more than enough for personal use).
3. On the API playground page, copy your **X-RapidAPI-Key**.

### 4. Set up environment variables
Create a file named `.env` in the root folder of your project and paste your keys like this:

~~~env
DISCORD_TOKEN=your_discord_bot_token_here
RAPIDAPI_KEY=your_rapidapi_key_here
~~~
*(Note: Never share or commit your `.env` file to GitHub! Make sure `.env` is listed in your `.gitignore`)*

### 5. Run the bot
~~~bash
python bot.py
~~~

## 💡 How to Use
Once the bot is online in your server, simply use the `!fjob` command followed by your search keyword:

~~~text
!fjob junior frontend developer remote
~~~
Or just type `!fjob` to use the default search query.

---
*Feel free to fork this repo and tweak the search filters to fit your own job hunting needs!*
