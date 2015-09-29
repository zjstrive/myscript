'''
Created on Sep 29, 2015

@author: jie
'''
import os
import traceback
from datetime import datetime

home_path = os.path.expanduser("~") + "/"
mysqldump_output_file_name = home_path + "mysql_backup/"


def mysqldump(host, user, password, database_name, port=3306, skipdata=False):
    try:
        skipdata_string = ''
        if skipdata:
            skipdata_string = '-d'
        output_file = mysqldump_output_file_name + database_name + str(datetime.now().strftime("%Y-%m-%d")) + '.sql'
        mysqldump_string = "mysqldump --lock-tables=false -C -P{0}  -h{1} -u{2} -p{3} {4} {5} > {6}".format(port,
                                                                                                              host,
                                                                                                              user,
                                                                                                              password,
                                                                                                              skipdata_string,
                                                                                                              database_name,
                                                                                                              output_file
                                                                                                              )
        os.system(mysqldump_string)
    except:
        traceback.print_exc()


def backup_xxdata():
    shell_str = 'find /home/jie/xxdata -name "*.zip" -mtime -700 | xargs -I {} scp {} /home/jie/xxdata_backup/'
    os.system(shell_str)


def run():
    backup_xxdata()
    mysqldump("127.0.0.1", "root", "admin", "monitoring")

if __name__ == '__main__':
    run()
