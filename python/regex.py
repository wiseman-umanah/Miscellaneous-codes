import re

link = input()
link_list = link.split("/")

def find_id(link_list = []):
    for i in link_list:
        if i.startswith("watch"):
            m = re.search('(?<=v=)\w+', i)
            print(m.group(0))
            return 0
    query = link_list[len(link_list) - 1]
    print(query)
    return 0

find_id(link_list)
