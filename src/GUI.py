import sfml

LifeSize = (9,9)
BombSize = (9,9)

class GUI (sfml.TransformableDrawable) :
  def __init__(self, iGame, visible = False) :
    sfml.Drawable.__init__(self)
    self.Game = iGame
    #self.Screen = sfml.View()
    #self.Screen.size = self.Game.Window.size
    #self.Screen.center = self.Game.Window.size * 0.5
    #self.Screen.move(self.Game.Window.size.x * -0.75, self.Game.Window.size.y * -0.30)
    self.Visible = visible
    self.position = (600,200)
    self.ObjectList = []
    self.LifeList = []
    self.BombList = []
    self.Borders = []
    
    BackgroundTop = sfml.RectangleShape((self.Game.Window.size.x, 30))
    BackgroundTop.fill_color = sfml.Color(20,20,20)
    self.Borders.append(BackgroundTop)
    BackgroundLeft = sfml.RectangleShape((30, self.Game.Window.size.y))
    BackgroundLeft.fill_color = sfml.Color(20,20,20)
    self.Borders.append(BackgroundLeft)
    BackgroundRight = sfml.RectangleShape((self.Game.Window.size.x - 530, self.Game.Window.size.y))
    BackgroundRight.fill_color = sfml.Color(20,20,20)
    BackgroundRight.position = (530,0)
    self.Borders.append(BackgroundRight)
    BackgroundTop = sfml.RectangleShape((self.Game.Window.size.x ,self.Game.Window.size.y - 580))
    BackgroundTop.fill_color = sfml.Color(20,20,20)
    BackgroundTop.position = (0, 580)
    self.Borders.append(BackgroundTop)
    
    LifeText = sfml.Text("Life", self.Game.AssetManager.Fonts["Crewniverse"], 20)
    LifeText.position = (0,0)
    LifeText.color = sfml.Color.WHITE
    self.ObjectList.append(LifeText)
    
    BombText = sfml.Text("Bomb", self.Game.AssetManager.Fonts["Crewniverse"], 20)
    BombText.position = (0,40)
    BombText.color = sfml.Color.WHITE
    self.ObjectList.append(BombText)
    
    ScoreText = sfml.Text("Score", self.Game.AssetManager.Fonts["Crewniverse"], 20)
    ScoreText.position = (0,80)
    ScoreText.color = sfml.Color.WHITE
    self.ObjectList.append(ScoreText)
    
    ScoreNum =  sfml.Text("0123456789", self.Game.AssetManager.Fonts["Atari"], 12)
    ScoreNum.position = (ScoreText.local_bounds.center.x - ScoreNum.local_bounds.width / 2 ,110)
    ScoreNum.color = sfml.Color.WHITE
    self.ObjectList.append(ScoreNum)
    
    for i in range(2) :
      Life = self.Game.AssetManager.GetBullet("Default_Violet")
      Life.position = (LifeText.position.x + i * 12, LifeText.position.y + 30)
      self.LifeList.append(Life)
      
    for i in range(3) :
      Bomb = self.Game.AssetManager.GetBullet("Default_Violet")
      Bomb.position = (BombText.position.x + i * 12, BombText.position.y + 30)
      self.BombList.append(Bomb)
      
      
  def draw(self, target, states) :
    if self.Visible is False :
      return
    #self.Game.Window.view = self.Screen
    for Background in self.Borders :
      target.draw(Background, states)
    for Obj in self.ObjectList :
      Obj.position = Obj.position + self.position
      target.draw(Obj, states)
      Obj.position = Obj.position - self.position
    for Life in self.LifeList :
      Life.position = Life.position + self.position
      target.draw(Life, states)
      Life.position = Life.position - self.position
    for Bomb in self.BombList :
      Bomb.position = Bomb.position + self.position
      target.draw(Bomb, states)
      Bomb.position = Bomb.position - self.position
    
  def Draw(self) :
    if self.Visible is False :
      return
    #self.Game.Window.view = self.Screen
    for Obj in self.ObjectList :
      self.Game.Window.draw(Obj)
    for Life in self.LifeList :
      self.Game.Window.draw(Life)
    for Bomb in self.BombList :
      self.Game.Window.draw(Bomb)
  
  def UpdateLife(self, Change) :
    pass
  
  def UpdateBomb(self, Change) :
    pass
  
  def UpdateScore(self, Change) :
    pass
  
    
    