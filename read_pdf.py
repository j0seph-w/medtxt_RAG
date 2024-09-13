
import json
from unstructured.partition.pdf import partition_pdf

elements = partition_pdf("Fundamental Techniques of Plastic Surgery.pdf")

all_txt = []

for element in elements:
    all_txt.append(str(element.text))

json_string = json.dumps(all_txt, indent=3)
save_file = open("all_txt.txt", "w")  
json.dump(all_txt, save_file, indent=3)  
save_file.close() 