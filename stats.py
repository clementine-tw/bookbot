def get_num_words(text: str) -> int:
    return len(text.split())

def get_chars_dict(text: str) -> dict:
    chars_dict = {}
    for c in text:
        c_lower = c.lower()
        if c_lower in chars_dict:
            chars_dict[c_lower] += 1
        else:
            chars_dict[c_lower] = 1
    return chars_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict: dict) -> list:
    sorted_list = []
    for k, v in num_chars_dict.items():
        sorted_list.append({"char": k, "num": v})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list