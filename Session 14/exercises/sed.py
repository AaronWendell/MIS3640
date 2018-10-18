def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    f_source = open('Session 14/exercises/' + source, 'r')
    f_dest = open('Session 14/exercises/' + dest, 'w')

    for line in f_source:
        new_line = line.replace(pattern, replace)
        f_dest.write(new_line)

    f_source.close()
    f_dest.close()


pattern = 'man'
replace = 'woman'
source = 'output.txt'
dest = 'new_' + source
sed(pattern, replace, source, dest)
