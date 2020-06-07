import vrcpy

def main():
    # Initialise vrcpy wrapper client and login with username + password
    client = vrcpy.Client()
    client.login("username", "password")

    # Get avatar via id
    a = client.fetch_avatar("avtr_fa5303c6-78d1-451c-a678-faf3eadb5c50")
    author = a.author() # Get author of the avatar
    print("Avatar '"+a.name+"' was made by "+author.displayName)
    ## This should print "Avatar 'Etoigne' was made by ***REMOVED***"

    # Close client session
    # Not needed unless you want to login again with this client object
    await client.logout()

if __name__ == "__main__":
    main()
