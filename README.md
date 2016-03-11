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
    "snapIdentifier": [ "scratchOpcode", argCount ],
```
For example:
```py
    "doSayFor":   [ "say:duration:elapsed:from:", 2 ],
```
Find a full list of Scratch block opcodes at https://github.com/LLK/scratch-flash/blob/master/src/Specs.as.
## Copyright
desnapifier is Copyright &copy; 2016 Jeandre Kruger.  
desnapifier is [Free Software](http://gnu.org/philosophy/free-sw.html) licensed under the GNU General Public License version, either version 3 of the license, or \(at your option\) any later version.
