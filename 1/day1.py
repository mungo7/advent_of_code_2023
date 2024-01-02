input_file=('input1.txt')

output_sum=0
with open(input_file, 'r') as f:
    for line in f:
        input_string=line
        output_list=[]
        for character in input_string:
            if character.isdigit():
                output_list.append(character)
        output_sum += int(output_list[0] + output_list[-1])
        print(output_sum)
print(output_sum)
