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
import notsupported

class NotEnoughArgumentsError(Exception):
    pass

class TooManyArgumentsError(Exception):
    pass

def check_args(s, c):
    if i < c:
        raise NotEnoughArgumentsError("not enough arguments for %s block" % s)
    if i > c:
        raise TooManyArgumentsError("too many arguments for %s block" % s)

def get_args(snap_block):
    args_list = []
    for child in snap_block:
        if child.tag == "l":
            args_list.append(child.text)
    return tuple(args_list)

def convert_block(snap_block):
    scratch_block = None

    if not "s" in snap_block.attrib:
        raise Exception("block has no s attribute!")

    s = snap_block.attrib["s"]

    if s == "receiveGo":
        scratch_block = kurt.Block("whenGreenFlag")
    if s == "doSayFor":
        (say, secs) = get_args(snap_block)
        scratch_block = kurt.Block("say:duration:elapsed:from:", say, secs)

    # unknown block
    if scratch_block == None:
        raise notsupported.UnsupportedBlockError(s)

    return scratch_block

def convert_scripts(snap_scripts):
    scratch_scripts = []

    for script in snap_scripts.iter("script"):
        scratch_script = kurt.Script()
        for block in script:
            if block.tag == "block":
                scratch_script.append(convert_block(block))
        scratch_scripts.append(scratch_script)

    return scratch_scripts
