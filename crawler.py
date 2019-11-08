from selenium import webdriver
from bs4 import BeautifulSoup
from krwordrank.word import summarize_with_keywords
import time
import csv

packageName = [<app_package_name_1>, <app_package_name_2>, <app_package_name_3>]
maxPage = 50
texts_1 = []
texts_2 = []
texts_3 = []
texts_4 = []
texts_5 = []
stopwords = []

file = open('result.csv', mode='w', newline='\n', encoding='cp949')
writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer.writerow(["game","name","ratings","comment"])
driver = webdriver.Chrome(<location_of_chromedriver.exe>)

for id in packageName:
    # Open web page
    link = "https://play.google.com/store/apps/details?id=" + id + "&hl=ko&showAllReviews=true"
    driver.get(link)
    time.sleep(3)

    # Sort by date
#    driver.find_element_by_xpath("//*[@id='fcxH9b']/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/c-wiz/div[1]/div/div[1]/div[2]/span").click();
#    time.sleep(3)
#    driver.find_element_by_xpath("//*[@id='fcxH9b']/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/c-wiz/div[1]/div/div[2]/div[1]").click();
#    time.sleep(3)

    print("Loading... "+id)
    # Scroll to end
    scroll = 0
    flag=0
    while 1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            loadMore=driver.find_element_by_xpath("//*[contains(@class,'U26fgb O0WRkf oG5Srb C0oVfc n9lfJ')]").click()
        except:
            time.sleep(1)
            flag=flag+1
            if flag >= 10:
                break
        else:
            flag=0
            scroll=scroll+1
            print("["+str(scroll)+"/"+str(maxPage)+"]", end='\r')
            if scroll >= maxPage:
                break
    print("Done. ["+str(scroll)+"/"+str(maxPage)+"]")

    reviews=driver.find_elements_by_xpath("//*[@jsname='fk8dgd']//div[@class='d15Mdf bAhLNe']")
    reviewCount=len(reviews)
    reviewIdx=0
    print("There are "+str(reviewCount)+" reviews avaliable in " + id)
    print("Writing the data...")

    for review in reviews:
        try:
            soup=BeautifulSoup(review.get_attribute("innerHTML"),"lxml")
            name=soup.find(class_="X43Kjb").text
            ratings=soup.find('div',role='img').get('aria-label')[10]
            comment=soup.find('span',jsname='fbQN7e').text
            if not comment:#expand the comment button
                comment=soup.find('span',jsname='bN97Pc').text
        
            name = name.encode('cp949', 'replace').decode('cp949', 'replace')
            comment = comment.encode('cp949', 'replace').decode('cp949', 'replace')
            writer.writerow([id,name,ratings,comment])

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
        except:
            pass
        else:
            reviewIdx=reviewIdx+1
            print("["+str(reviewIdx)+"/"+str(reviewCount)+"]", end='\r')
    print("Done. ["+str(reviewIdx)+"/"+str(reviewCount)+"]")

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