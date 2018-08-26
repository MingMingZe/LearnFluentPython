def read_line(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096)

        if not chunk:
            yield buf
            break
        buf += chunk


with open("input.txt") as f:
    for line in read_line(f, '{|}'):
        print(line)

