from elftools.elf.elffile import ELFFile
import sys
import os

if __name__ == '__main__':
    print("================")
    print("ELF File reader")
    print("================")
    
    elf_files = []
    
    # elf file input check
    if len(sys.argv) > 1:
        for path in range(1,len(sys.argv)):
            if path.is_file() and path.endswith('.elf'):
                elf_files.append(path)   
    else:
        try:
            for path in os.scandir(r'elf_files'):
                if path.is_file() and path.name.endswith('.elf'):
                    elf_files.append(path)
        except:
            print("Directory elf_files has not been found")
                
    if elf_files.count == 0:
        print("No .ELF files have not been provided")
        exit()                

    # Table template setup
    template = "{0:4}|{1:7}|{2:10}|{3:10}|{4:10}" # column widths: 8, 10, 15, 7, 10

    for path in elf_files:
        print('File: ', path)
        print("---------------")

        try:
            file = open(path, 'rb')
            elffile = ELFFile(file)

            print(template.format("NO.", "TYPE", "OFFSET", "FILE SIZE", "MEM SIZE")) # header
            for i in range(elffile.num_segments()):
                seg = elffile.get_segment(i)
                print(template.format('['+ str(i) + ']', seg.header.p_type, seg.header.p_offset, seg.header.p_filesz, seg.header.p_memsz)) # header          
        except:
            print("File " + str(path) + "failed to open")
        print("===============================================")

        
        
