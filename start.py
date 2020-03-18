#selenium module nedeed (pip install selenium)
#webdriver needed, get one of these {geckodriver, chromedriver, operadriver}
import sys
from bot_class import MoodleBot


if len(sys.argv) > 1:
    browser = sys.argv[1]
else:
    print("Nie podano przegladarki zainstalowanego webdrivera. Podaj go w argumencie {firefox, chrome, opera}")
    print("Webdriver powinien znajdować się w /usr/local/bin lub /usr/bin")
    exit()

#są 3 metody Xd

moodleBot = MoodleBot(browser)
moodleBot.login()
moodleBot.make_dic()
moodleBot.get_to_course()


