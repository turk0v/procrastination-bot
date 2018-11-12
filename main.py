from vk_parse import parse_vk_groups_of_user
from youtube_parse import parse_youtube_vids
from telegram_parse import parse_telegram_channels
from sites_parse import parse_sites_rss

# def page_is_loaded(driver):
# 	return driver.find_element_by_tag_name('body') != None

# # logging into site 
# driver = webdriver.Chrome(pass_to_chromedriver)#pass to chromedriver
# driver.get("https://track.mail.ru/pages/index/#")
# wait = WebDriverWait(driver,10)
# wait.until(page_is_loaded)

VK_GROUP_LIST = []
YOUTUBE_SUBS = []
TELEGRAM = []
SITES_TO_RSS = []

def main():
	results_of_parse = []
	results_of_parse.append(parse_vk_groups_of_user())
	results_of_parse.append(parse_youtube_vids())
	results_of_parse.append(parse_telegram_channels())
	results_of_parse.append(parse_sites_rss())
	print(results_of_parse)



if __name__ == "__main__":
	main()
