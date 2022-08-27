import re

t = re.compile(r"(?<=<)(?:.*?)(?=>)")
attrib = re.compile(r"([\w-]+)(?:=[\"'](.*?)[\"'])?")

string = ""

# get input stream
for _ in range(int(input())):
    string += input()

# discard comments
string = re.sub(r"(?:<!--(.|\s)*?(?:-->))","",string)

# extract individual tag information
tags = t.findall(string)

# iterate over the extracted tag information
for tag in tags:
    # tag handling logic
    if tag[0] == "/":
        print("End   :",tag[1:])
    else:
        attribs = attrib.findall(tag)
        if tag[-1] == "/":
            print("Empty :",attribs[0][0])
        else:
            print("Start :",attribs[0][0])
            
        for i in range(1,len(attribs)):
            m = attribs[i][0]
            if attribs[i][1] == '': 
                n = 'None' 
            else: 
                n = attribs[i][1]
            print("-> {} > {}".format(m,n))
