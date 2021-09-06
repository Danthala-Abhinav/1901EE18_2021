import os    

# Imported OS module
def output_individual_roll(File):   # To create every individual rollno data
    # File refers to regtable_old.csv
    try:
        mkdir('output_individual_roll')
        # To create a directory       
    except:
        pass
        # If already created we just move on to the next part
    with open(File, 'r') as f:
        # f refers to the File
         for line in f:
             # Each line of csv refers to 'line'
            entity = line.split(',')
            # entity is refered to each word of the line(separated by comma)
            del entity[4:8]
            del entity[2]
            if(entity[0]=='rollno'):
                continue
            else:
                try:
                    with open(f'output_individual_roll\\{entity[0]}.csv'):
                        with open(f'output_individual_roll\\{entity[0]}.csv', 'a') as g:
                            entity = ','.join(entity)
                            g.write(entity)
                except:
                    with open(f'output_individual_roll\\{entity[0]}.csv', 'w') as g:
                        g.write('rollno,register_sem,subno,sub_type\n')
                        entity = ','.join(entity)
                        g.write(entity)
    return                   

def output_by_subject(File):     # To create every individual subject data
    try:
        mkdir('output_by_subject')
    except:
        pass
    with open(File, 'r') as f:
         for line in f:
            entity = line.split(',')
            del entity[4:8]
            del entity[2]
            if(entity[2]=='subno'):
                continue
            else:
                try:
                    with open(f'output_by_subject\\{entity[2]}.csv'):
                        with open(f'output_by_subject\\{entity[2]}.csv', 'a') as g:
                            entity = ','.join(entity)
                            g.write(entity)
                except:
                    with open(f'output_by_subject\\{entity[2]}.csv', 'w') as g:
                        g.write('rollno,register_sem,subno,sub_type\n')
                        entity = ','.join(entity)
                        g.write(entity)
    return

output_individual_roll('regtable_old.csv')   
output_by_subject('regtable_old.csv')