# ELF File reader
ELF File reader is tool for analysis Executable and Linkable Format files. 
It provides information of each segment about 
- type
- offset in memory
- size in file
- size in memory

## Usage
At first navigate into directory where script or executable file is located. Then:
- Run script with following command for python package: `python ELFTool [argument]`

 - Or run executable file with command: `ELFTool.exe [argument]`

 Argument is path (or paths) to .ELF file or directory with .ELF files inside. For multiple path input separate each argument with space.
 Input arguments must be at least one or more .ELF file or directory with one or more .ELF files.
 
## Instalation as python package
Clone repository and instal python package with command `pip install .` if you are in root directory. Or enter **pythonPackage** directory and use command `pip install ELFTool-0.1.tar.gz`

## Instalation as Windows executable
Clone repository and use **ELFTool.exe** executable file. 
