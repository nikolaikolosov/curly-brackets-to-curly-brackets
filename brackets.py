import re

file_name = "file-with-metrics.txt"

with open(f"./temp/{file_name}") as file:
    content = file.read()
    pattern = r'{{(.*?)}}'
    replacement = r'{{ "{{" }}\1{{ "}}" }}'
    formatted_content = re.sub(pattern, replacement, content)
    output_file = open(f"./temp/{file_name}-formatted", "w")
    output_file.write(formatted_content)
    output_file.close()
