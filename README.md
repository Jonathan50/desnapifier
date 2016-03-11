# desnapifier
Convert [Snap*!*](http://snap.berkeley.edu) projects to [Scratch](http://scratch.mit.edu) by MIT.
## Dependencies
desnapifier depends on [Kurt](http://github.com/tjvr/kurt) by blob8108.
## Usage
```
python2 desnapifier.py infile.xml outfile.sb2
```
For example:
```
python2 desnapifier.py test.xml test.sb2
```
This will convert the Snap*!* project `test.xml` and output it to `test.sb2`
## Adding blocks
To add a block, simply add a new entry in `blocks.py`.  
An entry looks like the following:
```py
    "snapIdentifier": [ "scratchOpcode", argCount, makeBlockFn ],
```
`snapIdentifier` is the identifier Snap*!* uses to identify the block.  
`scratchOpcode` is the opcode of the Scratch block, or None if there is no Scratch equivilant.  
`makeBlockFn` is a function that should return a `kurt.Block`, or `None`. Use this only if there is no direct Scratch equivilant to the block.
For example:
```py
    "doSayFor":   [ "say:duration:elapsed:from:", 2, None ],
```
Find a full list of Scratch block opcodes at https://github.com/LLK/scratch-flash/blob/master/src/Specs.as.
## Status
desnapifier is currently only able to convert very simple Snap*!* projects.  
See `test.xml` for an example.  
See [TODO.md](http://github.com/Jonathan50/desnapifier/blob/master/TODO.md) for a list of \(most of?\) what needs to be done.
## Copyright
desnapifier is Copyright &copy; 2016 Jeandre Kruger.  
desnapifier is [Free Software](http://gnu.org/philosophy/free-sw.html) licensed under the GNU General Public License version, either version 3 of the license, or \(at your option\) any later version.
