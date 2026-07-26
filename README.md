# Nova!

A Discord bot.

- Language: Python (discord.py)
- Host: Render free web service
- The `DISCORD_TOKEN` is stored as a secret environment variable on the
  host — it is **never** committed to this repository.

## Keep-alive (free 24/7)

Render free services sleep after 15 minutes without traffic. A tiny HTTP
health server is injected at the top of the main file. Point a free
uptime monitor (UptimeRobot / cron-job.org) at the service URL with a
5-minute interval to keep the bot awake around the clock — free forever.
