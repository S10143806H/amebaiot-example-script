import docutils.core
import os
import sys
from bs4 import BeautifulSoup

# define common path
root_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0])))

# align RST to standard format
def formatRST():
    convFlag = False
    # Convert keywords to standard
    with open("2.rst", "r+", encoding="utf-8") as input, open("2.rst", "r+", encoding="utf-8") as output:
        for num, line in enumerate(input,1):
            if line.startswith("Introduction") != 0  and convFlag is False:
                print("CASE 0") # found standard format
                convFlag = True
            elif line.startswith("**Introduction**") != 0 and convFlag is False:
                print("CASE 1") # wrong format found
                line = "Introduction\n-------------------\n\n"
                # convFlag = True
            elif line.startswith("**Procedure**") != 0 and convFlag is False:
                print("CASE 2")
                line = "Procedure\n-------------------\n\n"
                convFlag = True
            elif line.startswith("**Example**") !=0 and line.startswith("**Introduction**") == 0 :
                print("CASE 3")
                insert_pos = num + 2
            output.write(line)
        input.close()
        output.close()
    # Add keyword to RST
    with open("2.rst", "r+", encoding="utf-8") as file:
        for x in range(insert_pos):
            file.readline()
        if convFlag is False:
            print("CASE 3 CONT")
            pos = file.tell()
            file_remainder = file.read()
            file.seek(pos)
            file.write("Introduction\n-------------------\n\n")
            file.write(file_remainder)
            convFlag = True
    file.close()

# convert from rst to html and remove unnecessary portion
def convRST2HTML():
    docutils.core.publish_file(
        source_path="2.rst",
        destination_path="raw.html",
        writer_name="html")
    # remove unwanted sections
    for file in os.listdir(root_path):
        if file.endswith(".html"):
            print("[INFO] Currently processing '%s'..." %
                  (os.path.join(root_path, file)))
            soup = BeautifulSoup(
                open((os.path.join(root_path, file)), encoding="utf-8"), "html.parser")
            model_content = soup.find_all(
                "div", {"class": "document"}, limit=1)  # filter content area
            model_content = BeautifulSoup(
                str(model_content), 'html.parser').prettify()
            with open((os.path.join(root_path, file)), "w", encoding='utf-8') as file:
                write_content = ''.join(str(model_content)[1:-2])
                file.write(write_content)
            file.close()
    print("[INFO] Output file is store in raw.html")

# split raw html to introduction, procedure section
def splitRawHTML():
    for file in os.listdir(root_path):
        if file.endswith(".html"):
            print("[M] Currently processing '%s'..." %
                  (os.path.join(root_path, file)))
            soup = BeautifulSoup(
                open((os.path.join(root_path, file)), encoding="utf-8"), "html.parser")
            introduction_content = soup.find_all(
                "div", {"id": "introduction"}, limit=1)  # filter content area
            introduction_content = BeautifulSoup(
                str(introduction_content), 'html.parser').prettify()
            procedure_content = soup.find_all(
                "div", {"id": "procedure"}, limit=1)  # filter content area
            procedure_content = BeautifulSoup(
                str(procedure_content), 'html.parser').prettify()
            # output introduction section
            file1 = "intro.html"
            with open((os.path.join(root_path, file1)), "w", encoding='utf-8') as file1:
                # remove start and end unnecessary part
                write_content = ''.join(str(introduction_content)[1:-2])
                file1.write(write_content)
            file1.close()
            # output procedure section
            file2 = "procedure.html"
            with open((os.path.join(root_path, file2)), "w", encoding='utf-8') as file2:
                # remove start and end unnecessary part
                write_content = ''.join(str(procedure_content)[1:-2])
                file2.write(write_content)
            file2.close()

# filter content-only in introduction, procedure section
def processSplitHTML():
    for file in os.listdir(root_path):
        if file.endswith("intro.html"):
            soup = BeautifulSoup(
                open((os.path.join(root_path, file)), encoding="utf-8"), "html.parser")
            introduction_content = soup.find_all('p')  # filter content area
            introduction_content = BeautifulSoup(
                str(introduction_content), 'html.parser').prettify()
            with open("intro.txt", "w+", encoding="utf-8") as file:
                # remove start and end unnecessary part
                write_content = ''.join(str(introduction_content)[1:-2])
                write_content = write_content.replace(
                    "<p>", "  ")  # remove <p>
                write_content = write_content.replace(
                    "</p>", "  ")  # remove </p>
                file.write(write_content)
            file.close()
    with open("intro.txt", "r", encoding="utf-8") as input, open('intro.txt', 'r+') as output:
        for line in input:
            if line.startswith(",") != 0:
                line = ''
                continue
            if line.strip():
                output.write(line)
        output.truncate()

    for file in os.listdir(root_path):
        if file.endswith("procedure.html"):
            soup = BeautifulSoup(open((os.path.join(root_path, file)), encoding="utf-8"), "html.parser").find_all(['p', 'blockquote'])
            # soup = soup + BeautifulSoup(open((os.path.join(root_path, file)), encoding="utf-8"), "html.parser").find_all('blockquote')
            procedure_content = BeautifulSoup(
                str(soup), 'html.parser').prettify()
            # print(procedure_content)
            with open("proce.html", "w+", encoding="utf-8") as file:
                write_content = ''.join(str(procedure_content)[1:-2])
                write_content = write_content.replace("<p>", "  ")   # remove <p>
                write_content = write_content.replace("</p>", "  ")  # remove </p>
                write_content = write_content.replace("<tt class=\"docutils literal\">", "  ") 
                write_content = write_content.replace("</tt>", "  ") 
                file.write(write_content)
            file.close()
    
    
    for file in os.listdir(root_path):
        if file.endswith("proce.html"):
            soup = BeautifulSoup(
                open((os.path.join(root_path, file)), encoding="utf-8"), "html.parser")
            img_hearders = soup.find_all("img")
            link_headers = soup.find_all("a")
            # span_headers = soup.find_all("span", limit=1)
            span_headers = soup.select("span")
            strong_headers = soup.find_all("strong")

            count = 0
            for img_header in img_hearders:
                count = count + 1
                img_header['class'] = "size-full wp-image-3851 aligncenter"
                del img_header['alt']
                img_header['src'] = "/wp-content/uploads/YYYY/MM/EXAMPLE/" + str(count) + ".png"
                del img_header['style']
                img_header['width'] = "800"
                img_header['height'] = "500"
                # print(header)
            for link_header in link_headers:
                del link_header ["class"]
            for span_header in span_headers:
                span_header.extract()
            last_header = "Code Reference"
            for last_header in strong_headers:pass
            if last_header:
                print(last_header)
                last_header["style"] = "color: #e67e22; background-color: white; font-size: 28px"
                last_header.name = "span"
            else:
                break
            soup = BeautifulSoup(
                str(soup), 'html.parser').prettify()
            # print(procedure_content)
            # print(soup)
            with open("proce.html", "w+", encoding="utf-8") as file:
                write_content = ''.join(str(soup))
                file.write(write_content)
            file.close()
    
    with open("proce.html", "r", encoding="utf-8") as input, open('proce.html', 'r+', encoding="utf-8") as output:
        for line in input:
            if line.startswith(",") != 0 or line.startswith(" ,") != 0 or line.startswith("<p style=\"color:#E67E22; font-size:24px\">") != 0 or line.startswith("</p>") != 0:
                line = ''
                continue
            if line.startswith("<p style=\"color:#E67E22; font-size:24px\">") != 0:
                print(line)
            if line.strip():
                output.write(line)
        output.truncate()
    
# append to template
def appendSplit2Template():
    file1="intro.txt"
    file2="proce.html"
    temp = root_path + "\\template\\mindy.html"
    
    with open(temp, "r+", encoding="utf-8") as file:
        for x in range(12): # change to line number
            print(file.readline())
        pos = file.tell()
        print(pos)
        file_remainder = file.read()
        file.seek(pos)
        with open(file1, "r", encoding="utf-8") as f1:
            for line in f1:
                print(line)
                file.write(line)
        file.write(file_remainder)
        pos = file.tell()
        print(pos)
        f1.close()
        file.close()
    
    with open(temp, "r+", encoding="utf-8") as file:
        for x in range(pos):
            print(file.readline())
        pos = file.tell()
        print(pos)
        file_remainder = file.read()
        file.seek(pos)
        with open(file2, "r", encoding="utf-8") as f3:
            for line in f3:
                print(line)
                file.write(line)
        file.write(file_remainder)
    f3.close()
    file.close()
       
#########################################
# Main Function
#########################################
if __name__ == '__main__':
    print("===== [MAIN Function] =====")

    formatRST()
    convRST2HTML()
    splitRawHTML()
    processSplitHTML()
    appendSplit2Template()