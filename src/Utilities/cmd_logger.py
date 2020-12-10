from subprocess import check_output


def result_of(cmd):
    """
    This function usable for debugging. You can get results of calling commands directly in Docker container. You can
    call commands that contains more than one word without awful subprocess syntax, just write full command in param
    e.g. 'ls images'. For get result in terminal don't forget put this function in 'logger.info()' call.
    :param cmd: command for run in string format
    """
    cmd_list_arr = cmd.split(" ")
    result = check_output(cmd_list_arr).decode('utf-8')
    return result
