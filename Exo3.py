# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:25:29 2021

@author: EDEM
"""

from datetime import datetime
from functools import total_ordreing
import itertools

@total_ordreing
class Order :
    
    NewIdei = itertools.count()
    
    def __init__(self, quantite, prix, buy=True):
        self.__quantite = quantite
        self.__prix = prix
        self.__buy = buy
        self.__date= datetime.now()
        self.id = next(self.NewIdei)+1 

    def __str__(self):
        return "%s @ %s" % (self.__quantite, self.__prix)

    def __repr__(self):
        return "Order(%s, %s, %s)" % (self.__quantite, self.__prix,
                                                                  self.__buy)

    def __eq__(self, other): 
        return other and self.__quantite == other.__quantite and self.__prix == other.__prix
                     
    def __lt__(self, other): 
        return other and self.__prix < other.__prix
    
    def get_quantite(self):
        return self.__quantite
    
    def set_quantite(self, x):
        self.__quantite=x
        
    def get_prix(self):
        return self.__prix
    
    def get_buy(self):
        return self.__buy
    
    def get_date(self):
        return self.__date
    
    

class Book :
    
   
    
    
    def __init__(self, name, list_buy_ordres=[], list_sell_ordres=[] ):
        self.__name = name
        self.__list_buy_ordres = list_buy_ordres
        self.__list_sell_ordres = list_sell_ordres
        self.__string=""

    def __str__(self): 
        return self.__string
    
    def __repr__(self): 
        return "Book(%s, %s, %s)" % (self.__name, self.__list_buy_ordres, 
                                                     self.__list_sell_ordres)
    
    def insert_buy(self, quantite, prix):
        
        self.__list_buy_ordres.append(Order(quantite,prix,True))#We had the ordre to the book
        n=len(self.__list_buy_ordres)-1
        temp="--- Insert %s %s | ID : % s| Date : %s | on %s \n" % ("BUY" ,
                                                                    self.__list_buy_ordres[n] ,
                                                                    self.__list_buy_ordres[n].id,
                                                                    self.__list_buy_ordres[n].get_date(),
                                                                    self.__name)#We make the ordre public
        self.__string+=temp
        self.__list_buy_ordres.sort(key= lambda o: (o,o.get_date()), reverse=True)
        temp+=self.Executer_ordre()
        temp+=self.print_book()
        print(temp)
        
        
        
    def insert_sell(self, quantite, prix):
        self.__list_sell_ordres.append(Order(quantite,prix,False))#We had the ordre to the book
        n=len(self.__list_sell_ordres)-1
        temp="--- Insert %s %s | ID : % s| Date : %s | on %s \n" % ("SELL",
                                                                    self.__list_sell_ordres[n] ,
                                                                    self.__list_sell_ordres[n].id,
                                                                    self.__list_sell_ordres[n].get_date(),
                                                                    self.__name)#We make the ordre public
        self.__string+=temp
        self.__list_sell_ordres.sort(key= lambda o: (o,o.get_date()), reverse=False)
        self.__list_sell_ordres.reverse()
        temp+=self.Executer_ordre()
        temp+=self.print_book()
        print(temp)
        
            
    def Obtenir_buy_ordres(self):
        return self.__list_buy_ordres
    
    def Obtenir_sell_ordres(self):
        return self.__list_sell_ordres
    
    
    def print_book(self):
        temp=""
        temp+="Book on %s \n" % (self.__name)
        for k in self.__list_sell_ordres + self.__list_buy_ordres:
            temp+="\t %s %s | %s\n" % ("BUY" if k.get_buy() else "SELL", k, k.get_date())
        temp+="------------------------\n\n"
        self.__string+=temp
        return temp
    
    def Executer_ordre(self):
        temp=""
        while (self.__list_sell_ordres and self.__list_buy_ordres) and self.__list_sell_ordres[-1].get_prix()<=self.__list_buy_ordres[0].get_prix() :
            
            if self.__list_sell_ordres[-1].get_quantite()>self.__list_buy_ordres[0].get_quantite():
                temp+="Execute %s at %s on %s\n" % (self.__list_buy_ordres[0].get_quantite(),
                                                             self.__list_buy_ordres[0].get_prix(),
                                                             self.__name)
                self.__list_sell_ordres[-1].set_quantite(self.__list_sell_ordres[-1].get_quantite()-self.__list_buy_ordres[0].get_quantite())
                self.__list_buy_ordres.pop(0)

            else :
                temp+="Execute %s at %s on %s\n" % (self.__list_sell_ordres[-1].get_quantite(),
                                                             self.__list_buy_ordres[0].get_prix(),
                                                             self.__name)
                self.__list_buy_ordres[0].set_quantite(self.__list_buy_ordres[0].get_quantite()-self.__list_sell_ordres[-1].get_quantite())
                self.__list_sell_ordres.pop()
            self.__string+=temp
        return temp