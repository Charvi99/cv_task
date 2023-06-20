from elftools.elf.elffile import ELFFile
import os
from pathlib import Path
import sys
        
def loadArguments(argv):    
    '''
        Load and check arguments
        ------------------------
        Params:
            argv : list of strings
        Return:
            elf_files : list of paths
    '''
    elf_files = []
    
    # argument check
    if len(argv) > 1:
        for arg in argv[1:]:
            path = Path(arg)
            
            # if path is file
            if path.is_file():
                    try:
                        if path.suffix == '.elf':
                            elf_files.append(path)
                    except:
                        print("Argument: " +  "is not path to .ELF file")

            # if path is dir            
            elif path.is_dir():
                try:
                    for path_indir in os.scandir(path):
                        if path_indir.name.endswith('.elf'):
                            elf_files.append(path_indir)
                except:
                    print("Directory " + path.name + " has not been found")
    else:
        print("Missing arguments, enter at least one path to .ELF file or directory with .ELF file")
    
    return elf_files
 
                      
def proccessFiles(elf_files):
    '''
    Inspect atributes of .ELF files from input argument
    ------------------------
    Params:
        elf_files : list of paths
    Return:
        err : count of fails
    '''
    
    err = 0
    # Table template setup
    template = "{0:4}|{1:7}|{2:10}|{3:12}|{4:11}" # column widths: 8, 10, 15, 7, 10

    for path in elf_files:
        print('File: ', path.name)
        
        try:
            file = open(path, 'rb')
            elffile = ELFFile(file)
            
            # print header of table
            print(template.format("NO.", "TYPE", "OFFSET", "SIZE IN FILE", "SIZE IN MEM"))
            
            # print atributes of each segment in file 
            for i in range(elffile.num_segments()):
                seg = elffile.get_segment(i)
                print(template.format('['+ str(i) + ']', seg.header.p_type, seg.header.p_offset, seg.header.p_filesz, seg.header.p_memsz)) # header          
            elffile.close()
        except:
            print("File " + str(path) + "failed to open")
            err = err + 1
    return err

def main(argv):
    print("===============================================")
    print("ELFTool script")
    print("===============================================")
    elf_files = loadArguments(argv)
    
    if elf_files.count == 0:
        print("No .ELF files have not been provided")
        exit() 
        
    err = proccessFiles(elf_files)
    if err > 0:
        print(err + " files faild to open")
    print("===============================================")

if __name__ == '__main__':
    main(sys.argv)
        
        
