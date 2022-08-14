#This is a program to pull a random workout of the day
#Requires reqeusts and bs4 to be installed. Install with "python3 -m pip install <requests/bs4>"
import random
import requests
from bs4 import BeautifulSoup

#generate random crossfit WOD
ranyr = str(random.randint(17,21)) #generate a random year between 2017-2022
ranmo = str(random.randint(1,12)).zfill(2) #generate a random month and add a leading 0 if needed
randa = str(random.randint(1,28)).zfill(2) #generate a random day and add a leading 0 if needed
wod = ranyr + ranmo + randa #combine the yr/mo/day in the format used on crossfit.com
website = "https://crossfit.com/"+wod #actual WOD page

#parse out only the workout
page_response = requests.get(website, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20) #pulls the random WOD webpage in full
page_content = BeautifulSoup(page_response.content, "html.parser") #uses beautifulsoup to parse the webpage
page_wod = str(page_content.find_all("div", {"class": "_wrapper_1uw7e_18 _text-block_1x7b4_17"})) #cuts webpage down to just the WOD section

#save WOD to local html for display
html_clock = '''<!DOCTYPE html>
<html lang="en" >
<class="wf-ingracondensed-n8-active wf-ingracondensed-n5-active wf-ingracondensed-n4-active wf-ingracondensed-n3-active wf-ingracondensed-n7-active wf-active"><head><meta http-equiv="Content-type" content="text/html; charset=utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet"><link rel="stylesheet" href="https://use.typekit.net/jas7dha.css">
<body onload="startTime()">

<h2>TIMER</h2>

<div id="txt"></div>

<script>
function startTime() {
  const today = new Date();
  let h = today.getHours();
  let m = today.getMinutes();
  let s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('txt').innerHTML =  h + ":" + m + ":" + s;
  setTimeout(startTime, 1000);
}

function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}
</script>

</body>'''

local_html = open("/opt/homebrew/var/www/index.html", "w") #open the local html file to write the WOD to
local_html.write(html_clock + '\n' + page_wod) #write output to local html file
local_html.close #close local html file

#you can set up a raspberry pi with a monitor to query/display the webpage in your gym to display the WOD now
