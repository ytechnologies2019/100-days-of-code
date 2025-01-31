class User:
    def __init__(self , id , username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self , user):
        user.followers += 1
        self.following += 1


user1 = User("01" , "user01")
user2 = User("02","user02")

print (user1.id , user1.username)
print (user2.id , user2.username)

print (user1.follow(user2))
print (user1.followers)
print (user1.following)
print (user2.followers)
print (user2.following)