import json
import re
import requests
import numpy
def summarization(roomname):
    room=str(roomname)
    accessToken = "bf8426d5-7e47-4f3d-9802-fc827f74cfb5"
    file=open(roomname+".docx",'r')
    frequency={}
    sadi={}
    inputText=file.read()
    JSON_MSG = "{ \"text\" : \"" + inputText + "\" , \"token\" : \"" + accessToken + "\" }"
#print(JSON_MSG)
    response = requests.post('https://api.cle.org.pk/v1/pos',json={"text":inputText,"token":accessToken})
    response=response.json()
    with open('pos.json','w') as f:
        json.dump(response,f)
    f.close()
    with open('pos.json',"r") as w:
        saad=json.load(w)
    w.close()
#print(type(saad))
    fareed=saad['response']
    sadi=(fareed['tagged_text'])
#print(sadi)

    sentence_li=[]
    x = sadi.split("ہے")
    DF={}
#print(x)
    for i in range(len(x)):
        #print(x[i])
        sentence_li.append(x[i])
        #print("\n")
#print(sentence_li)
#print(len(sentence_li))

    NN_li=[]
    NNP_li=[]
    VBF_li=[]
    other_li=[]
    for i in range(len(sentence_li)):
        sentence=str(sentence_li[i])
        s=sentence.split(" ")
        NN=0
        NNP=0
        VBF=0
        other=0
        for w in s:
            f=str(w)
            f=f.split("|")
        #print(f)
            for w in f[::2]:
                #print(w)
                if(w=="NN"):
                    NN=NN+1
                elif(w=="NNP"):
                    NNP=NNP+1
                elif(w=="VBF" or w=="VBI"):
                    VBF=VBF+1
                else:
                    other=other+1
      
        NN_li.append(NN)
        NNP_li.append(NNP)
        VBF_li.append(VBF)
        other_li.append(other)
    
#print("List of Noun Singular in sentence: ")
#print(NN_li)
#print("\n")
#print("List of Proper Noun Singular in sentence: ")
#print(NNP_li)
#print("\n")
#print("List of Verb Singular in sentence: ")
#print(VBF_li)
#print("\n")
    result=NN_li
    for i in range(len(result)):
        result[i]=result[i]+NNP_li[i]+VBF_li[i]
    
#print("Resultant Score list of sentence: ")
#print(result)
#print("\n")
    fi=open(roomname+".docx",'r')
    textfile=fi.read()
    tex=textfile.split("ہے")
    sort_index = numpy.argsort(result)[::-1]
#print(sort_index)
    sort_index=list(sort_index)
    length = len(sort_index)
#print(length)
    sum_index = length//3
#print(sum_index)
    summary = sort_index[:sum_index]
#print(summary)
#print("\n")
    #print("Summary...\n")
    final=""
    for i in summary:
        final=final+tex[i]
        f = open(room+"summary"+".docx", "a")
        f.write(final)
        f.close()
    #print(final)
    
summarization("1")