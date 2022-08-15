# WOD_randomizer
Simple script to pull a random WOD from crossfit.com (workout only) and can then be displayed on a monitor in your gym. Local HTML file displays a timer for ease of tracking/timing WODs. 
Run the WOD_randomizer script and then browse to localhost:8080 (or wherever apache is configured for) to display. Would work best if running on a Raspberry Pi W that is connected to a monitor in your gym. Then, you could setup a cron to run daily at midnight to refresh the WOD automatically and have it displayed for use. 

![alt text](https://github.com/JasonBurnsInfosec/WOD_randomizer/blob/040812102749a0975bd35e6774b5f6510890cd5a/Screen%20Shot%202022-08-14%20at%203.22.55%20PM.png)

Need to add error handling for request fails or random rolls that land on rest day WODs. Could use some css beautifying but come on, who cares. You can also just add a quick HTTP server to the python itself and serve the WOD from there, I just wanted to send it to my apache server instead.

The real purpose of this was to practice web scraping, parsing, transforming, and utilizing arbitrary web data. 
