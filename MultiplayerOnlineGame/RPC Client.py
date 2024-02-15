class GameClient:
    def __init__(self, server, player_id):
        self.server = server  # Reference to the RPC server
        self.player_id = player_id  # Unique identifier for the player

    def login(self):
        # Simulate an RPC call for player login
        self.server.login_player(self.player_id)

    def request_match(self, other_player_id):
        # Simulate an RPC call to request a new match
        self.server.start_match(self.player_id, other_player_id)

    def send_game_action(self, action):
        # Simulate an RPC call to send a game action
        self.server.play_game(self.player_id, action)

# Simulating two clients connecting to the game server
player1 = GameClient(game_server, 'Player1')
player2 = GameClient(game_server, 'Player2')

# Players log into the game server
player1.login()
player2.login()

# Player 1 requests a match with Player 2
player1.request_match('Player2')

# Simulate game play with RPC calls for actions
player1.send_game_action('move_forward')
player2.send_game_action('shoot_arrow')
# ... and so on

# The server would process these actions and continuously update the game state
