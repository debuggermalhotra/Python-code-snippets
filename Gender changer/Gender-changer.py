dictionary={ "batman": "batwoman", "batwoman":"batman",
"boy":"girl", "girl":"boy",
"boyfriend":"girlfriend", "girlfriend":"boyfriend",
"father" : "mother", "mother":"father",
"husband":"wife", "wife":"husband",
"his":"her", "her":"his",
"he":"she","she":"he",
"male":"female", "female":"male",
"man":"woman", "woman":"man",
"Mr":"Ms","Mr":"Ms",
"sir":"madam", "madam":"sir",
"son":"daughter", "daughter":"son",
"uncle":"aunt","aunt":"uncle","him":"her","her":"him",
"brother":"sister","sister","brother"
,"actor":"actress","actress":"actor"}

string=raw_input("Enter a sentence: ")

list1=list()

list1=string.split()

for word in list1:
 flag=0
 
if word in dictionary:
   string=string.replace(word,dictionary[word])
print(string)