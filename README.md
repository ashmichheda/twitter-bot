# twitter-bot
Twitter bot using Twitter APIs

### Initial Set up
1. First step, check python version using `python3 --version` **OR** `python --version` on console (terminal/shell/command prompt)

2. **If you have python 3.7, then run the below command:** <br/>
  `pip3 install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b`
  <br/> **OR** <br/>
 `pip install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b`

### Files
* **my_twitter_bot.py** - This is the main py file that includes all the logic.
* **last_seen_id.txt** - This file contains the ID of the tweet that my_twitter_bot.py has seen last. 

### Twitter Bot functionality
* My bot responds to tweets mentioning my account with the questions like 'How are you?' or 'All good?' with the text "I am good!"


#### Bot demo screen-shot
Here's my bot demo photo:

<img src = "/twitter-bot-demo.PNG" width = "410" height = "300">
