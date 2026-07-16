import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

RAPIDAPI_KEY = "YOUR RAPID API KEY"
DISCORD_TOKEN = (
    "YOUR_DISCORD_TOKEN"
)


@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} Bot online, ready to find a jobs!")


@bot.command()
async def fjob(ctx, *, keyword="Frontend"):

    await ctx.send(
        f"🔍 *finding job for:* **{keyword}**...\nPlease wait!"
    )

    url = "https://jsearch.p.rapidapi.com/search-v2"
    querystring = {
        "query": keyword,
        "page": "1",
        "num_pages": "1",
        "date_posted": "all", 
    }
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com",
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        hasil_api = data.get("data", [])

        if isinstance(hasil_api, dict):
            jobs = []
            for val in hasil_api.values():
                if isinstance(val, list):
                    jobs = val
                    break
        else:
            jobs = hasil_api

        jobs = jobs[:5]

        if not jobs:
            await ctx.send(
                "❌ *error, no jobs found!*"
            )
            return

        for job in jobs:
            title = job.get("job_title", "No Title")
            company = job.get("employer_name", "company not found")

            city = job.get("job_city", "") or ""
            country = job.get("job_country", "") or ""
            location = (
                f"{city}, {country}".strip(", ")
                if (city or country)
                else "Unknown Location!"
            )

            apply_link = job.get("job_apply_link", "https://linkedin.com")
            platform = job.get("job_publisher", "LinkedIn / Various")
            job_type = job.get("job_employment_type", "Full-time") or "Full-time"

            embed = discord.Embed(
                title=f"🚀 Job Found: {title}",
                url=apply_link,
                color=discord.Color.blue(),
            )
            embed.add_field(name="🏢 Company", value=company, inline=True)
            embed.add_field(name="📍 Location", value=location, inline=True)
            embed.add_field(
                name="💼 Type", value=job_type.capitalize(), inline=True
            )
            embed.add_field(name="🌐 Source", value=f"*{platform}*", inline=False)
            embed.set_footer(text="💡 Click the job title above to apply!")

            await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(
            "⚠️ *Error Happend, Check your api key or connection!*"
        )
        print(f"Error details: {e}")


# Jalankan bot
bot.run(DISCORD_TOKEN)
