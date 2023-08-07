import os
import mytypes

index = 0
working_dir = './'
target_name = 'stapled.csv'
stapled_filepath = os.path.join(working_dir, target_name)
with open(stapled_filepath, 'w') as f_t:
    # headers
    headers = ['index', 'app_id', 'line_num'] + mytypes.columns
    f_t.write('{}\n'.format(';'.join(headers)))

    for filename in os.listdir(working_dir):
        if filename.endswith('.csv') and filename != target_name:
            app_id = filename.replace('.csv', '')
            filepath = os.path.join(working_dir, filename)
            with open(filepath, 'r') as f_s:
                print('file {} has been opened'.format(filename))
                line_num = 0
                while True:
                    line = f_s.readline()
                    if line:
                        extended = '{};{};{};{}\n'.format(index, app_id, line_num, line.rstrip('\n'))
                        f_t.write(extended)
                        line_num += 1
                        index += 1
                    else:
                        print('file {} has been stapled: line_num: {}; index: {};'.format(filename, line_num, index))
                        break
