"""
на вход подается ссылка на HTML файл.
скачать этот файл,
затем найти в нем все ссылки вида <a ... href="..." ... >
вывести список сайтов, на которые есть ссылка,
в алфавитном порядке
"""
import re
import requests


def get_domain_names(url: str) -> list:
    """request url, get domain names from string like <a ... href="..." ... >"""
    domains_list = []
    page = requests.get(url=url)
    if page:
        for page_line in page.text.splitlines():
            page_line = page_line.rstrip()
            domain_pattern = r'(<a.+href=[\'\"])([^\.\.\\]\w*\:\/\/)([\w\.\-]*)'
            domain_search = re.search(pattern=domain_pattern, string=page_line)

            if domain_search:
                domain_name = domain_search.group(3)
                if domain_name not in domains_list:
                    domains_list.append(domain_name)

        domains_list.sort()
    return domains_list


# for manual input
URL = input().rstrip()


#############
## testing
#############

# URL = 'http://pastebin.com/raw/2mie4QYa'  # test 1
# URL = 'http://pastebin.com/raw/hfMThaGb'  # test 2
# URL = 'http://pastebin.com/raw/7543p0ns'  # test 3


domains_found = get_domain_names(URL)
for domain_name in domains_found:
    print(domain_name)


#####
# get correct output for test 3
correct_list = []
with open('test_3_output.txt', encoding='utf-8', newline='') as f_check:
    for line in f_check.read().splitlines():
        correct_list.append(line)

# check for missing links
for line in correct_list:
    if line not in domains_found:
        print(f'missing: {line}')
