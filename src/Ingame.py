import sfml
from GameState import GameState
from Player import Player

class GameData :
  def __init__(self) :
    self.PlayerLife = 2
    self.PlayerBomb = 3
    self.Focus = False
    self.PlayerCoor = sfml.Vector2(100,400)
    self.Clock = sfml.Clock()
    self.TimeToMove = sfml.milliseconds(45)
    self.EnemyList = []
    self.Boss = None
    self.Bounds = sfml.Rectangle((30,30),(500,550))
    self.BulletList = []
  
  def MovePlayer(self, Direction) : #Direction is a (x,y) pair
    if self.CheckTime() is False :
      return self.PlayerCoor
    NewCoor = None
    if self.Focus is True :
     NewCoor = self.PlayerCoor + sfml.Vector2(Direction[0], Direction[1]) * 2.5
    else :
      NewCoor = self.PlayerCoor + sfml.Vector2(Direction[0], Direction[1]) * 5
    if self.Bounds.contains(NewCoor) is True :
       self.PlayerCoor = NewCoor
    return self.PlayerCoor
  
  def CheckCollisions(self) :
    for Enemy in self.EnemyList :
      if abs(Enemy.CollisionRadius - self.Player.CollisionRadius)**2 <= (Enemy.x - self.Player.x) ** 2 + (Enemy.y - self.Player.y) ** 2 and (Enemy.CollisionRadius + self.Player.CollisionRadius)**2 >= (Enemy.x - self.Player.x) ** 2 + (Enemy.y - self.Player.y) ** 2 :
        return Enemy
    for Bullet in self.BulletList :
      if abs(Bullet.CollisionRadius - self.Player.CollisionRadius)**2 <= (Bullet.x - self.Player.x) ** 2 + (Bullet.y - self.Player.y) ** 2 and (Bullet.CollisionRadius + self.Player.CollisionRadius)**2 >= (Bullet.x - self.Player.x) ** 2 + (Bullet.y - self.Player.y) ** 2 :
        return Bullet
    return None
  
  def CheckTime(self) :
    if self.Clock.elapsed_time < self.TimeToMove :
      return False
    self.Clock.restart()
    return True
    

class InGame(GameState) :
  def __init__(self, iGame) :
    super().__init__(iGame)
    self.Screen.size = self.Game.Window.size
    self.Screen.center = self.Game.Window.size * 0.5
    self.PlayerSprite = Player(self.Game.AssetManager.GetSprite("Steven"), self.Game.AssetManager.GetBullet("Default_Purple"))
    self.Data = GameData()
    self.Background = sfml.RectangleShape((500,550))
    self.Background.position = (30,30)
    self.Background.outline_color = sfml.Color.WHITE
    self.Background.fill_color = sfml.Color.BLACK
  
  def Draw(self) :
    self.Game.Window.draw(self.Background)
    self.Game.Window.draw(self.PlayerSprite)
  
  def Update(self, dt) :
    pass
  
  def HandleInputs(self) :
    if sfml.Keyboard.is_key_pressed(sfml.Keyboard.L_SHIFT) :
      self.Data.Focus = True
      self.PlayerSprite.Focus = True
    else :
      self.Data.Focus = False
      self.PlayerSprite.Focus = False
          
    if sfml.Keyboard.is_key_pressed(sfml.Keyboard.Z) :
      if self.PlayerSprite.Focus is True :
        pass
      else :
        pass
        
    MovementVector = sfml.Vector2(0,0)
    if sfml.Keyboard.is_key_pressed(sfml.Keyboard.X) :
      pass
        
    if sfml.Keyboard.is_key_pressed(sfml.Keyboard.UP) :
      MovementVector += (0,-1)
          
    if sfml.Keyboard.is_key_pressed(sfml.Keyboard.DOWN) :
       MovementVector += (0,1)
          
    if sfml.Keyboard.is_key_pressed(sfml.Keyboard.LEFT) :
       MovementVector += (-1,0)
          
    if sfml.Keyboard.is_key_pressed(sfml.Keyboard.RIGHT) :
       MovementVector += (1,0)
          
    if sfml.Keyboard.is_key_pressed(sfml.Keyboard.ESCAPE) :
      pass
    
    self.MovePlayer(MovementVector)
    for event in self.Game.Window.events :
      if type(event) is sfml.CloseEvent :
        self.Game.Window.close()
        exit(0)
  
  def MovePlayer(self, Direction) :
    self.PlayerSprite.MoveTo(self.Data.MovePlayer(Direction))
    
        