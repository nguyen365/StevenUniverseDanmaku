import sfml

def SpriteCopy(original) :
  copy = sfml.Sprite(original.texture, original.texture_rectangle)
  return copy