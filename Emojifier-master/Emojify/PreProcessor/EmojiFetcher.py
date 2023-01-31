import re
import os
import base64
import json
import requests
work_location = "/path/to/your/working/directory"


def process_base_64_file(file_name, base64_image):
    with open(f"{file_name}", 'wb') as f:
        f.write(base64.b64decode(base64_image))
        
def company_names():
    return ["Brow", "Chart", "Appl", "Goog", "Twtr", "One", "FB","FBM","Sams","Wind","GMail","SB","DCM","KDDI"]

def get_company_name(i):
    return company_names()[i - 2]

def create_work_directory(work_location):
    os.system(f"mkdir {work_location}")
    for company in company_names():
        os.system(f"mkdir {work_location}/{company}")

def fetch_from_the_unicode_website(work_location):
    response = requests.get('https://unicode.org/Public/emoji/13.0/emoji-test.txt')
    html_content = response.text
    
    table_rows = re.findall(r'<tr>(.*?)</tr>', html_content, re.DOTALL)
    print(f"Number of Rows {len(table_rows)}")
    meta_data_dictionary = {}
    for row in table_rows[12:]:
        row_cols = re.findall(r'<td>(.*?)</td>', row, re.DOTALL)
        if len(row_cols) == 0:
            continue
        
        unicode_name = re.search(r'<a name="(.*?)">', row_cols[1]).group(1)
        
        meta_data_dictionary[unicode_name] = {
            'actual_name': re.search(r'>(.*?)<', row_cols[16]).group(1),
            'year_introduced': re.search(r'>(.*?)<', row_cols[17]).group(1)[:4],
            'key_words': [x.group(1) for x in re.finditer(r'>(.*?)<', row_cols[18])]
        }

        for i in range(2, len(row_cols)):
            image_search = re.search(r'<img src="data:image/png;base64,(.*?)"', row_cols[i])
            if not image_search:
                continue
            base64_value = image_search.group(1)
            process_base_64_file(f"{work_location}/{get_company_name(i)}/{unicode_name}.png", base64_value)

    with open(f"{work_location}/MetaDataInfo.json", "w") as f_meta:
        f_meta.write(json.dumps(meta_data_dictionary, sort_keys=True, indent=4))

# Convert all Images to RGB .jpg.
for company in company_names():
    os.system(f"mogrify -flatten -format jpg {work_location}/{company}/.png -quality 99")
    os.system(f"rm {work_location}/{company}/.png")
    os.system(f"mogrify -colorspace sRGB -type truecolor {work_location}/{company}/*.jpg")

def fetch_files(work_location):
    create_work_directory(work_location)
    fetch_from_the_unicode_website(work_location)

if __name__ == "__main__":
    print ("Fetching")
    fetch_files("/tmp/Emojis");
