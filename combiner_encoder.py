import sys

if __name__ == "__main__":

    _of     = open("formatted.html", "w+")
    _if     = open("inner.html")
    _tp     = open("template.html")
    _nt     = open("notes.txt")
    _st     = open("inner_style.css")

    template    = _tp.readlines()
    inner       = _if.readlines()
    notes       = _nt.readlines()
    style       = _st.readlines()

    stylin = 0
    i = 0
    while "WRITE_HERE" not in template[i]:
        _of.write(template[i])
        i += 1

    # notes
    _of.write("<pre class=notes>\n")
    for line in notes:
        _of.write(line)

    _of.write("</pre>\n")

    # inner html
    _of.write("<pre class=html>\n")
    for line in inner:  
        r = line.replace("<", "<y*^+&lt")
        r = r.replace(">","&gt</y>")
        r = r.replace("*^+", ">")
        if "<y>&lt!--" in r:
            r = r.replace("<y>&lt!--", "<html_comm>&lt!--")
            r = r.replace("--&gt</y>", "--&gt</html_comm>")
        _of.write(r)
    _of.write("</pre>\n")

    # inner css
    _of.write("<pre class=css>\n")
    for line in style:
        r = line
        if "{" in line:
            r = '<bl>'
            r = r + line.replace("{", "{</bl>")
        elif "}" in line:
            r = line.replace("}", "<bl>}</bl>")
        else:
            r = "<css>" + r[:-1] + "</css>\n"

        if "/*" in r:
            r = r.replace("/*", "<css_comm>/*")
            r = r.replace("*/", "*/</css_comm>")

        _of.write(r)
    _of.write("</pre>\n")


    i += 1
    while i < len(template):
        _of.write(template[i])
        i += 1

    _if.close()
    _of.close()
    _tp.close()
    _nt.close()
    _st.close()

