from bs4 import BeautifulSoup
import urllib2
print "Enter Username :"
x=raw_input()
url="http://www.spoj.com/users/"
url=url+x
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
result = soup.find('div', {'class' :'col-md-3'}, id='user-profile-left').text
print result
