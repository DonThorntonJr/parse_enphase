import sys
import requests
from bs4 import BeautifulSoup
url = sys.argv[1]
# print ( url )
re0 = requests.get ( url )
bs0 = BeautifulSoup(re0.content,"html.parser")
# print(bs0.prettify())
table = bs0.find_all ( "table" )[2]
# print ( table.text )
sys.stdout.write ( "{\n" )
sys.stdout.write ( "  \"prtg\":\n" )
sys.stdout.write ( "  {\n" )
for row in table.find_all('tr'):
	col = row.find_all('td')[0]
	val = row.find_all('td')[1]
	if col.text == "Currently generating":
		sys.stdout.write ( "      \"result\": [\n" )
		sys.stdout.write ( "        {\n" )
		sys.stdout.write ( "          \"channel\": \"Currently Generating (W)\",\n" )
		if val.text.split( )[1] == "kW":
			sys.stdout.write ( "            \"value\": \"%d\"\n" % int ( float ( val.text.split( )[0] ) * 1000 ) )
		else:
			sys.stdout.write ( "            \"value\": \"%d\"\n" % int ( float ( val.text.split( )[0] ) ) )
		sys.stdout.write ( "        },\n" )
	if col.text == "Number of Microinverters Online":
		sys.stdout.write ( "        {\n" )
		sys.stdout.write ( "          \"channel\": \"%s\",\n" % "Number of Microinverters Online" )
		sys.stdout.write ( "            \"value\": \"%d\"\n" % int ( val.text ) )
		sys.stdout.write ( "        }\n" )
		sys.stdout.write ( "      ]\n" )
		sys.stdout.write ( "  }\n" )
		sys.stdout.write ( "}\n" )
sys.stdout.flush ( )
