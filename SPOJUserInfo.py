from bs4 import BeautifulSoup
import urllib2 
print "Enter Username :"
x=raw_input()
url="http://www.spoj.com/users/"
url=url+x
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
print "    "
print "****************************"
print "    "
while soup.find('div', {'class' :'col-md-3'}, id='user-profile-left')==None:
	print "**Invalid Username**"
	print " " 
	print "Enter a valid username : "
	print "    "
	x=raw_input()
	url="http://www.spoj.com/users/"
	url=url+x	
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	print "    "
	print "-----------------------------"
	print "    "
result = soup.find('div', {'class' :'col-md-3'}, id='user-profile-left').text
print "   " 
print "fetching .. .... ......"
print "   "
print "Successful !"
print result
