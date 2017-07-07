# PES library development

Eventually this project will provide a library to read and write PES 1, 2 and 6.

However, 1 will be documented and implemented first.

For the time being, all that exists is a document being created that describes PES version 1.

Please, help with all UNK values in the document.


## Contents

 * [docs](./docs) Directory with information about the file format
 * [pes-files](./pes-files) Example files to test/analyze
 * [LibPes](./LibPes) PES library
   * [pesheader.py](./LibPes/pesheader.py) PES header class
 * [read-pes.py](./read-pes.py) Util to parse PES files. Usage: `python read-pes.py pes-files/minimalV6.pes`


## Plan for reverse-engineering

 1. Build a basic util to parse a PES file
 2. Collect PES files to test the implementation
 3. Run lib over as many files as possible, analyze results
 4. Try to understand 100% of file format
 5. Implement util to write PES files

