import os
import sys
import shutil
import docutils.core
from bs4 import BeautifulSoup

# define common path
root_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0])))
keyword = 'Class'


# Align RST to standard format
# add introduction and procedure section if it does not contained

def formatRST():
    convFlag = False
    insert_pos = 0
    replace_list = ['.. method::']
    delete_list = ['.. code:: cpp', '``']
    delete_list_EG = ['``']
    
    # Convert keywords in .rst to standard format
    for filename in os.listdir(root_path):
        if filename.endswith(".rst"):
            f = os.path.join(root_path, filename)
            if os.path.isfile(f):
                if keyword in f:
                    # API Documents
                    print("[INFO] %s" % f)
                    with open(f, "r+", encoding="utf-8") as input, open(f, "r+", encoding="utf-8") as output:
                        # delete rst keyword cannot be recognized
                        for line in input:
                            for word in replace_list:
                                line = line.replace(word, '-')
                            for word in delete_list:
                                line = line.replace(word, '')
                            output.write(line)
                else:                                                           
				# Example Guides                    
                    with open(f, "r+", encoding="utf-8") as input, open(f, "r+", encoding="utf-8") as output:
                        for num, line in enumerate(input, 1):
                            if line.startswith("Introduction") != 0 and convFlag is False:
                                # print("[DEBUG] CASE 0") # found standard format
                                convFlag = True
                            elif line.startswith("**Introduction**") != 0 and convFlag is False:
                                # print("[DEBUG] CASE 1") # wrong format found
                                line = "Introduction\n-------------------\n\n"
                            elif line.startswith("**Procedure**") != 0 and convFlag is False:
                                # print("[DEBUG] CASE 2") # wrong format found
                                line = "Procedure\n-------------------\n\n"
                                convFlag = True
                            elif line.startswith("**Example**") != 0 and line.startswith("**Introduction**") == 0:
                                # print("[DEBUG] CASE 3") # mising keyword
                                insert_pos = num + 2
                            output.write(line)
                        input.close()
                        output.close()
                        # CASE3: Adding keyword to RST
                        with open(f, "r+", encoding="utf-8") as file:
                            for x in range(insert_pos):
                                file.readline()
                            if convFlag is False:
                                # print("[DEBUG] CASE 3 CONT")
                                pos = file.tell()
                                file_remainder = file.read()
                                file.seek(pos)
                                file.write("Introduction\n-------------------\n\n")
                                file.write(file_remainder)
                                convFlag = True
                        file.close()
            
    print("[%s][INFO] ------------ Done -----------" % ("formatRST"))

# convert from rst to html and remove unnecessary portion
def convRST2HTML():
    for filename in os.listdir(root_path):
        if filename.endswith(".rst"):
            f = os.path.join(root_path, filename)
            if os.path.isfile(f):
                # print(f)
                filename, file_extension = os.path.splitext(f)
                print("[INFO] Currently converting '%s.html'..." % filename)
                docutils.core.publish_file(
                    source_path=f,
                    destination_path=filename + ".html",
                    writer_name="html")
                soup = BeautifulSoup(
                    open(filename + ".html", encoding="utf-8"), "html.parser")
                # filter model content area only
                model_content = soup.find_all(
                    "div", {"class": "document"}, limit=1)
                model_content = BeautifulSoup(
                    str(model_content), 'html.parser').prettify()
                # write filtered content to the same file
                with open(filename + ".html", "w", encoding='utf-8') as file:
                    write_content = ''.join(str(model_content)[1:-2])
                    file.write(write_content)
                    print(
                        "[INFO] Converted output file is stored in '%s.html'" % filename)
            file.close()
    print("[%s][INFO] ---------- Done ----------" % ("convRST2HTML"))

# split raw html to introduction & procedure section
def splitHTMLContent():
    for filename in os.listdir(root_path):
        if filename.endswith(".rst"):
            f = os.path.join(root_path, filename)
            if os.path.isfile(f):
                filename, file_extension = os.path.splitext(f)
                # check whether the file name contains Class
                if keyword in filename:
                    # API Documents
                    print("[INFO] [API] Currently splitting '%s.html'..." % filename)
                    # soup = BeautifulSoup(open(filename + ".html", encoding="utf-8"), "html.parser")
                    # currently processing as a whole file
                else:
                    # Example Guides
                    print("[INFO] [EXP] Currently splitting '%s.html'..." % filename)
                    soup = BeautifulSoup(
                        open(filename + ".html", encoding="utf-8"), "html.parser")
                    introduction_content = BeautifulSoup(str(soup.find_all(
                        "div", {"id": "introduction"}, limit=1)), 'html.parser').prettify()
                    procedure_content = BeautifulSoup(str(soup.find_all(
                        "div", {"id": "procedure"}, limit=1)), 'html.parser').prettify()
                    materials_content = BeautifulSoup(str(soup.find_all(
                        "ul", {"class": "simple"}, limit=1)), 'html.parser').prettify()
                    
                    # output MATERIALS section
                    with open(filename + "_materials.html", "w", encoding='utf-8') as file0:
                        # remove start and end unnecessary part
                        write_content = ''.join(str(materials_content)[1:-2])
                        soup = BeautifulSoup(materials_content, 'html.parser')
                        write_content = write_content.replace(
                            "</ul>", "  ")  # remove </ul>

                        # add in hyper link
                        write_content = write_content.replace(
                            "AMB21",  "<a href=" "'/amebad/#rtk_amb21'" ">AMB21</a>")
                        write_content = write_content.replace(
                            "AMB22",  "<a href=" "'/amebad/#rtk_amb22'" ">AMB22</a>")
                        write_content = write_content.replace(
                            "AMB23",  "<a href=" "'/amebad/#rtk_amb23'" ">AMB23</a>")
                        write_content = write_content.replace(
                            "BW16",  "<a href=" "'/amebad/#partner_bw16'" ">BW16</a>")
                        file0.write(write_content[20:])
                    file0.close()
                    
                    # output INTRODUCTION section
                    with open(filename + "_intro.html", "w", encoding='utf-8') as file1:
                        # remove start and end unnecessary part
                        write_content = ''.join(
                            str(introduction_content)[1:-2])
                        file1.write(write_content)
                    file1.close()

                    # output PROCEDURE section
                    with open(filename + "_proce.html", "w", encoding='utf-8') as file2:
                        # remove start and end unnecessary part
                        write_content = ''.join(str(procedure_content)[1:-2])
                        file2.write(write_content)
                    file2.close()
    print("[%s][INFO] -------- Done --------" % ("splitHTMLContent"))


# filter content-only in introduction & procedure section
def processSplitHTML():
    for filename in os.listdir(root_path):
        if keyword in filename:
            # API Documents
            if filename.endswith(".html"):
                soup = BeautifulSoup(
                    open((os.path.join(root_path, filename)), encoding="utf-8"), "html.parser")
                # introduction_content = soup.find_all('p')  # filter content area
                introduction_content = BeautifulSoup(
                    str(soup), 'html.parser').prettify()
                with open((os.path.join(root_path, filename)), "w+", encoding="utf-8") as file:
                    # remove start and end unnecessary part
                    write_content = ''.join(str(introduction_content)[38:-8])
                    # remove <blockquote>
                    write_content = write_content.replace("<blockquote>", "")
                    write_content = write_content.replace("</blockquote>", "")
                    # remove <hr>
                    write_content = write_content.replace(
                        "<hr class=\"docutils\"/>", "  ")
                    # remove ,
                    write_content = write_content.replace(",", "")
                    # remove <p>
                    write_content = write_content.replace("<p>", "")
                    write_content = write_content.replace("</p>", "")
                    # replace <ul>
                    write_content = write_content.replace(
                        "<ul class=\"simple\">", "<h3 style=\"color: #e67e22; font-size: 28px;\">")
                    write_content = write_content.replace("</ul>", "</h3>")
                    file.write(write_content)
                file.close()

            if filename.endswith(".html"):
                print(filename)
                soup = BeautifulSoup(
                    open((os.path.join(root_path, filename)), encoding="utf-8"), "html.parser")
                strong_headers = soup.find_all("strong")
                h1_headers = soup.find_all('h1')
                li_headers = soup.find_all('li')
                table_headers = soup.find_all("table")
                tbody_headers = soup.find_all("tbody")
                soup.colgroup.decompose()
                count = 0

                for strong_header in strong_headers:
                    strong_header['style'] = "font-size: 22px; color: #000000;"

                for h1_header in h1_headers:
                    del h1_header["class"]
                    h1_header['style'] = "color: #0070c0; font-size: 28px;"
                    h1_header.name = 'strong'
                    
                for li_header in li_headers:
                    APIname = li_header.string.strip().replace("::","_")
                    li_header.name = 'strong'
                    new_child_tag = soup.new_tag("a", id=APIname, class_="anchor")
                    li_header.append(new_child_tag)

                for table_header in table_headers:
                    del table_header["class"]
                    table_header['border'] = "0"
                
                for tbody_header in tbody_headers:
                    del tbody_header["valign"]

                soup = BeautifulSoup(str(soup), 'html.parser').prettify()
                with open((os.path.join(root_path, filename)), "w+", encoding="utf-8") as file:
                    write_content = ''.join(str(soup))
                    file.write(write_content)
                file.close()
        else:
            # Example Guides
            # processing _intro.html
            if filename.endswith("intro.html"):
                soup = BeautifulSoup(
                    open((os.path.join(root_path, filename)), encoding="utf-8"), "html.parser")
                introduction_content = soup.find_all(
                    'p')  # filter content area
                introduction_content = BeautifulSoup(
                    str(introduction_content), 'html.parser').prettify()
                with open((os.path.join(root_path, filename)), "w+", encoding="utf-8") as file:
                    # remove start and end unnecessary part
                    write_content = ''.join(str(introduction_content)[1:-2])
                    # remove <p>
                    write_content = write_content.replace("<p>", "  ")
                    write_content = write_content.replace("</p>", "  ")
                    file.write(write_content)
                file.close()
                with open((os.path.join(root_path, filename)), "r", encoding="utf-8") as input, open((os.path.join(root_path, filename)), 'r+') as output:
                    for line in input:
                        if line.startswith(",") != 0:
                            line = ''
                            continue
                        if line.strip():
                            output.write(line)
                    output.truncate()
                print("[%s] %s created successfully" %
                      ("processSplitHTML", filename))

            # processing _proce.html
            

            if filename.endswith("proce.html"):
                # print(filename)
                soup = BeautifulSoup(
                    open((os.path.join(root_path, filename)), encoding="utf-8"), "html.parser")
                img_hearders = soup.find_all("img")
                link_headers = soup.find_all("a")
                span_headers = soup.find_all("span")
                strong_headers = soup.find_all("strong")

                count = 0

                for img_header in img_hearders:
                    count = count + 1
                    img_header['class'] = "size-full wp-image-3851 aligncenter"
                    del img_header['alt']
                    img_header['src'] = "/wp-content/uploads/YYYY/MM/EXAMPLE/" + \
                        str(count) + ".png"
                    del img_header['style']
                    img_header['width'] = "800"
                    img_header['height'] = "500"

                for link_header in link_headers:
                    del link_header["class"]

                for span_header in span_headers:
                    print(span_header)
                    span_header.extract()
                last_header = "Code Reference"

                for last_header in strong_headers:
                    pass
                if last_header:
                    last_header["style"] = "color: #e67e22; background-color: white; font-size: 28px"
                    last_header.name = "span"
                else:
                    break

                soup = BeautifulSoup(str(soup), 'html.parser').prettify()
                with open((os.path.join(root_path, filename)), "w+", encoding="utf-8") as file:
                    write_content = ''.join(str(soup))
                    file.write(write_content)
                file.close()
                
                if filename.endswith("proce.html"):
                # print(filename)
                    soup = BeautifulSoup(open((os.path.join(root_path, filename)), encoding="utf-8"),
                                        "html.parser").find_all(['p', 'blockquote', 'table'])
                    # print(soup)
                
                    procedure_content = BeautifulSoup(
                        str(soup), 'html.parser').prettify()
                
                    with open((os.path.join(root_path, filename)), "w+", encoding="utf-8") as file:
                        write_content = ''.join(str(procedure_content)[1:-2])
                        # remove <p>
                        write_content = write_content.replace("<p>", "  ")
                        write_content = write_content.replace("</p>", "  ")
                        
                        # remove <tt>
                        write_content = write_content.replace(
                            "<tt class=\"docutils literal\">", "  ")
                        write_content = write_content.replace("</tt>", "  ")
                        write_content = write_content.replace("<blockquote>", "  ")
                        write_content = write_content.replace("</blockquote>", "  ")
                        write_content = write_content.replace('<p class="first admonition-title">', " ")
                    
                        file.write(write_content)
                    file.close()

                with open((os.path.join(root_path, filename)), "r", encoding="utf-8") as input, open((os.path.join(root_path, filename)), 'r+', encoding="utf-8") as output:
                    for line in input:
                        if line.startswith(",") != 0 or line.startswith(" ,") != 0 or line.startswith("<p style=\"color:#E67E22; font-size:24px\">") != 0 or line.startswith("</p>") != 0 or line.startswith("<blockquote>") != 0 or line.startswith("</blockquote>") != 0:
                            line = ''
                            continue
                        if line.strip():
                            output.write(line)
                    output.truncate()
                print("[%s] %s created successfully" %
                      ("processSplitHTML", filename))
    # print("[%s][INFO] -------- Done -------- " % ("processSplitHTML"))

# append to template
def appendSplit2Template():
    temp = root_path + "\\template_self\\mindy.html"
    output_dir = root_path + "\\output\\"

    # check if output folder exist
    output_folder = os.path.exists(output_dir)
    if output_folder == True:
        print(output_folder)
        print("%s has already been created" % output_dir)
    else:
        os.mkdir(output_dir)
        print("%s not existed, created a new one" % output_dir)

    for file in os.listdir(root_path):
        if file.endswith("intro.html"):
            if os.path.isfile(file):
                filename = file.split('_')[0]
                print("[%s][INFO] Currently processing '%s_intro.html'..." %
                      ("appendSplit2Template", filename))
                # create a new folder to store output files
                if os.path.isdir(output_dir):
                    shutil.copy(temp, output_dir + filename + ".html")
                    if os.path.isfile(output_dir + filename + ".html"):
                        with open(output_dir + filename + ".html", "r+", encoding="utf-8") as file_output:
                            for x in range(5):
                                print(file_output.readline())
                            pos = file_output.tell()
                            print(pos)
                            file_remainder = file_output.read()
                            print(file_remainder)
                            file_output.seek(pos)

                            with open(file, "r", encoding="utf-8") as f1:
                                print(file)
                                for line in f1:
                                    print(line)
                                    file_output.write(line)
                            file_output.write(file_remainder)
                            pos = file_output.tell()
                            print(pos)
                        f1.close()
                        file_output.close()
    print("===========================================")
    print("[%s][INFO] added intro.html to the template" %
          ("appendSplit2Template"))

    for file in os.listdir(root_path):
        if file.endswith("proce.html"):
            if os.path.isfile(file):
                filename = file.split('_')[0]
                print("[INFO] Currently processing '%s_proce.html'..." % filename)
                # continue writing to the output file
                if os.path.isfile(output_dir + filename + ".html"):
                    with open(output_dir + filename + ".html", "r+", encoding="utf-8") as file_output:
                        for x in range(pos):
                            print(file_output.readline())
                        pos = file_output.tell()
                        print(pos)
                        file_remainder = file_output.read()
                        print(file_remainder)
                        file_output.seek(pos)

                        with open(file, "r", encoding="utf-8") as f1:
                            print(file)
                            for line in f1:
                                print(line)
                                file_output.write(line)
                        file_output.write(file_remainder)
                        pos = file_output.tell()
                        # print(pos)
                    f1.close()
                    file_output.close()
                # else:
                    # os.mkdir(output_dir)
    print("===========================================")
    print("[%s][INFO] added proce.html to the template" %
          ("appendSplit2Template"))

    for file in os.listdir(root_path):
        if file.endswith("materials.html"):
            if os.path.isfile(file):
                filename = file.split('_')[0]
                print("[INFO] Currently processing '%s_materials.html'..." % filename)
                
                # continue writing to the output file
                if os.path.isfile(output_dir + filename + ".html"):
                    with open(output_dir + filename + ".html", "r+", encoding="utf-8") as file_output:
                     
                        for x in range(2): 
                            print(file_output.readline())
                        pos = file_output.tell()
                        print(pos)
                        file_remainder = file_output.read()
                        print(file_remainder)
                        file_output.seek(pos)

                        with open(file, "r", encoding="utf-8") as f1:
                            for line in f1:
                                print(line)
                                file_output.write(line)
                        file_output.write(file_remainder)
                        pos = file_output.tell()
                        print(pos)
                    f1.close()
                    file_output.close()
                    
    print("===========================================")
    print("[%s][INFO] added materials.html to the template" % ("appendSplit2Template"))


# remove processing middle files
def removeFiles():
    output_dir = root_path + "\\output\\"

    for filename in os.listdir(root_path):
        if filename.endswith(".rst"):
            f = os.path.join(root_path, filename)
            if os.path.isfile(f):
                filename, file_extension = os.path.splitext(f)
                if os.path.isfile(output_dir + filename.split('\\')[-1] + ".html"):
                    print("[INFO] Found output file '%s.html'..." %
                          (output_dir + filename.split('\\')[-1]))
                    for file in os.listdir(root_path):
                        if file.endswith(".html"):
                            os.remove(file)
            print("[INFO] Removed .html files")


#########################################
# Main Function
#########################################
if __name__ == '__main__':
    print("===== [MAIN Function] =====")

    formatRST()
    convRST2HTML()
    splitHTMLContent()
    processSplitHTML()
    appendSplit2Template()
    removeFiles()