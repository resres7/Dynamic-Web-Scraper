#Thread for scraping twitch chat 
import time, threading, sys
from collections import deque 
from selenium import webdriver

class Look_at_chat(threading.Thread):
    """must be:
    channel=dreadztv
    nonstop=True
       optional:
       steps=5 -> need only if nonstop==False"""
    def __init__(self, steps=5, *, channel="dreadztv", nonstop=True):
        self.massages = deque("", 100)
        self.nonstop = nonstop
        if steps < 0:
            raise ValueError("Steps must be > 0")
        self.steps = steps
        self.url = 'https://www.twitch.tv/popout/' + channel + \
                          '/chat?popout='
        self.lock = threading.Lock()
        threading.Thread.__init__(self)
        
    def run(self):
        self.scrap_chat()

    def scrap_chat(self):
        # Creating driver Chrome and automaticly run thread for screping
        option = webdriver.ChromeOptions()
        option.add_argument("--incognito")
        self.driver  = webdriver.Chrome()
        self.driver.get(self.url)
        time.sleep(5)
        print("driver started")
        self.thread = threading.Thread(target=self.theread_for_craping).start()
    
    def theread_for_craping(self):
        # Function with thread like scraping webpage
        try:
            while self.steps or self.nonstop:
                time.sleep(4)
                now_msg = [elem.text for elem in 
                            (self.driver.find_elements_by_class_name
                            ('chat-line__message'))]
                try:
                    last_msg = self.massages[-1]
                    with self.lock:
                        self.massages.extend(now_msg[now_msg.index(last_msg)+1:])
                except IndexError:
                    with self.lock:
                        self.massages.extend(now_msg)
                if self.steps != 0: 
                    self.steps -= 1
        finally:
            self.driver.close()
            print("driver was quited")
            sys.exit()
    
    def stop_scraping(self):
        self.nonstop = False
        self.steps = 1


if __name__ == "__main__":
    lat = Look_at_chat(channel="sacriel", steps=3)
    lat.start()
    for i in range(6):
        time.sleep(3)
        try:
            print("\n".join(list(lat.massages)))
        except Exception as e:
            print(e)
    print("STOP")
    lat.stop_scraping()
    time.sleep(4)