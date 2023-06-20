from elftools.elf.elffile import ELFFile
import sys
import os

if __name__ == '__main__':
    print("================")
    print("ELF File reader")
    print("================")
    
    elf_files = []
    
    # elf file input check
    sys.argv = [sys.argv[0], r'C:\Espressif\cv_task\elf_files\blink.elf', '"elf_files\\blink.elf"', 'argument2']
    if len(sys.argv) > 1:
        for arg_index in range(1,len(sys.argv)):
            try:
                arg_path = str(sys.argv[arg_index])
                if arg_path.endswith('.elf'):
                    elf_files.append(arg_path)
            except:
                print("Argument: " +  "is not path to .ELF file")
                
    else:
        try:
            for path in os.scandir(r'elf_files'):
                if path.name.endswith('.elf'):
                    elf_files.append(path)
        except:
            print("Directory elf_files has not been found")
                
    if elf_files.count == 0:
        print("No .ELF files have not been provided")
        exit()                

    # Table template setup
    template = "{0:4}|{1:7}|{2:10}|{3:12}|{4:11}" # column widths: 8, 10, 15, 7, 10

    for path in elf_files:
        if type(path) == os.path:
            print('File: ', path.name)
        else:
            print('File: ', path)
        print("---------------")

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

        
        
