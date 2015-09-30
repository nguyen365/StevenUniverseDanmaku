import sfml

class Entity :
  def __init__(self, Start, Sprite, CollisionRadius = 1) :
    self.Sprite = Sprite
    self.x = Start[0]
    self.y = Start[1]
    self.Sprite.origin = (self.Sprite.local_bounds.right / 2, self.Sprite.local_bounds.bottom / 2)
    self.Sprite.position = sfml.Vector2(self.x, self.y)
    self.CollisionRadius = CollisionRadius