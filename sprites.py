import kurt

def convert_sprite(sprite, scratch_project):
    scratch_sprite = kurt.Sprite(scratch_project, sprite.attrib["name"])
    scratch_project.sprites.append(scratch_sprite)
