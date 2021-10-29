
#File serach engine to search a file and store the results in text file and database(using postgreSQL)

from inspect import _empty
import os
from db import *
import PySimpleGUI as sg
import threading
from gui import *
        

class SearchEngine:
    def __init__(self):
        self.file_index=[]
        self.results=[]
        self.matches=0
        self.records=0
    
    #creating new index

    def create_new_index(self,path):
        root_path=path
        self.file_index=[(root,files) for root,dirs,files in os.walk(root_path) if files]

    #function for search

    def search(self,values,path):
        #reset variables
        root_path=path
        self.file_index=[(root,files) for root,dirs,files in os.walk(root_path) if files]
        self.results.clear()
        self.matches=0
        self.records=0
        term=values['term']

        #perform search

        for path,files in self.file_index:
            for file in files:
                self.records +=1
                if( values['contains'] and term.lower() in file.lower() or
                    values['beginswith'] and file.lower().startswith(term.lower()) or
                    values['endswith'] and file.lower().endswith(term.lower()) or values['file'] and term == file):

                        result=path.replace('\\','/') + '/' + file
                        self.results.append(result)
                        self.matches +=1
                        #print(result)
                else:
                    continue
        #save search results in text file(optional)

        with open('search_results.txt','w') as f:
            for row in self.results:
                f.write(row+'\n')


def test1(values):
    #search_doc=input("Enter the name of the document to be searched")
    d=database()  #creating object of database
    threads=[]
    results_db=[]
    results_db=d.search_db(values)
    s=SearchEngine()  #creating object of SearchEngine
    if(not results_db):
        print("-----From file search-----")
        if (values['path'] == ""):
            values['path']=['C:\\','D:\\']
        
        #using threads to search file concurrently on different drives 
       
            for path in values['path']:
                t1=threading.Thread(target=s.search,args=[values,path])
                t1.start()
                threads.append(t1)
            for t in threads:
                t.join()
        else:
            s.search(values,values['path'])
            print()
        print('>> There were {:,d} matches out of {:d} records searched.'.format(s.matches,s.records))
        for match in s.results:
            d.addrecord(match)  #adds record to database
            print(match)    
def main():
    g=Gui()
    while True:
        event,values =g.window.read()
        if event is None:
            break      
        if event=='search':
            test1(values)
main()       
        
        
        
        
        
        
        
