#!/usr/bin/python
# This is a simple python script to get the api informations from
#    https://github.com/Binaryify/NeteaseCloudMusicApi
import os, re

def getCurrentPathFiles() :
    t_files = os.listdir()
    files = [];
    for file in t_files :
        if not os.path.isdir(file) and os.path.splitext(file)[1] == '.js' :
            files.append(file)
    return files

def details(path) :
    response = ''
    with open(path, 'r') as file :
        first_line = file.readline()
        content = file.read()
        intro = re.sub('\/\/', '###', first_line)
        url = re.search('`https?(.|\n)+`', content).group()
        data = re.search('const data = (.|\n)+return', content)
        if data :
            data = re.sub('(const data \= |\n.*return)', '', data.group())
        else :
            data = '{}'
        response += f'''
---

{intro}

{url}

POST :
```javascript
{data}
```
'''
    return response

if __name__ == '__main__' :
    with open('doc.md', 'w+') as doc_file :
        for file in getCurrentPathFiles() :
            doc_file.write(details(file))
