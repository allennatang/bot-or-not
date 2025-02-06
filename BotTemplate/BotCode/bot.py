from abc_classes import ABot
from teams_classes import NewUser, NewPost


class Bot(ABot):
    def create_user(self, session_info):
        # todo logic
        # Example:
        new_users = [
            NewUser(username="TestBot1", name="Allenna1", description="Hello I'm a bot"),
            
        ]
        return new_users

    def generate_content(self, datasets_json, users_list):
        # todo logic
        # It needs to return json with the users and their description and the posts to be inserted.
        # Example:
        posts = []
        bot_posts = [
    "Just finished my favorite book for the third time and I still can't get enough of the characters! What's a book you could read over and over? #BookLovers",
    "Just had the most epic coffee catch-up with an old friend. It's amazing how time flies, but the memories and laughter never fade. Grateful for these moments! What's the best catch-up you've had lately? #Friendship #CoffeeTalk",
    "Just discovered a hidden coffee shop in my neighborhood and wow, the vibe is incredible! Who knew a little caffeine could spark such joy? #HiddenGems #CoffeeLovers",
    "Just tried my hand at cooking a new recipe tonight and wow, I might have actually nailed it! Anyone else ever surprise themselves in the kitchen? #CookingAdventures #Homemade",
    "Just saw the most incredible sunset at the park! There's something magical about the sky turning all those brilliant colors. Perfect way to end the day. Hope everyone gets a moment to unwind tonight! #NatureLover #Grateful",
    "Just had the most amazing coffee shop experience. The barista learned my order on the second visit! That kind of personal touch makes all the difference. What's your favorite local spot? #CoffeeLovers #SupportLocal",
    "Just had the most amazing coffee at that little cafe on the corner. Perfect blend and the barista was super friendly! What's your favorite go-to spot for a caffeine boost? #CoffeeLovers #LocalCafes",
    "Just saw a kid confidently explain to their friend why broccoli is a dinosaur's favorite food. Kids really have the wildest imaginations! What's the funniest thing you've heard a child say lately? #KidLogic #Imagination",
    "Just finished a great book that had me completely hooked! Anyone else have recommendations for page-turners? I'm in the mood for something equally gripping! #BookRecommendations #ReadersCommunity",
    "Just tried that new cafe down the street, and their matcha latte is *chef's kiss*! Who knew a little green could taste so good? #CoffeeLover #LocalEats"
]
        for j in range(len(users_list)):
            for i in range(10):
                posts.append(NewPost(text=bot_posts[i], author_id=users_list[j].user_id, created_at='2024-03-17T00:20:30.000Z',user=users_list[j]))
        return posts
