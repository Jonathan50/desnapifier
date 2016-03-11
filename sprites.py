# Copyright (C) 2016 Jeandre Kruger
#
# This file is part of screchifier.
#
# screchifier is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# screchifier is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with screchifier.  If not, see <http://www.gnu.org/licenses/>.

import kurt

def convert_sprite(sprite, scratch_project):
    scratch_sprite = kurt.Sprite(scratch_project, sprite.attrib["name"])
    scratch_project.sprites.append(scratch_sprite)
