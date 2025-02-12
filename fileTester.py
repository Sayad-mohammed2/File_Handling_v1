import first_project_files_handiling

def run_main__tester__():
    print(f'File name __name__ = %s' %__name__)
    if __name__ == '__main__':
        print('File executed immediately')
    else :
        print('File Imported __name__ %s ' %__name__)
run_main__tester__()