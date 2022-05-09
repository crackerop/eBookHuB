def login(userid, password, flag):
  ui = input("USER ID:")
  if ui == userid.strip():
    pw = input("password:")
    if pw == password:
      if flag == 0:
        manager()
      else:
        customer()
    else:
      print('\nSorry, Passwords do not match')
      mainmenu()
  else:
    print('\nInvalid username')
    mainmenu()

def customer():
    print('\n1 View Movie and Timings \n2 View Seat Prices \nPress any key to exit')
    ch = input("\nEnter your choice: ")
    if ch == '1':
       print('\n\n   Movies                          Timings\n\n1 ATRANGI RE                     [1]10 AM [2]4 PM\n\n2 Spiderman-NWH                  [1]4 PM  [2]10 PM\n\n3 PUSHPA-THE RISE[PART(1)        [1]11 AM [2]9 PM \n\n4 KINGSMAN-THE GOLDEN CIRCLE     [1]1 PM  [2]6 PM')
    elif ch == '2':
      print('\nRow 1 and 2 : RS 350\nRow 3 to 6 : RS 250\nRow 6 to 15 : RS 150')
    else:
      exit()
    ch = input("\nPress 1 to go back \nPress any key to exit\nEnter your choice: ")
    if ch == '1':
      customer()
    else:
      exit()
         
def ticket(movie,time):
  Booked_seat = 0
  prize_of_ticket = 0
  Total_Price = 0
  Row = 1
  Seats = 15
  Total_seat = Row*Seats
  bookedseatst1=0
  bookedseatst2=0
  bookedseatst3=0
  bookedseats = bookedseatst1 + bookedseatst2 + bookedseatst3
  if movie == 1:
    if time == 1:
      bsfile='bookedseatATRANGI1.txt'
      movieTime="TIME: 10 AM"
    else:
      bsfile='bookedseatATRANGI2.txt'
      movieTime="TIME: 4 PM"
    sdfile = 'ATRANGI.txt'
    mailfile = 'Atrangimail.txt'
    movieName = "MOVIE: ATRANGI RE "
  elif movie == 2:
    if time == 1:
      bsfile='bookedseatSPDNWH1.txt'
      movieTime="TIME: 4 PM"
    else:
      bsfile='bookedseatSPDNWH2.txt'
      movieTime="TIME: 10 PM"
    sdfile = 'SPDNWH.txt'
    mailfile = 'SPDNWHmail.txt'
    movieName = "Spiderman-NWH"
  elif movie == 3:
    if time == 1:
      bsfile='bookedseatPUSHPA1.txt'
      movieTime="TIME: 11 AM"
    else:
      bsfile='bookedseatPUSHPA2.txt'
      movieTime="TIME: 9 PM"
    sdfile = 'PUSHPA.txt'
    mailfile = 'PUSHPAmail.txt'
    movieName = "PUSHPA-THE RISE[PART(1)"
  elif movie == 4:
    if time == 1:
      bsfile='bookedseatKG1.txt'
      movieTime="TIME: 1 PM"
    else:
      bsfile='bookedseatKG2.txt'
      movieTime="TIME: 6 PM"
    sdfile = 'KINGSMAN.txt'
    mailfile = 'KINGSmail.txt'
    movieName = "KINGSMAN-THE GOLDEN CIRCLE"

  finish='yes'
  while finish =='yes':
    import sys
    c = 0
    Row_number = int(input('\nEnter Row Number - \n'))
    Column_number = int(input('\nEnter Column Number - \n'))
    bookedseat=(Row_number , Column_number)
    bs = open(bsfile, 'r')
    line = 0
    while True:
      line = line + 1  
      s = bs.readline().strip('\n')
      if s == (str(bookedseat)):
        c=c+1
        break
      if not s:  
        break
    if c>0:
      print("\n\nALREADY BOOKED")
      c = 0
    else:
      print("\n\nSUCCESS") 
      pricet1= 350
      pricet2=250
      pricet3=150
      prize_of_ticket1=0
      prize_of_ticket2=0
      prize_of_ticket3 =0
      f = open(bsfile, 'a')
      f.write(str(bookedseat))
      f.write("\n")
      f.close()
      sd = open(sdfile,'a')
      y = sd.write(str(bookedseat))
      sd.write("\n")
      sd.close()
      ag = open(mailfile,'a')
      ag.write(str(bookedseat))
      ag.write("\n")
      ag.close()
      if Row_number in range(15) and Column_number in range(15):
        if Row_number<=2 and Column_number <=15:
          bookedseatst1= bookedseatst1+1
          prize_of_ticket2 = (pricet2 * bookedseatst2)
          prize_of_ticket3 = (bookedseatst3 * pricet3)
          prize_of_ticket1= (pricet1*bookedseatst1) + prize_of_ticket3 + prize_of_ticket2
          print('prize_of_ticket - ', 'RS', prize_of_ticket1) 
        elif Row_number>2 and Row_number<=6 and Column_number<=15:
          prize_of_ticket1= (pricet1*bookedseatst1)
          prize_of_ticket3 = (bookedseatst3 * pricet3)
          bookedseatst2=bookedseatst2+1
          prize_of_ticket2 = (pricet2 * bookedseatst2)+ prize_of_ticket1 + prize_of_ticket3
          print('prize_of_ticket - ', 'RS', prize_of_ticket2)
        else:
          bookedseatst3 = bookedseatst3+1
          prize_of_ticket1= (pricet1*bookedseatst1)
          prize_of_ticket2 = (pricet2 * bookedseatst2) 
          prize_of_ticket3 = (bookedseatst3 * pricet3) + prize_of_ticket1 + prize_of_ticket2
          print('Total cost - ', 'RS', prize_of_ticket3)    
      finish = input('\n\n"yes" for more booking and "no" for stop booking - ')
      if finish == "no":
       name=input('\nEnter name:')
       while(1):
         mobile= int(input("\nEnter phone number:"))
         if mobile>6000000000 and mobile<9999999999:
           break
         else:
           print("##########Invalid phone number##########")
       while(1):
         emailadd=input("\nEnter email address(gmail):")
         import re
        # email_pattern = r'\b^[a-z0-9](\.?[a-z0-9]){5,}@gmail\.com$\b'
         
         if ( re.fullmatch(email_pattern, emailadd) ):
           break
         else:
           print("##########Invalid gmail id##########")
       
       
       t = movieTime
       mo = movieName
       price = max(prize_of_ticket1, prize_of_ticket2 ,prize_of_ticket3)
       N = "NAME:" ,name
       P = "MOBILE NUMBER:",mobile
       TP = "Total cost:", price
       ED = "Email:", emailadd

       ag = open(mailfile,'a')
       ag.write(str(mo))
       ag.write("\n")
       ag.write(str(t))
       ag.write("\n")
       ag.write(str(N))
       ag.write("\n")
       ag.write(str(P))
       ag.write("\n")
       ag.write(str(TP))
       ag.write("\n")
       ag.write(str(ED))
       ag.write("\n")
       ag.write("\n")
       ag.close()

       sd = open(sdfile,'a')
       sd.write(str(t))
       sd.write("\n")
       sd.write(str(N))
       sd.write("\n")
       sd.write(str(P))
       sd.write("\n")
       sd.write(str(TP))
       sd.write("\n")
       sd.write("\n")
       sd.close()
       mail(mailfile,emailadd)
        
                
def mail(mailfile,emailadd):
  import smtplib
  gmailaddress = "aucinemas@gmail.com"
  gmailpassword = "ahduni@cinemas"
  file = open(mailfile,'r+')
  msg = file.read()
  mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
  mailServer.starttls()
  mailServer.login(gmailaddress , gmailpassword)
  mailServer.sendmail(gmailaddress, emailadd , msg)
  print (msg)
  print(" \n  Booked Successfully!")
  mailServer.quit()
  file.truncate(0)
  file.close()

def manager():
  x = 10
  movie=0
  while x != 0:
    print('\n1 for Show the seats \n2 for Buy a Ticket  \n3 Exit')
    x = int(input('\nSelect Option - '))
    if x == 1:
      sa = open('seats arrangement.txt','r')
      print(sa.read())
      sa.close()
    elif x == 2:
        print("\n##########   Movies   ##########\n\n1 ATRANGI RE \n\n2 Spiderman-NWH \n\n3 PUSHPA-THE RISE[PART(1) \n\n4 KINGSMAN-THE GOLDEN CIRCLE ")
        movie = int(input("\nEnter movie number:"))
        if movie == 1:
          print("\n\n##########   Timings   ########## \n\n[1]10 AM \n\n[2]4 PM")
          time=int(input("\nEnter timing(number):"))
        elif movie == 2:
          print("\n\n##########   Timings   ########## \n\n[1]4 PM \n\n[2]10 PM")
          time=int(input("\nEnter timing(number):"))
        elif movie == 3:
          print("\n\n##########   Timings   ########## \n\n[1]11 AM \n\n[2]9 PM")
          time=int(input("\nEnter timing(number):"))
        elif movie == 4:
          print("\n\n##########   Timings  ########## \n\n[1]1 PM \n\n[2]6 PM")
          time=int(input("\nEnter timing(number):"))
        else:
          print("\n######## INVALID #############")
          break
        if time == 1 or time == 2:
          ticket(movie,time)
        else:
          print("\n######## INVALID #############")
          break
        
    
    else:
            print()
            print('\n***  THANK YOU  ***')
            print()
            exit()

def mainmenu():
  print('\n\n***** Welcome to AU Cinemas *****')
  print('\nEnter 1 for Manager Login \nEnter 2 for Customer Login \nEnter any other integer to exit')
  choice = int(input('\nEnter your choice: '))
  if choice == 1:
    f = open('login.txt','r')
    userid = f.readline()
    password= f.readline()
    login(userid, password, 0)
    f.close()
  elif choice == 2:
    f = open('customerlogin.txt','r')
    userid = f.readline()
    password= f.readline()
    login(userid, password, 1)
    f.close()
  else:
    print("\n#####exit######")
    exit()

mainmenu()

