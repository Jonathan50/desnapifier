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

import os, kurt
from desnapifier import scripts, blocks

def test_all_blocks():
    scratch_block = None
    for key in blocks.blocks:
        if blocks.blocks[key][0] != None:
            args = [ "foo" ] * blocks.blocks[key][1]
            scripts.check_args(blocks.blocks[key][0], blocks.blocks[key][1], len(args))
            scratch_block = kurt.Block(blocks.blocks[key][0], *args)
        else:
            if blocks.blocks[key][2] == None:
                raise Exception("Both block[0] and block[2] are none!")
            scratch_block = blocks.blocks[key][2]()
