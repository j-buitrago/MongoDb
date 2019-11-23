import json
from lxml import etree

def etree2json(element, labels):

    publication = {}
    authors = []
    
    print(etree.tostring(element), "\n")
    print(element.tag, "\n")

    for subelement in element:
        if subelement.tag in labels:
            print(subelement.tag, subelement.text)
            if subelement.tag == "year":
                if subelement.text != None:
                    publication[subelement.tag] = int(subelement.text)
                else:
                    publication[subelement.tag] = "None"
            elif subelement.tag == "author":
                authors.append(subelement.text)
            else:
                publication[subelement.tag] = subelement.text

    publication['Authors'] = authors
    publication['type'] = element.tag
    print("\n",publication)

    return publication


def main():

    imputFile= 'dblp.xml'
    outputFile = 'dblp_def.json'
    
    #open for writing, truncating the file first
    writer = open(outputFile, 'w') 

    #we need to definy the types of publications 
    public_types = ["article","inproceedings","incollection"]
    labels = ["title", "author", "journal", "year"]

    cont = 0

    #The enconding is ISO-8859-1 (latin-1) as "Some Lessons Learned" article described
    for event, element in etree.iterparse(imputFile, dtd_validation=True, load_dtd=True,
    events=('start', 'end'), encoding='ISO-8859-1',tag=public_types, html=True):
        
        if event == 'start':
            publication = etree2json(element, labels)
            json.dump(publication, writer)
            writer.write('\n')

        elif event == 'end':
            element.clear()
            cont+=1
            #if cont == 15:
            #    break
            
    writer.close()



if __name__ == '__main__':
    main()