# Copyright (C) 2016 Jeandre Kruger
#
# This file is part of desnapifier.
#
# desnapifier is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# desnapifier is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with desnapifier.  If not, see <http://www.gnu.org/licenses/>.

import kurt
import scripts

def convert_sprite(sprite, scratch_project):
    print "Converting sprite %s..." % sprite.attrib["name"]

    scratch_sprite = kurt.Sprite(scratch_project, sprite.attrib["name"])

    print "> Converting scripts..."
    snap_scripts = None
    for child in sprite:
        if child.tag == "scripts":
            snap_scripts = child
    if snap_scripts == None:
        raise Exception("scripts is None!")
    scratch_sprite.scripts = scripts.convert_scripts(snap_scripts)

    scratch_project.sprites.append(scratch_sprite)
