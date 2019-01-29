#!/usr/bin/python3.5
import sys
import re
import urllib.request


def parseWeb():
    link = "https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa" + \
            "855ea#file-movies-csv"
    # url link to website

    with urllib.request.urlopen(link) as f:  # grabbing site info
        htmlList = []  # set list
        for i in f.readlines():   # loop through site grabing the html '''
            htmlList.append(i)
            scrape = str(htmlList)  # setting list to string
        pattern = str(re.compile(r'\<\/td\>(.*?)\<\/tbody\>',
                                 re.I).findall(scrape))
        # look for the  tags <td> through </tbody>

        removeHtmlTags = re.compile('<.*?>')  # remove other html tags
        tagFree = re.sub(removeHtmlTags, '', pattern)

        removeReturnLines = re.compile(r'^\[\'\\\\n\\\'\,\sb\\\'\s+')
        # removes ' \ ans spaces in the html
        returnFree = re.sub(removeReturnLines, '', tagFree)

        removeSlash1 = re.compile(r'\\\\n\\\'\,\sb\\\'')
        reSlash1 = re.sub(removeSlash1, '\n', returnFree)
        # removes additional white space and places return line after the
        # section ends

        endChar = re.compile(r'\'\,\s\"\\\\n\'\,\sb\'')
        end = re.sub(endChar, '', reSlash1)  # removes specific slashes

        end2char = re.compile(r'\\\\n\'\,\sb\'\s+\"\]')
        endchar2 = re.sub(end2char, '', end)  # cleans last lines
        sys.stdout = open('file', 'w')  # writes output to a file called file
        print(str(endchar2))


parseWeb()
