from subprocess import check_output


def result_of(cmd):
    cmd_list_arr = cmd.split(" ")
    result = check_output(cmd_list_arr).decode('utf-8')
    return result
