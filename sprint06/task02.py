import json
import logging
import os.path


logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def parse_user(output_file, *input_files):
    result = []
    names = []
    for elem in input_files:
        if os.path.isfile(elem):
            with open(elem, "r") as f:
                content = json.load(f)
                for i in content:
                    if i.get("name") and i["name"] not in names:
                        names.append(i["name"])
                        result.append(i)
        else:
            logging.error(f"File {elem} doesn't exist")


    with open(output_file, "w+") as file:
        json.dump(result, file, indent=4)
