import sfml

class Bullet :
  def __init__ (self, Start, Sprite, Radius, Name="") :
    #Initial Coordintes (do not modify)
    self.Name = Name
    self.iX = Start[0]
    self.iY = Start[1]
    self.X = self.iX
    self.Y = self.iY
    self.Sprite = Sprite
    self.Radius = Radius
  def Update(self, dt) :
    self.T = self.T + dt
    self.X = self.iX + self.PEq[0](self.T)
    self.Y = self.iY + self.PEq[1](self.T)
    
class BulletPatter :
  def __init__ (self) :
    self.BulletList = []
    
    