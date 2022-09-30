import random
import re

def getResponse(comment):
    #we should probably turn everything into uppercase before we do this.
    #And all our responses should be capitalized

    #we'll first compile all the regexes. We should ignore case. We should standardize the case of the comment,
    #so that the regexes can match it
    hate = re.compile(r"(hates?|dislikes?|(doesn't like)|(don't like))\s+(.*)(\.|!|$)")
    excess = re.compile(r"(((([A-Z]\w+)\s)+)|(\b(\w+)))\s(is|was|(will be)|am|are)\s(too|so)\s(.*)(\.|!|$)")
    default = re.compile(r"([.!?]\s+)?([^.!?]*)(\.|!|$)$")
    thesis = re.compile(r"(\w+)\s(thinks?|expects?|calculates?|believes?)\s(.*)")
    reflex = re.compile(r"\b(I am|you are|we are|we|I)\b")
    support = re.compile(r"(((([A-Z]\w+)\s)+)|(\b(\w+)))\s(supports?|likes?|favours?)(.*)(\.|!|\Z)")
    bad = re.compile(r"(((([A-Z]\w+)\s)+)|(\b(\w+)))\s(has|had)\s(a\s)?(bad|poor)\s.*")
    good = re.compile(r"(((([A-Z]\w+)\s)+)|(\b(\w+)))\s(has|had)\s(a\s)?(good)\s.*")
    noMore = re.compile(r"(too much|excessive)\s(.*)(\.|!|\Z)")
    lack = re.compile(r"(isn't|not)(\shave)?\s(enough)\s(.*)(\.|!|\Z)")
    prescript = re.compile(r"(((([A-Z]\w+)\s)+)|(\b(\w+)))\sshouldn't\s.*(\.|!|\Z)")
    tension = re.compile(r"((is tension between)|tense).*")
    relations = re.compile(r"(have|has)\s(.*)\srelations with .*")
    query = re.compile(r"\?\Z")
    
    #now we need to do the matching/searching
    hateCapt = hate.search(comment)
    excessCapt = excess.search(comment)
    thesisCapt = thesis.search(comment)
    supportCapt = support.search(comment)
    badCapt = bad.search(comment)
    goodCapt = good.search(comment)
    noMoreCapt = noMore.search(comment)
    lackCapt = lack.search(comment)
    prescriptCapt = prescript.search(comment)
    tensionCapt = tension.search(comment)
    relatCapt = relations.search(comment)
    queryCapt = query.search(comment)

    reflexCapt = reflex.search(comment)
    defaultCapt = default.search(comment)
    #then we'll check the comment to see which one matches. use if-elses
    #we'll respond to the last match
    #we need a pronoun morpher. like to change he to him; they to them etc.
    pronounMorph = {
                    "he" : "him",
                    "she" : "her",
                    "they" : "them",
                    "I" : "you",
                    "we" : "y'all",
                    "I am" : "you are",
                    "we are" : "y'all are",
                    "you are" : "I am",
                    "He" : "him",
                    "She" : "her",
                    "They" : "them",
                    "We" : "y'all",
                    "I am" : "you are",
                    "We are" : "y'all are",
                    "You are" : "I am"
                    }
    
    pronounMorph2 = {
                    "I" : "you",
                    "we" : "y'all",
                    "We" : "y'all",
                    }
    response = 'Pardon?'
    #commentReflex = reflex.sub(auxVerbPrnn.get(reflexCapt(1)), comment)
    if hateCapt != None:
        response = "What's so bad about " + hateCapt.group(4) + "?"
    elif noMoreCapt != None:
        response = "How can excess " + noMoreCapt.group(2) + " be addressed?"
    elif excessCapt != None:
        choice = random.randint(1,2)
        switcher = {
            1: "What has made " + pronounMorph.get(excessCapt.group(1), excessCapt.group(1)) + " so " + excessCapt.group(10) + "?",
            2: "There are situations where being " + excessCapt.group(10) + " is beneficial",
            }
        response = switcher.get(choice)
    elif thesisCapt != None:
        response = "Do you agree with " + pronounMorph.get(thesisCapt.group(1), thesisCapt.group(1)) + "?"
    elif supportCapt != None:
        response = pronounMorph2.get(supportCapt.group(1), supportCapt.group(1)) + " favours " + supportCapt.group(8) + "? Why?"
    elif comment == "Goodbye":
        response = "Goodbye"
    elif badCapt != None:
        response = "How did " + badCapt.group(1) + " fall into that situation?"
    elif goodCapt != None:
        response = "What has made " + goodCapt.group(1) + " so fortunate?"
    elif lackCapt != None:
        response = "What can be done to improve " + lackCapt.group(4) + "?"
    elif prescriptCapt != None:
        response = "Why shouldn't " + prescriptCapt.group(1) + " do that?"
    elif tensionCapt != None:
        response = "How did this tension start"
    elif relatCapt != None:
        response = "Have relations always been " + relatCapt.group(2) + "?"
    elif queryCapt != None:
        response = "I'm not sure. What do you think?"
    elif reflexCapt != None:
        response = reflex.sub(pronounMorph.get(reflexCapt.group(1)), comment) + "?"
    elif defaultCapt != None:
        response = defaultCapt.group(2) + "?"
    
    #to remove excess whitespace
    response = response.upper()
    wsRemover = re.compile("\s+")
    response = wsRemover.sub(" ", response)
    
    return response