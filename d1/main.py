import re
FILE_NAME = 'sample_input'

# data = open(FILE_NAME, 'r').read()
# lines = str(data).split('\n')
# total = 0
# for line in lines:
#     first_last = ()
#     line = line.strip()
#     m = re.findall(r'\d', line)
#     if len(m)>=2:
#         total+=m[0]
#         total+=m[-1]
#     elif len(m)==1:
#         total+=m[0]*2
#     else:
#         raise Exception(f'no input found! {m}')

with open(FILE_NAME) as f:
    total = 0
    for line in f:
        first_last = ()
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
