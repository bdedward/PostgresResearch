f = open('envlist', 'r')

#Pulls in image names from postgres list
images = [word.strip() for line in f.readlines() for word in line.split(',') if word.strip()]

count = 0;
imagename = ""
for x in range(len(images)):    
    tmpcount = len(open(images[x]).readlines(  ))
    if(tmpcount == 15):
        count = tmpcount
        imagename = images[x]
    print(count)
    

print("Largest env file is from image: " + images[x])

print("The number of env variables: ")
print(count)