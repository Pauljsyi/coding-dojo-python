class Player():
    new_team = []
    new_list = []
    def __init__(self, params):
        self.name = params["name"]
        self.age = params["age"]
        self.position = params["position"]
        self.team = params["team"]
    def info(self):
      print()
      print(self.name)
      print(self.age)
      print(self.position)
      print(self.team)
      return self
    
    @classmethod
    def populate_list(self, roster):
      # print(players)
      for i in range(len(roster)):
        # print(roster[i])
        self.new_team.append(roster[i])
      return self.new_team
    
    @classmethod
    def get_team(cls,new_team):
      for i in range(len(new_team)):
        # print("get_team function: ", new_team[i])
        cls.new_list.append(new_team[i])
        
      return cls.new_list

    def __repr__(self):
      display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
      return display

kevin = {
  "name": "Kevin Durant", 
  "age":34, 
  "position": "small forward", 
  "team": "Brooklyn Nets"
}
jason = {
  "name": "Jason Tatum", 
  "age":24, 
  "position": "small forward", 
  "team": "Boston Celtics"
}
kyrie = {
  "name": "Kyrie Irving", 
  "age":32,
  "position": "Point Guard", 
  "team": "Brooklyn Nets"
}


players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]



# Create your Player instances here!
# player_jason = ???


player_paul = Player(kyrie)
# player_paul.populate_list(players)
player_paul.get_team(player_paul.populate_list(players))
print('new list:   ...   ',player_paul.new_list)

# print(player_paul.name)
# print(player_paul.age)
# print(player_paul.position)
# print(player_paul.new_team)


print(player_paul.__repr__())