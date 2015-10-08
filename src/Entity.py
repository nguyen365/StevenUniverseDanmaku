import sfml

class Entity :
  def __init__(self, Start, Sprite, CollisionRadius, Name="") :
    self.Sprite = Sprite
    self.x = Start[0]
    self.y = Start[1]
    self.Sprite.origin = (self.Sprite.local_bounds.right / 2, self.Sprite.local_bounds.bottom / 2)
    self.Sprite.position = sfml.Vector2(self.x, self.y)
    self.CollisionRadius = CollisionRadius
    self.Name = Name
  
  def draw(self, target, states) :
    target.draw(self.Sprite)
  
  def Move(self, iX, iY) :
    self.x = self.x + iX
    self.y = self.y + iY
    self.Sprite.position = sfml.Vector2(self.x, self.y)
    
  def MoveTo(self, iX, iY) :
    self.x = iX
    self.y = iY
    self.Sprite.position = sfml.Vector2(self.x, self.y)
    
  def CheckIntersectionWith(self, target) :
    if (self.CollisionRadius - target.CollisionRadius)**2 <= (self.x - target.x) ** 2 + (self.y - target.y) ** 2 and (self.x - target.x) ** 2 + (self.y - target.y) ** 2 <= (self.CollisionRadius + target.CollisionRadius)**2 :
      return True
    return False
