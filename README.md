# WOD_randomizer
Simple script to pull a random WOD from crossfit.com (workout only) and can then be displayed on a monitor in your gym. Local HTML file displays a timer for ease of tracking/timing WODs. 
Run the WOD_randomizer script and then browse to localhost:8080 (or wherever apache is configured for) to display. Would work best if running on a Raspberry Pi W that is connected to a monitor in your gym. Then, you could setup a cron to run daily at midnight to refresh the WOD automatically and have it displayed for use. 

![alt text](https://github.com/JasonBurnsInfosec/WOD_randomizer/blob/ec5ff21d36dae60e41c1a66c9b8e97e0626d0c3a/Screen%20Shot%202022-08-15%20at%2010.05.13%20AM.png)

Need to add error handling for request fails or random rolls that land on rest day WODs. Could use some css beautifying but come on, who cares. You can also just add a quick HTTP server to the python itself and serve the WOD from there, I just wanted to send it to my apache server instead.

The real purpose of this was to practice web scraping, parsing, transforming, and utilizing arbitrary web data. 
