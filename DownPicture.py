from requests import session
import urllib.request

s = session()

# get token by link: https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed 
accessToken = 'EAAA...' # code token

# set id
id = '501097147704503'

# set the number of downloads
sum = '200'

#get all link pictures
data = s.get('https://graph.facebook.com/'+id+'?fields=feed.limit('+sum+'){full_picture}&access_token='+accessToken)

#get link picture and download
for i in range(0, int(sum)):
    dataPicture = data.json()['feed']['data'][i]
    if 'full_picture' in dataPicture:
        print(i+1)
        print("=============")
        link = dataPicture['full_picture']
        urllib.request.urlretrieve(link, "D:/picture/img" + str(i+1) + ".jpg")
