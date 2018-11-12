import vk
import requests
import re
import itertools
import json
from personal import ACCESS_TOKEN,USER_ID

def send_vk_api_request(method,params):
	token = "access_token={}".format(ACCESS_TOKEN);
	request = "https://api.vk.com/method/"+ method +"?"+ params +"&"+ token+"&" + "v=5.85";
	sent_request = requests.get(request).text
	return(sent_request)

def parse_vk_groups_of_user():
	list_of_ids = []
	method = "groups.get";
	params = "user_id={}&extended=1&fields=id,name".format(USER_ID)
	result_request = send_vk_api_request(method,params)
	list_of_ids = re.findall('"id":[0-9]*',result_request)
	done_ready_list_of_ids = []
	i = 0
	j = 0
	for i in range(len(list_of_ids)):
		done_ready_list_of_ids.append(re.findall('[0-9]*',list_of_ids[i]))
		done_ready_list_of_ids[i] = list(filter(None,done_ready_list_of_ids[i]))
	done_ready_list_of_ids = list(itertools.chain.from_iterable(done_ready_list_of_ids))
	return(done_ready_list_of_ids)


def get_wall_of_group(groups_list):

	method = "wall.get";
	params = "owner_id=-{}&count=2".format(groups_list[0])
	result_request = send_vk_api_request(method,params)
	print(result_request)



	
x = parse_vk_groups_of_user()
get_wall_of_group(x)








