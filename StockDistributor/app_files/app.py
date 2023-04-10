#========================
#notes
#========================

#ID - 13972515
#Password - DupaBlada360
#Who is Balad?

#installs
#pip install websocket-client==1.4.1
#pip install termtables
#pip install pytz
#pip install decimal

#========================
#imports
#========================

import sys
import os
import getpass
import termtables as tt
from API import XTB
from datetime import datetime
import pytz
import json
from decimal import *
getcontext().prec = 6

#========================
#tekst
#========================

#login
hello = "Hello Trader! "
selectaccount = """Please select the account that we will be working with today starting by providing its Lp. You can also press enter to use a custom account"""
incorectmsg = """Please provide a number that corresponds to your selected account, you can also press enter to use a custom account"""
howtologin="""Please select the account that we will be working with today starting by providing its user ID first (exp. 13972515)...
You can also select the type of your account. Default is demo.(exp. 13972515,demo)"""
prowidepasword="Now type in the password to your account (exp. DupaBlada360)..."
nolettersinID="""There can be no letters in {user ID}."""
incorectcredencials1="""
Looks like the credentials You provided were incorrect because:""" 
incorectcredencials2="""Try again starting with {user ID} of your account...(exp. 13972515)
You can also select the type of your account, default is demo.(exp. 13972515,demo)"""
#workingamount
askworkingamount="""Now chose how much of your balance do you want the app to work on."""
wholebalance = """If you want the app to work on your whole balance just press enter!"""
justnumbers = """Please provide a number that corresponds to how much of your balance you want the app to work on."""
nothyerthanbalnce = """The amount of balance that you designate can't be hayer than your balance."""
#selecting tickers
selectticckers="""Now its time to specify which tickers should the amount specified earlier be distributed between.
To do tha simply provide the tickers one after another in such fashion:{ticker},{ticker},{ticker},... exp.(T.US,EURUSD,EURPLN, P.vh)
You can also import .json files: (exp_Indexes.json-defaults [than must be in the folder of this program]"""
chosewhattodo="""This are the tickets you selected. You may now select what to do with each one, address them by their LP. than select what to do.
-if seweral tickets were found, chose wich one to go with by typing the number that corresponds with it like so: 1-1 
    (numbers at the end of stocks corespond to: \033[1m5 - ETF CFD, 4 - CFD, 9 - Stock\033[0m)
-if u want to delete eny of them type in lp.-d for example 2-d
-typing in just a raw ticker will ad it to the table
-\033[1md\033[0m alone will delete all the tickets taht weren't found
you may make changes to seweral tickets at the time: 1-2, 2-d, 4-d, T.US
and just presing {enter} will remove all the missing ones and chose the first one if there are any to chose
You can also import .json files: (exp_Indexes.json-defaults [than must be in the folder of this program] """
looksgoog='\033[1m'+"""   Every ticker looks good and is redy for further use!
    Presing {enter} now will take you too the next step!"""+'\033[0m'
chosewhattodo2="""This are the tickets you selected. You may now select what to do with each one, address them by thair LP. than select what to do.
-if seweral tickets were found, chose wich one to go with by typing the number that corresponds with it like so: 1-1 
    (numbers at the end of stocks corespond to: \033[1m5 - ETF CFD, 4 - CFD, 9 - Stock\033[0m)
-if u want to delete eny of them type in lp.-d for example 2-d
-typing in just a raw ticker will add it to the table
-\033[1md\033[0m alone will delete all the tickets taht weren't found
you may make changes to seweral tickets at the time: 1-2, 2-d, 4-d, T.US
You can also import .json files: (exp_Indexes.json-defaults [than must be in the folder of this program] """
#geting prices and data
notfound = "Some of the tickers you selected, where not found. (The API returnrd a error)"
closedtrade ="Some ticker from your selection are closed curently, you can type {w} to make the program wait for the tickers to become open"
toshort = "Some tickers are open for to short, they canot be included.(OPEN for <= 0.1h)"
advace = '\033[1m'+"  Every thing looks great, presing {enter} now will take you to the next step!"+'\033[0m'
info =  """You can remove tickers by providing teir Lp. number (1/2/3...), you can alsow select multiple at a time by seperting them by a coma(1,2,3...)
And presing enter will automaticly remove all tickers tahat are ioncorect."""
#combination calculation
mathinfo = """This is what the program was able to calculate, you can remove tickers using theier LP. number (1/2/3...,1/2/3...,...)
Use {w} to togle wating.

    \033[4m\033[95m\033[1mJust persing enter will perchese this tickers!\033[0m"""
#basiccomands
ester = ['\033[95m'+'One day,'+'\033[0m','\033[96m'+'A wise man came,'+'\033[0m','\033[36m'+'To the lair of begining,'+'\033[0m','\033[94m'+'He took a glimpse,'+'\033[0m','\033[92m'+'At the young script,'+'\033[0m','\033[93m'+'And said only this:'+'\033[0m','\033[91m'+'Who Is Balad?'+'\033[0m','Then he left.']
basiccomands="Use \033[1mq\033[0m to quit, \033[1mr\033[0m to restart."
basiccomands1="Use \033[1mq\033[0m to quit, \033[1mr\033[0m to restart."

#========================
#functions
#========================

#specific functions

def removedubles(list):
    clist = list
    glist = list
    for o in list:
        c = 0
        for g in clist:
            if o[1] == g[1]:
                c = c + 1
        if c > 1:
            glist.remove(g)
    return glist

def renumber(tickers):
    lp = 0
    for i in tickers:
        lp = lp + 1
        i[0] = lp
    return tickers

def chekticker(AllSymbols, ticker): 
    i = ticker
    clear()
    print("Cheking Tickers...")
    firtst = False
    if '.' in i[1]:
        i[1]  = upp(i[1])
        o = str(i[1]).split('.')
        if (o[0] != ''):
            for k in AllSymbols:
                l = k.split('.')
                if l[0] == o[0]:
                    if firtst == False:
                        i[1] = [k]
                        firtst = True
                        i[2] = 1
                    elif firtst == True:
                        i[1].append(k)
                        i[2] = 2
                if i[2] == '':
                    i[2] = 3
        else: i[2] = 4     
    else: 
        if i[1] in AllSymbols:
            i[2] = 5
        else: i[2] = 6
    print("Done!")
    return i

def chektickers(AllSymbols, tickers):    
    clear()
    print("Cheking Tickers...")
    for i in tickers:
        firtst = False
        if '.' in i[1]:
            o = str(i[1]).split('.')
            try:
                g = o[1].split('-')
                o = [o[0],g[0],g[1]]
            except:
                pass
            if o[1] == "json":
                file =f'{o[0]}.{o[1]}'
                with open(file) as f:
                    try:
                        data = json.load(f)
                    except:
                        print("file not founf!")
                        break
                try:
                    tickersg = data[o[2]]
                except:
                    tickersg = data
                tickers.remove(i)
                for i in tickersg:
                    tickers.append(['',i,''])
                tickers = chektickers(AllSymbols, tickers)
                break
            o[0] = upp(o[0])
            if (o[0] != ''):
                for k in AllSymbols:
                    l = k.split('.')
                    if l[0] == o[0]:
                        if firtst == False:
                            i[1] = [k]
                            firtst = True
                            i[2] = 1
                        elif firtst == True:
                            i[1].append(k)
                            i[2] = 2
                    if i[2] == '':
                        i[2] = 3
            else: tickers.pop(i[0]-1)  
        else: 
            if i[1] in AllSymbols:
                i[2] = 5
            else: i[2] = 6
    print("Done!")
    return tickers

def prepforprint(tickers,headers):
    tickersp = []
    # my brother in christ, use a switch statement
    for i in tickers:
        a = san(str(i[1]))
        if i[2] == 1:
            tickersp.append([i[0],a,'found']) 
        elif i[2] == 2:
            tickersp.append([i[0],a,'\033[94m'+'select: (5 - ETF CFD, 4 - CFD, 9 - STC)'+'\033[0m']) 
        elif i[2] == 3:
            tickersp.append([i[0],a,'\033[91m'+'not found'+'\033[0m']) 
        elif i[2] == 4:
            tickersp.append([i[0],a,'\033[91m'+'not a ticker'+'\033[0m']) 
        elif i[2] == 5:
            tickersp.append([i[0],a,'instrument found']) 
        elif i[2] == 6:
            tickersp.append([i[0],a,'\033[91m'+'instrument not found'+'\033[0m']) 
        else:
            tickersp.append([i[0],a,'\033[95m'+'wird ass bug'+'\033[0m']) 

    tickerspp = tt.to_string(tickersp,header=headers,style=tt.styles.ascii_thin_double,)
    
    return tickerspp

def chekifgood(tickersg):
    descriptions = []
    allgood = True
    if tickersg == [] or (tickersg == ''):
        allgood = False
    else:
        for i in tickersg:
            descriptions.append(i[2])
        allgood = True
        for u in descriptions:
            if (u==3) or (u==4) or (u==6) or (u==2):
                allgood = False
    return allgood

#basicfunctions

def rouddown(nume,p=2):
  nume = str(nume)
  num=nume.split('.')
  c = 0
  nums = num[0]+'.'
  for i in num[1]:
    c += 1
    if c <= p:
      nums = nums + i
  if p == 0:
    nums = nums + '0'
  return nums

def upp(input_string):
    output_string = ''
    for i in input_string:
        if input_string.isupper() == True:
            output_string += i
        else:
            output_string += i.upper()
    return output_string

def san(input_string):
    output_string = ''
    for i in input_string:
        if (i == ' ') or (i == '[') or (i == ']'):
            outchar = ''
        else:
            outchar = i
        output_string += outchar
    return output_string

def clear():
    c = True
    if c == True:
        print('Who is Balad?')
        os.system("clear" if (os.name == "posix") else "cls")

def crudecomands(input1):
    if input1 == "q" :
        sys.exit()
    elif input1 == "r":
       main()
    elif input1 == "WhoisBalad?":
        clear()
        input()
        for x in ester:
            print(x)
            input()
        clear()
        
#========================
#CODE
#========================

def main():

    #=login=

    ID = ""
    Password = ""
    real = False

    clear()
    satage = 0
    incorect = False
    done = False
    while True:
      try:
        f = open("accounts.json",)
        accounts = json.load(f)
      except:
        break
      clear()
      if done:
         break
      if accounts != [] and satage == 0:
        print('', hello, selectaccount, basiccomands1, sep= '\n'+'\n') 
        print(tt.to_string(accounts,header=["Lp.", "ID", "Type", "note"],style=tt.styles.ascii_thin_double,))
        comands = "1/2/3...,{enter}, q, r,"
        satage = 1
      if incorect:
        print('', incorectmsg, basiccomands1, sep= '\n'+'\n') 
        print(tt.to_string(accounts,header=["Lp.", "ID", "Type", "note"],style=tt.styles.ascii_thin_double,))
        comands = "1/2/3...,{enter}, q, r,"
      
      inputs = san(input("<comands - "+ comands +"> "))
      crudecomands(input)

      if inputs == '':
        break
      for i in accounts:
        if inputs == str(i[0]):
          ID = str(i[1])
          if  i[2] == 'real':
            real = True
          done = True
        else:
          incorect = True
    balance = 0
    corectcredencials = 0
    while True:
        clear()
        if (ID=='') or (Password==''):
            getID = False
            if (ID==''):
               getID = True
            hasletters = False
            while True:
                clear()
                if corectcredencials == 1:
                    print('', incorectcredencials1 + '\n' + '---' + API.loginp()["errorDescr"]  + "---" + '\n' + incorectcredencials2, basiccomands1, sep= '\n'+'\n')
                    comands = "ID, q, r,"
                    corectcredencials = 3
                if (not getID) and (corectcredencials != 3):
                    print('', prowidepasword, ID, basiccomands1, sep= '\n'+'\n')
                    comands = "Password, q, r,"
                    Password = getpass.getpass(prompt="<comands - "+ comands +"> ")
                    crudecomands(Password)
                    break
                if (not hasletters) and (corectcredencials == 0):
                    print('', hello, howtologin, basiccomands1, sep= '\n'+'\n')
                    comands = "ID, q, r,"
                if (not hasletters) and (corectcredencials != 3) and (corectcredencials >0) :
                    print('', howtologin, basiccomands1, sep= '\n'+'\n')
                    comands = "ID, q, r,"
                if (hasletters) and (corectcredencials !=3):
                    print('', nolettersinID, basiccomands1, sep= '\n'+'\n')
                    comands = "ID, q, r,"
                    hasletters = False
                if corectcredencials == 3:
                    corectcredencials=4

                input1 = san(input("<comands - "+ comands +"> "))
                crudecomands(input1)

                if input1 != '':
                    if ',' in input1:
                      a = input1.split(',')
                      if a[1] == 'real':
                        real = True
                      else:
                        real = False
                      for i in a[0]:
                        if i.isalpha():
                          hasletters = True
                    else:
                      real = False
                      for i in input1:
                          if i.isalpha():
                              hasletters = True
                    if not hasletters:
                        try: 
                          ID = a[0]
                        except:
                          ID = input1
                        getID = False
        API = XTB(ID, Password,real)

        def baseiccomands(input1):
            if input1 == "q" :
                API.logout()
                sys.exit()
            elif input1 == "r":
               main()
            elif input1 == "WhoisBalad?":
                clear()
                input()
                for x in ester:
                    print(x)
                    input()
                clear()
        clear()
        print('Logoging in...')
        try:
            balance=API.get_Balance()
            chek = True
        except:
            chek = False
        if chek == False:
            corectcredencials = 1  
            ID = ''
            Password = ''            
        else: 
            break

    #=working amount=

    currency = API.get_AccCurency()
    clear()
    print('', 'Loged in!', sep= '\n'+'\n')
    pbalance=f'\033[1mYour current balance is \033[92m{str(balance)} {currency}\033[0m'
    noclerar = False
    cantbehyer = False
    noleeters = False
    comands = "ammount/{enter}, q, r,"
    workingamount = 0
    while True:
        if noclerar:
            clear()
        noclerar = True
        if (not cantbehyer) and (not noleeters):
            print('', pbalance, askworkingamount, wholebalance, basiccomands, sep= '\n'+'\n')
        if noleeters:
            print('', pbalance, justnumbers, wholebalance, basiccomands, sep= '\n'+'\n')
            noleeters = False
        if cantbehyer:
            print('', pbalance, nothyerthanbalnce, wholebalance, basiccomands, sep= '\n'+'\n')  
            cantbehyer = False

        input2 = san(input("<comands - "+ comands +"> "))
        baseiccomands(input2)

        if input2 == '':
            workingamount = balance
            break
        try:
            input2 = float(input2)
            if input2 <= balance:
                workingamount = input2
                break
            else:
                cantbehyer = True
        except:
            noleeters = True
    balance = 0
    clear()

    #=make file=

    def  chekfileposibleTickers():

        clear()

        print("Cheking if file 'posibleTickers.txt' exsits")
        if os.path.isfile('posibleTickers.txt'):
             print('File with all the avilable tickets for tour account exsists!')
        else:
            print('File not found!')
            print('Maiking file with all the avilable tickets for tour account...')
            with open('posibleTickers.txt','w') as f:

                Symbols=API.get_AllSymbols()

                for i in Symbols:
                    f.write("%s\n" % i["symbol"])
            print('File made!')
        clear()
    
    def  chekfileminimumtransaction():

        clear()

        print("Cheking if file 'minimumTarnsactions.txt' exsits")
        if os.path.isfile('minimumTarnsactions.txt'):
            print('File with minimum transactions exsists!')
        else:
            print('File not found!')
            print('Maiking file with minimum valiues for transactions...')
            with open('minimumTarnsactions.txt','w') as f:
                Symbols=API.get_AllSymbols()
                categories = []
                for i in Symbols:
                    cat = i["categoryName"]
                    if cat not in categories:
                        categories.append(cat)
                for i in categories:
                    if i == "STC":
                        txt = f'{i} - {10}'
                    else:
                        txt = f'{i} - {0}'
                    f.write("%s\n" % txt,)
            print('File made!')
        clear()

    chekfileposibleTickers()
    chekfileminimumtransaction()

    #=sellect tickers=

    print('', '\033[1m'+'The amount of money to be dystribiute today is ' +'\033[92m'+ str(workingamount) + ' ' + currency+'\033[0m', sep= '\n'+'\n')
    bs = [False,[],'',0,False,False]
    noclerar = False
    with open("posibleTickers.txt", "r") as f:
        f = open("posibleTickers.txt", "r")
        AllSymbols = f.read().splitlines()

    def pickticker(bs):
        noclerar = bs[0]
        tickers = bs[1]
        tickersp =bs[2]
        stage = bs[3]
        godtogo = bs[4]
        fanaly = bs[5]
        while True:
            if godtogo == True:
                stage = -1
            if noclerar:
                clear()
            noclerar = True
            if stage == 0:
                print('', selectticckers, basiccomands, sep= '\n'+'\n')  
                comands = "[{ticker},{ticker},{ticker},...], q, r,"
            if stage == 1:
                print('', selectticckers, "You heave to geave us some thing to work with!",basiccomands, sep= '\n'+'\n')  
                comands = "[{ticker},{ticker},{ticker},...], q, r,"
                stage = 5
            if godtogo == True:
                print('',tickersp,looksgoog ,chosewhattodo2, basiccomands, sep= '\n'+'\n')  
                comands = "[lp{1/2/3...}-{select{1/2/3..}/d},{1/2/3...}-{{1/2/3..}/d}]/{new ticker}/[enter]/d/q/r"
                fanaly = True  
            if (stage == 2) or (stage == 4):
                print('',tickersp ,chosewhattodo, basiccomands, sep= '\n'+'\n')  
                comands = "[lp{1/2/3...}-{select{1/2/3..}/d},{1/2/3...}-{{1/2/3..}/d}]/{new ticker}/[enter]/d/q/r"
                stage = 4
            input3 = san(input("<comands - "+ comands +"> "))
            baseiccomands(input3)
            if stage == 0:
                if input3 == '':
                    stage = 1
                else:
                    stage = 2
                    tickersd = input3.split(",")
                    a=1
                    for e in tickersd:
                        if e != '':
                            tickers.append([a, e, ""])
                            a = a + 1
                    if (tickers == '') or (tickers == []):
                        stage = 1
                    else:
                        tickers = chektickers(AllSymbols, tickers)
                        tickers = removedubles(tickers)
                        tickers = renumber(tickers)
                        godtogo = chekifgood(tickers)
                        tickersp = prepforprint(tickers,["Lp.", "Ticker", "Description"])
            if (stage == 4) or (stage == 5):
                stage = 4
                tickerss = []
                if input3 == '':
                    for i in tickers:
                        if (i[2] == 1 ) or (i[2] == 2) or (i[2] == 5):
                            if i[2] == 2:
                                tickerss.append([i[0], i[1][0], 1])
                            else:
                                tickerss.append([i[0], i[1], i[2]])
                    tickers = tickerss
                if  input3 == 'd':
                    for i in tickers:
                        if (i[2] == 1 ) or (i[2] == 2) or (i[2] == 5):
                            tickerss.append([i[0], i[1], i[2]])
                    tickers = tickerss   
                elif  input3 != '':  
                    comandlist =  input3.split(',') 
                    for i in  comandlist:
                        if i != '':
                            blob = False
                            if ('-' in i):
                              if ('json' not in i):
                                u = i.split('-')                        
                                l = int(u[0])
                                if u[1] == 'd':
                                    for c in  tickers:
                                        if (c[0] == l) :
                                            tickers.pop(l-1)
                                else:                         
                                    try:
                                      j = int(u[1])                       
                                      blob = True
                                    except:
                                        blob = False
                                if blob: 
                                    j -= 1 
                                    for c in  tickers:
                                        if (c[0] == l) and  (c[2] == 2):
                                            try:
                                              c[1] = c[1][j]
                                              c[2] = 1
                                            except:
                                              pass
                              else:
                                tickers.append(['',i,''])
                                tickers = chektickers(AllSymbols, tickers)
                                tickers = removedubles(tickers)
                                tickers = renumber(tickers)
                                godtogo = chekifgood(tickers)
                                tickersp = prepforprint(tickers,["Lp.", "Ticker", "Description"])
                            else:
                                tickera = ['',i,'']
                                tickera = chekticker(AllSymbols, tickera)
                                tickers.append(tickera)
                if (tickers == '') or (tickers == []):
                    stage = 1
                else:
                    tickers = removedubles(tickers)
                    tickers = renumber(tickers)
                    godtogo = chekifgood(tickers)
                    tickersp = prepforprint(tickers,["Lp.", "Ticker", "Description"])
            if fanaly:
                if input3 == '':
                    print('Done!')
                    break
                fanaly = False
                stage = 4
                if  input3 == 'd':
                    for i in tickers:
                        if (i[2] == 1 ) or (i[2] == 2) or (i[2] == 5):
                            tickerss.append([i[0], i[1], i[2]])
                    tickers = tickerss   
                elif  input3 != '':  
                    comandlist =  input3.split(',') 
                    for i in  comandlist:
                        if i != '':
                            blob = False
                            if ('-' in i):
                              if ('json' not in i):
                                u = i.split('-')                        
                                l = int(u[0])
                                if u[1] == 'd':
                                    for c in  tickers:
                                        if (c[0] == l) :
                                            tickers.pop(l-1)
                                else:                         
                                    try:
                                      j = int(u[1])                       
                                      blob = True
                                    except:
                                        blob = False
                                if blob: 
                                    j -= 1 
                                    for c in  tickers:
                                        if (c[0] == l) and  (c[2] == 2):
                                            try:
                                              c[1] = c[2][j]
                                              c[2] = 1 
                                            except:
                                               pass
                              else:
                                tickers.append(['',i,''])
                                tickers = chektickers(AllSymbols, tickers)
                                tickers = removedubles(tickers)
                                tickers = renumber(tickers)
                                godtogo = chekifgood(tickers)
                                tickersp = prepforprint(tickers,["Lp.", "Ticker", "Description"])              
                            else:
                                tickera = ['',i,'']
                                tickera = chekticker(AllSymbols, tickera)
                                tickers.append(tickera)
                godtogo = chekifgood(tickers)
                if (tickers == '') or (tickers == []):
                    stage = 1
                else:
                    tickers = removedubles(tickers)
                    tickers = renumber(tickers)
                    tickersp = prepforprint(tickers,["Lp.", "Ticker", "Description"])
        return ([noclerar,tickers,tickersp,stage,godtogo,fanaly])
    
    #geting prices and data 
    bs = pickticker(bs)
    tickers = bs[1]
    def datafeching(tickers):
      symbolprice = []
      psymbolprice = []
      clear()
      print('Geting Prices...')

      with open("minimumTarnsactions.txt", "r") as f:
          file = f.read().splitlines()
          categories=[]
          for i in file:
            y = san(i)
            a = y.split('-')
            categories.append(a)


      for i in tickers:
          API.login() 
          lp = i[0] 
          data = API.get_Symbol(i[1])
          if data != False:   
              symbol = data["symbol"]
              monidata = API.get_CommissionDef(symbol,data['lotMin'])
              lotstep = data["lotStep"]
              price = (data["ask"]/lotstep)
              price1 = f'{price} {data["currency"]}'
              #price pln

              minprice = 0
              for i in categories:
                  if i[0] == data["categoryName"]:
                      minprice = float(i[1])

              if data['currencyPair'] == True:
                  pricepln = price + (monidata['commission'])
                  pricepln1 = f'{pricepln} {currency}'
                  mintrade = minprice
                  mintrade1 = f'{mintrade} {currency}'
              else:
                  pricepln = (price * (monidata['rateOfExchange'])) + (monidata['commission'])
                  pricepln1 = f'{pricepln} {currency}'
                  mintrade = minprice * (monidata['rateOfExchange'])
                  mintrade1 = f'{mintrade} {currency}'

              #min voliune valiue pln
              minvaliue= pricepln*(data["lotMin"])
              minvaliue1= data["lotMin"]

              #lotmin
              lotmin= data["lotMin"]
              #lotmax
              lotmax= data["lotMax"]

              #tradeopen
              def lookinfutureclose(dayofweek,symbol):
                    maxmsinday = (24*60*60*1000)
                    dayofweek = int(dayofweek)
                    opendata = []
                    openin = 0
                    if dayofweek == 7:
                      dayofweekfuture = 1 
                    else:
                      dayofweekfuture = dayofweek + 1 

                    while True:
                        opendata = API.get_TradingHours(symbol, int(dayofweekfuture))
                        if dayofweekfuture == 7:
                          dayofweekfuture = 1 
                        else:
                          dayofweekfuture += 1
                        if opendata == False:
                          openin += maxmsinday
                        else:
                          openin += opendata[0]['fromT']
                          break
                        if dayofweekfuture == dayofweek:
                            openin = 0000
                            break
                    return openin
              def lookinfutureopen(dayofweek,symbol,openin):
                    maxmsinday = (24*60*60*1000)
                    dayofweek = int(dayofweek)
                    if dayofweek == 7:
                      dayofweekfuture = 1 
                    else:
                      dayofweekfuture = dayofweek + 1 
                    while True:
                        opendata = API.get_TradingHours(symbol, int(dayofweekfuture))
                        if dayofweekfuture == 7:
                            dayofweekfuture = 1 
                        else:
                            dayofweekfuture += 1 
                        if (opendata == False) or (opendata[0]['fromT'] != 0):
                          break
                        elif (opendata[0]["fromT"] == 0) and (opendata[0]['toT'] != maxmsinday):
                            openin +=  opendata[0]['toT'] 
                            break           
                        else:
                            openin += maxmsinday
                        if dayofweekfuture == dayofweek:
                            openin = 0000
                            break
                    return openin

              openin = 0.0
              openclosed = ''
              now = datetime.now(pytz.timezone("CET"))
              week = int(now.strftime('%w'))
              if week == 0:
                  week = 7
              hours = int(now.strftime("%H"))
              minutes = int(now.strftime("%M"))
              segundos = int(now.strftime("%S"))
              timeinms = (hours*60*60*1000)+(minutes*60*1000)+(segundos*1000) 
              maxmsinday = (24*60*60*1000) 
              API.login()
              opendata = API.get_TradingHours(symbol, week)

              if opendata != False:
                  for i in opendata:
                      if timeinms < i["fromT"]:
                          openin = i["fromT"] - timeinms 
                          openclosed = '\033[91m'+'CLOSED'+'\033[0m'
                          break
                      elif (timeinms >= i["fromT"]) and (timeinms < i["toT"]):
                          openclosed = '\033[92m'+'OPEN'+'\033[0m'
                          openin = i["toT"] - timeinms
                          if i["toT"] == maxmsinday:
                              openin = lookinfutureopen(week,symbol,openin) 
                          break
                  if timeinms >= opendata[-1]["toT"]:
                      openclosed = '\033[91m'+'CLOSED'+'\033[0m'
                      openin = lookinfutureclose(week,symbol)
              else:
                  openclosed = '\033[91m'+'CLOSED'+'\033[0m'
                  openin = lookinfutureclose(week,symbol)

              openin = int(openin)
              if openin != 0000:
                  openin1 = rouddown(openin/(60*60*1000),2)
              else:
                  openin,openin1 = '\033[95m'+'infinite '+'\033[0m'

              tradeopen = [openclosed, openin]
              tradeopen1 = f'{openclosed} for {openin1}h'
              #output asembling
              symbolprice.append([lp,symbol,price,pricepln,minvaliue,mintrade,tradeopen,lotmin,lotmax,lotstep])
              psymbolprice.append([lp,symbol,price1,pricepln1,minvaliue1,mintrade1,tradeopen1,])
          else:
              symbolprice.append([lp,i[1],'Not found','-','-','-','-','-','-'])
              psymbolprice.append([lp,i[1],'Not found','-','-','-','-',])
      print('Done!')
      API.logout()
      return symbolprice,psymbolprice
    symbolprice,psymbolprice = datafeching(tickers)
    clear()
    wait = False
    unknowncomand = False
    while True:
      notime = False
      closed = False
      mising = False
      redy = True
      if symbolprice != []:
        for i in symbolprice:
          if i[2] == 'Not found':
            mising = True
            redy = False
          elif i[6][0] == '\033[91m'+'CLOSED'+'\033[0m':
            closed = True
            redy = False
          elif (i[6][0] == '\033[92m'+'OPEN'+'\033[0m') and (i[6][1] <= 0.1):
            notime = True
            redy = False

      clear()  
      print(tt.to_string(psymbolprice,header=["Lp.", "Symbol", "Price",'Price'+ currency,"Min Voliune Valiue",'Min. Perches','Trading Open/Closed'],style=tt.styles.ascii_thin_double,))
      comands = "{enter},[{1/2/3/...},{1/2/3/...},{1/2/3/...},...], w, q, r,"
      print('')
      if wait:
        print('\033[96m'+'Wating enebled!'+'\033[0m' '\n' 'In the buing phaze the program will sleap for the specifird amount of time.','\n','\n')
      if mising:
        print(notfound,'\n')
      if closed:
        print(closedtrade,'\n')
      if notime:
        print(toshort,'\n')
      if unknowncomand:
        print('\033[91m'+'Comand not found!'+'\033[0m','\n')
        unknowncomand = False
      if redy:
        print(advace,'\n')
      print(info,'\n')
      print(basiccomands)
      input3 = san(input("<comands - "+ comands +"> "))
      baseiccomands(input3)
      if input3 == 'w':
        wait = not wait
      elif (input3 == "") and (redy == True):
        break
      elif (input3 == "") and (wait == True) and (notime == False) and (mising == False):
        break
      elif input3 == "":
        for i in symbolprice[:]:
          if (i[2] == 'Not found') or ((i[6][0] == '\033[92m'+'OPEN'+'\033[0m') and (i[6][1] <= 100000)):
            symbolprice.remove(i)
            for b in psymbolprice[:]:
              if i[0] == b[0]:
                 psymbolprice.remove(b)
          if (i[6][0] == '\033[91m'+'CLOSED'+'\033[0m') and (wait == False):
            symbolprice.remove(i)
            for b in psymbolprice[:]:
              if i[0] == b[0]:
                 psymbolprice.remove(b)
      else:
        index = input3.split(',')
        unknowncomand = True
        for i in index:
          try:
            a = int(i)
            for i in symbolprice[:]:
              if i[0] == a:
                 symbolprice.remove(i)
                 unknowncomand = False
            for i in psymbolprice[:]:
              if i[0] == a:
                 psymbolprice.remove(i)
                 unknowncomand = False
          except:
            pass 
      if symbolprice == []:
        print('empty, restart')
        baseiccomands('r')
      symbolprice = renumber(symbolprice)

    # calculating combination

    comands = "{enter},[{1/2/3/...},{1/2/3/...},{1/2/3/...},...], q, r, w"
    unknowncomand = False
    while True:
      clear()

      def sum(out):
        for i in out:
          i[4] = Decimal(i[2])*Decimal(i[3])
        return out

      def tsum(preped):
        s = 0
        for i in preped:
          s = Decimal(s) + Decimal(i[4])
        return s

      def prep(raw1):
        raw1.sort(reverse= True,key=lambda x: x[2])
        out = []
        for i in raw1:
          #["Lp.", "Symbol",'Price',"Amount",'Valiue','lotstep','lotmax','lotmin','Avilabilty','Min. Prechuse']
          out.append([i[0],i[1],i[3],i[7],0,i[9],i[8],i[7],i[6][0],i[6][1],i[5]])
          while (Decimal(out[-1][2])*Decimal(out[-1][3])) <= i[5]:
            out[-1][3] = Decimal(out[-1][3]) + Decimal(out[-1][5]) 
        out = sum(out)
        return out

      def mainframe (raw1,preped1,ma1):
        print("Calculating...")
        p =[]
        preped1.reverse()
        for i in raw1:
          p.append(i[0])
        s = tsum(preped1)
        while s > ma1:
          sum(preped1)
          s = tsum(preped1)
          for n in preped1:
            if n[3] != 0:
              n[3] = Decimal(n[3]) - Decimal(n[5])
              sum(preped1)
              s = tsum(preped1)
              break
          c = 0
          for i in preped:
            c = Decimal(c) + Decimal(i[3])
          if c == 0:
            print ('nah man')
            break
        preped1.reverse()
        while p != []:
          for i in p[:]:
            preped2 = sum(preped1)
            s = tsum(preped1)
            for n in preped1:
              if n[0] == i:
                n[3] = Decimal(n[3]) + Decimal(n[5])
                sum(preped1)
                s = tsum(preped1)
                debug = False
                if  debug == True:
                  print (f'{n[3]}  |  {s} - {ma1} = {Decimal(ma1) - s}')
                if s >= Decimal(ma1):
                  n[3] = Decimal(n[3]) - Decimal(n[5])
                  p.remove(i)
          preped2 = sum(preped1)
        print('Done!')
        return preped2

      preped = prep(symbolprice)
      cooked= (mainframe(symbolprice,preped,workingamount))
      cookedp = []
      cat = 0
      for i in cooked:
        cat += 1
        cookedp.append([cat,i[1],i[2],i[3],i[4],i[6],i[8]])
      print (tt.to_string(cookedp,header=["Lp.", "Symbol",'Price','\033[4m'+'\033[36m'+'\033[1m'+"Amount"+'\033[0m','\033[4m'+'\033[1m'+'Valiue'+'\033[0m','lotmax',"Availabilty"],style=tt.styles.ascii_thin_double,))
      print('')
      print("Toral valiue: "+str(tsum(cooked)))
      print("Amount to distribute: "+str(workingamount))
      print("Amount left after purchase: "+str(Decimal(workingamount) - tsum(cooked)))
      print('')
      print(mathinfo)
      print('')
      if (tsum(cooked) == 0E-48) or (tsum(cooked) == 0) or (cooked == []):
        print('empty, restart')
        baseiccomands('r')
      if wait:
        print('\033[96m'+'Wating enebled!'+'\033[0m' '\n' 'In the buing phaze the program will sleap for the specifird amount of time.','\n','\n')
        print('')
      if unknowncomand:
        print('\033[91m'+'Comand not recognised!'+'\033[0m')
        print('')
        unknowncomand = False
      print (basiccomands)
      input3 = san(input("<comands - "+ comands +"> "))
      baseiccomands(input3)

      if input3 == "":
        break
      elif input3 == 'w':
        wait = not wait
      else:
        index = input3.split(',')
        for i in index:
          try:
            a = int(i)
            for i in symbolprice[:]:
              if i[0] == a:
                 symbolprice.remove(i)
          except:
            unknowncomand = True 
    #buyng symbols
    stage1 = []
    for i in cooked:
     stage1.append(['',i[1],''])
    renumber(stage1)
    stage2,stage2b = datafeching(stage1)
    for i in stage2[:]:
      if (i[2] == 'Not found') or((i[6][0] == '\033[92m'+'OPEN'+'\033[0m') and (i[6][1] <= 100000)):
        stage2.remove(i)
      if (i[8] == '\033[91m'+'CLOSED'+'\033[0m') and (wait == False):
        stage2.remove(i)
    if stage2 == []:
      print('empty, restart')
      baseiccomands('r')
    stage3 = prep(stage2)
    stage4 = mainframe(stage2,stage3,workingamount)
    for i in stage4[:]:
      if (i[3] == 0) or (i[3] == 0E-48):
        stage4.remove(i)
    if stage4 == []:
      print('empty, restart')
      baseiccomands('r')
    for i in stage4[:]:
      while i[3] > i[6]:
        r = i[3] - i[6]
        i[3] = i[6]
        stage4.append(i)
        i[3] = r
    buylistp1 = []
    buylistp2 = []
    for i in stage4[:]:
      if i[8] == '\033[92m'+'OPEN'+'\033[0m':
        buylistp1.append([i[1],i[3],i[5]])
      if i[8] == '\033[91m'+'CLOSED'+'\033[0m':
        buylistp2.append([i[1],i[3],i[5],i[9]])
    buylistp2.sort(reverse= False,key=lambda x: x[3])
    API = XTB(ID, Password,real)
    API.login()
    ID = ''
    Password = ''
    results = []
    if buylistp1 != []:
      for i in buylistp1:
        a = i[1]
        done = True
        while True:
          status, order_code = API.make_Trade(i[0], 0, 0, float(a))
          status = API.check_Trade(order_code)
          print(status)
          time = 0
          while status == 1:
            time += 1
            status = API.check_Trade(order_code)
            if time > 10:
              break
          if done:
            if (status == 0) or (status == 4):
              a = Decimal(a) - Decimal(i[2])
              if a == Decimal(0):
                done = False
          else:
            print(f'Buying: {i[0]} - {a} - {order_code} - {status}')
            results.append([i[0], a,i[1], order_code, status])
            break
          if (i[1] == 0) or (i[1] == 0E-48):
            status = 'faled to buy eny amount'
            print(f'Buying: {i[0]} - {a} - {order_code} - {status}')
            results.append([i[0], a,i[1], order_code, status])
            break
          API.ping()
    h = 0
    if buylistp2 != []:
      for i in buylistp2:
        t = float(i[3]-h)
        if t  > 0:
          print (f'Sleping for {t/1000}s')
          time.sleep(round(t/1000))
          h = h + i[3]
        a = i[1]
        while True:
          status, order_code = API.make_Trade(i[0], 0, 0, float(a))
          status = API.check_Trade(order_code)
          time = 0
          while status == 1:
            time += 1
            status = API.check_Trade(order_code)
            if time > 10:
              break
          if (status == 0) or (status == 4) and (a != 0):
            a = Decimal(a) - Decimal(i[2])
          else:
            print(f'Buying: {i[0]} - {a} - {order_code} - {status}')
            results.append([i[0], a,i[1], order_code, status])
            break
          if (i[1] == 0) or (i[1] == 0E-48):
            status = 'faled to buy any amount'
            print(f'Buying: {i[0]} - {a} - {order_code} - {status}')
            results.append([i[0], a,i[1], order_code, status])
            break
          API.ping()
    API.logout()
    clear()
    print('')
    print('Thank you for using this app!')
    print('')
    if results != []:
      print(tt.to_string(results,header=['Ticker',"Bought","Planed",'order_code','Status'],style=tt.styles.ascii_thin_double,))
      print(""" 
        ERROR - 0 - error.
        ENDING - 1 - pending.
        CCEPTED - 3 - The transaction has been executed successfully.
        REJECTED - 4 - The transaction has been rejected.""")
    else:
      print("Sadly nothing was percused...")
    
main()

