#Helper functions we don't want in main file to keep it clean.

#function to get followers
import instaloader
from instaloader import Profile
def followers_list(username):
    L = instaloader.Instaloader()
    L.login("pranavdhawan4", "itsanewpassword")

    profile = Profile.from_username(L.context, username)
    print(f"{username} is followed by these profiles: ")
    for follower in profile.get_followers():
        print(follower.username)

def get_dp_url(username):
    L = instaloader.Instaloader()
    L.login("pranavdhawan4", "itsanewpassword")

    profile = Profile.from_username(L.context, username)
    print(profile.profile_pic_url)