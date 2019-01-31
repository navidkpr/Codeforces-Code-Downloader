
def extract_codes(file_paths):
    first_line_text_filter = "program-source-text"

    for path in file_paths:
        myfile = open(path, 'r');
        lines = myfile.read()
        lines = lines.splitlines()
        while lines[0].find(first_line_text_filter) == -1:
            lines = lines[1:];
        while lines[0][0] != '>':
            lines[0] = lines[0][1:]
        lines[0] = lines[0][1:]
        myfile = open(path, 'w');
        for line in lines:
            myfile.write(line + '\n')
