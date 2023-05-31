# Conversor from trace file (pinatrace.so) to din format required to DineroIV benchmark tool.

input_filename  = 'radix.trace.out'
output_filename = 'radix.din'

output_file = open(output_filename, 'w', newline='\n', encoding='utf-8')

with open(input_filename, 'r') as file:
    text = file.readlines()

count = 0

for input_line in text:
    try:
        tokens = input_line.split()
        
        output_line = tokens[1] + " " + tokens[0].replace(':', '')  + " " + tokens[2] + "\n"

        output_file.writelines(output_line)

        count += 1

    except Exception:
        x = 0
        pass

file.close()

print(f'Work well done and the file {output_filename} was generated with {count} records.')
