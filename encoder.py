import sys

if __name__ == "__main__":

    of   = open("final.html", "w+")
    html = open(sys.argv[1]).readlines()

    stylin = 0
    line = -1
    while 1:
        line += 1
        of.write(html[line])
        if "<pre>" in html[line]:
            break
    
    while 1:
        line += 1
        if "</pre>" in html[line]:
            break

        if "</style>" in html[line]:
            stylin = 0;

        if stylin:
            r = html[line]
            if "{" in html[line]:
                r = '<bl>'
                r = r + html[line].replace("{", "{</bl>")
                of.write(r)
            elif "}" in html[line]:
                r = html[line].replace("}", "<bl>}</bl>")
                of.write(r)
            else:
                of.write("<css>" + r + "</css>")
            continue

        if "<style>" in html[line]:
            stylin = 1;
        
        r = html[line].replace("<", "<y*^+&lt")
        r = r.replace(">","&gt</y>")
        r = r.replace("*^+", ">")
        of.write(r)

    while line < len(html):
        of.write(html[line])
        line += 1


        
