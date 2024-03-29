import instaloader
from instaloader import Profile
import csv

#function puts the username, and dp url of the followers in a csv file for a provided account

def main(username):
    L = instaloader.Instaloader()
    L.login("batman5honeysingh", "applemango")
    c= 1
    profile = Profile.from_username(L.context, username)

    with open('followers_list.csv', mode='w') as followers_file:
        followers_writer = csv.writer(followers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        print("Writing data in csv file..\n")
        for follower in profile.get_followers():
            #if c > :
            try:
                followers_writer.writerow([c, follower.username, follower.profile_pic_url])

                print(f"{follower.username}'s data stored.")
            except:
                print(f"{follower.username}'s data wasn't stored :(\n\nc={c}")
            c += 1

            #READ THIS:
            #if the program stops at any time due to any error, uncomment line 18 and place the number printed in the console.
            #Also, indent the next lines so the program works. Keep c+=1 out of the if loop.
    
    print('Alright, done.')

if __name__ == '__main__':
    username = input("Enter username: ")
    main(username)