import re
import logging as log
from typing import List 

FILE_NAME = 'sample_input'

def data() -> List[str]:
    data = open(FILE_NAME, 'r').read()
    return data.split('\n')

def main():
    total = 0
    for line in data():
        line = line.strip()
        m = re.findall(r'\d', line)
        if len(m)>=2:
            total+=int(m[0])
            total+=int(m[-1])
        elif len(m)==1:
            total+=int(f'{m[0]}{m[0]}')
        else:
            raise Exception('no input found!')
    print(f'Total: {total}')

if __name__ == "__main__":
    main()
