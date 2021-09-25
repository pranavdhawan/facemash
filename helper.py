import instaloader
from instaloader import Profile
import csv

#function puts the username, and dp url of the followers in a csv file for a provided account

def main(username):
    L = instaloader.Instaloader()
    L.login("pranavdhawan4", "itsanewpassword")
    c= 1
    profile = Profile.from_username(L.context, username)

    with open('followers_list.csv', mode='w') as followers_file:
        followers_writer = csv.writer(followers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        print("Writing data in csv file..\n")
        for follower in profile.get_followers():
            followers_writer.writerow([c, follower.username, follower.profile_pic_url])

            print(f"{follower.username}'s data stored.")
            c += 1
    
    print('Alright, done.')

if __name__ == '__main__':
    username = input("Enter username: ")
    main(username)