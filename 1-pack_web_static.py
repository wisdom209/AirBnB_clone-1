#!/usr/bin/python3
"""make a tarball of web_static files"""
from fabric.api import local, task, settings
from datetime import datetime


@task
def do_pack():
    """make a tar archive"""
    now = datetime.now()
    y = now.strftime('%Y')
    mon = now.strftime('%m')
    day = now.strftime('%d')
    h = now.strftime('%H')
    mins = now.strftime('%M')
    s = now.strftime('%S')
    tar_name = "web_static_{}{}{}{}{}{}".format(y, mon, day, h, mins, s)
    local('rm -rf git_folder')
    local('git clone https://github.com/wisdom209/AirBnB_clone git_folder')
    local('rm -rf versions && mkdir versions')
    local("tar -czvf versions/{}.tgz -C\
           git_folder/ web_static".format(tar_name))
    local('rm -rf git_folder')
    with settings(warn_only=True):
        result = local('test -d versions && test -n "$(ls versions)" | true')
    if result.failed:
        return None
    else:
        archive_path = "versions/{}.tgz".format(tar_name)
        print(archive_path)
        return (archive_path)
