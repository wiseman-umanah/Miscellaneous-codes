import xml.dom.minidom

def main():
    # use the parse() funtion to load and parse an XML file
    doc = xml.dom.minidom.parse("samplexml.xml")

    # print out the document mode and the name of the first child tag
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    
    # get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("Skill")
    print(skills.length,"skills are listed")
    for skill in skills:
        print(skills.getAttribute("name")) 

    # create a new XML tag and add it into the document
    skills = doc.getElementsByTagName("Skill")
    print(skills.length,"skills are listed")
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name","baller")
    doc.firstChild.appendChild(newSkill)


main()
