from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from krwordrank.word import summarize_with_keywords
import time
import csv

packageName = [<app_package_name_1>, <app_package_name_2>, <app_package_name_3>]
maxReviewCountThreshold = 8000
texts_1 = []
texts_2 = []
texts_3 = []
texts_4 = []
texts_5 = []
stopwords = []

file = open('result.csv', mode='w', newline='\n', encoding='cp949')
writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer.writerow(["game","name","ratings","date","comment"])

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

for id in packageName:
    # Open web page
    link = "https://play.google.com/store/apps/details?id=" + id + "&hl=ko&showAllReviews=true"
    driver.get(link)
    time.sleep(3)

    print("Loading... "+id)

    # Show all reviews
    driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[4]/section/div/div/div[5]/div/div/button").click()
    time.sleep(1)

    # Scroll to end
    reviewContainer = driver.find_element(By.XPATH, "/html/body")
    reviewContainer.click()
    reviews = []

    prevReviewCount = 0
    reviewCountCheckThreshold = 5
    reviewCountCheckFlag = 0

    while 1:
        reviewContainer.send_keys(Keys.END)
        time.sleep(1)

        reviews = driver.find_elements(By.XPATH, "//div[@class='RHo1pe']")
        print("[" + str(len(reviews)) + "]", end = '\r')

        if maxReviewCountThreshold <= len(reviews):
            break
        elif prevReviewCount == len(reviews):
            reviewCountCheckFlag = reviewCountCheckFlag + 1
            if reviewCountCheckFlag >= reviewCountCheckThreshold:
                break
        else:
            reviewCountCheckFlag = 0
            prevReviewCount = len(reviews)

    print("Done. There are " + str(len(reviews)) + " reviews avaliable in " + id)
    print("Writing the data...")

    reviewIdx = 0
    for review in reviews:
        soup = BeautifulSoup(review.get_attribute("innerHTML"), "lxml")
        name = soup.find(class_="X5PpBb").text
        name = name.encode('cp949', 'replace').decode('cp949', 'replace')
        ratings = soup.find('div',role='img').get('aria-label')[10]
        date = soup.find(class_="bp9Aid").text
        comment = soup.find(class_="h3YV2d").text
        comment = comment.encode('cp949', 'replace').decode('cp949', 'replace')

        writer.writerow([id, name, ratings, date, comment])

        if ratings == "1":
            texts_1.append(comment)
        elif ratings == "2":
            texts_2.append(comment)
        elif ratings == "3":
            texts_3.append(comment)
        elif ratings == "4":
            texts_4.append(comment)
        elif ratings == "5":
            texts_5.append(comment)

        reviewIdx = reviewIdx + 1
        print("[" + str(reviewIdx) + "/" + str(len(reviews)) + "]", end = '\r')

    print("Done. [" + str(reviewIdx) + "/" + str(len(reviews)) + "]")

file.close()
print("\n")

print("5 ====")
keywords = summarize_with_keywords(texts_5, stopwords=stopwords, verbose=True)
for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
    print('%8s:\t%.4f' % (word, r))

print("4 ====")
keywords = summarize_with_keywords(texts_4, stopwords=stopwords, verbose=True)
for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
    print('%8s:\t%.4f' % (word, r))

print("3 ====")
keywords = summarize_with_keywords(texts_3, stopwords=stopwords, verbose=True)
for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
    print('%8s:\t%.4f' % (word, r))

print("2 ====")
keywords = summarize_with_keywords(texts_2, stopwords=stopwords, verbose=True)
for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
    print('%8s:\t%.4f' % (word, r))

print("1 ====")
keywords = summarize_with_keywords(texts_1, stopwords=stopwords, verbose=True)
for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
    print('%8s:\t%.4f' % (word, r))

print("Process Done.")