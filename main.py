from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        email = bot.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[1]/div/label/div[2]/div/input')
        password = bot.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[2]/div/label/div[2]/div/input')
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        bot.get('https://twitter.com/7eVaNM')
        print('Going to page...')

    def recentTweet(self):
        time.sleep(5)
        bot = self.bot
        tweet = bot.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[1]/div/article/div/div[2]/div[2]/div[2]/span').get_attribute('innerHTML')
        print('Most Recent Tweet: ' + tweet.rstrip())
        return tweet

    def compareTweets(self):
        bot = self.bot
        bot.get('https://twitter.com/7eVaNM')
        time.sleep(2)
        tweettxt = open('tweet.txt', 'r+')
        tweetsArray = tweettxt.readlines()
        last_tweet = tweetsArray[len(tweetsArray) - 1]
        last_stripped = last_tweet.strip()
        print('Last Tweet: ' + last_tweet.rstrip())
        recent = self.recentTweet()
        recent_stripped = recent.strip()
        if (last_stripped != recent_stripped):
            tweettxt.write(recent + "\n")
            tweettxt.close()
            return True
        print('Did not tweet')
        return False

    def reply(self, tweet):
        time.sleep(5)
        bot = self.bot
        clickTweet = bot.find_element_by_css_selector(
            'div.r-1ljd8xs:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > article:nth-child(1)')
        clickTweet.click()
        time.sleep(2)
        replyButton = bot.find_element_by_css_selector(
            'div.r-3qxfft:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        replyButton.click()
        time.sleep(2)
        tweetField = bot.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div')
        tweetField.send_keys(tweet)
        sendButton = bot.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]')
        sendButton.click()
        print('Tweeted Successfully!')
        time.sleep(1)
        exitButton = bot.find_element_by_css_selector('div.r-53xb7h')
        exitButton.click()
        print('Exiting')


EvanPoggers = TwitterBot('EvanPoggers', 'EvanPoggersxD')
EvanPoggers.login()

while(True):
    if(EvanPoggers.compareTweets()):
        EvanPoggers.reply('Poggers')
    print('Waiting 20 seconds')
    time.sleep(20)
