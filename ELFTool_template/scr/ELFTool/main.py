from elftools.elf.elffile import ELFFile
import sys
import os
from pathlib import Path


if __name__ == '__main__':
    print("================")
    print("ELF File reader")
    print("================")
    
    elf_files = []
    sys.argv = [sys.argv[0], r"C:\Espressif\cv_task\elf_files", r"C:\Espressif\cv_task\elf_files\main.elf"]
    # argument check
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
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
    
    if elf_files.count == 0:
        print("No .ELF files have not been provided")
        exit()                

    # Table template setup
    template = "{0:4}|{1:7}|{2:10}|{3:12}|{4:11}" # column widths: 8, 10, 15, 7, 10

    for path in elf_files:
        print('File: ', path.name)
        
        try:
            file = open(path, 'rb')
            elffile = ELFFile(file)

            print(template.format("NO.", "TYPE", "OFFSET", "SIZE IN FILE", "SIZE IN MEM")) # header
            for i in range(elffile.num_segments()):
                seg = elffile.get_segment(i)
                print(template.format('['+ str(i) + ']', seg.header.p_type, seg.header.p_offset, seg.header.p_filesz, seg.header.p_memsz)) # header          
        except:
            print("File " + str(path) + "failed to open")
        print("===============================================")

        
        
