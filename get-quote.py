def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])

if __name__== "__primary__":
  primary()
  
git add get-quote.py
git commit -m "Renamed the primary function"
git push
