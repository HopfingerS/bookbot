def count_words(content):
    word_list = content.split()
    return len(word_list)

def count_characters(content):
    content = content.lower()
    word_dict = {}
    dict_list = []

    #content = content[:50]

    for c in content:
        new_dict = {}
        new_dict["char"] = c
        new_dict["num"] = 1
                
        if not any(d.get("char") == c for d in dict_list):
            dict_list.append(new_dict)
        else:
            index = -1
            for l in dict_list:
                if l["char"] == new_dict["char"]:
                    index = dict_list.index(l)
            

            dict_list[index]["num"] += 1         
    return dict_list

def sort_on(items):
    return items["num"]