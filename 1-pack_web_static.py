#!/usr/bin/python3
"""make a tarball of web_static files"""
from fabric.api import local, task, settings
from datetime import datetime
import os


@task
def do_pack():
    """make a tar archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    tar_name = "web_static_{}".format(date)
    try:
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        local('git clone https://github.com/wisdom209/AirBnB_clone git_folder')
        local("tar -czvf versions/{}.tgz -C\
        git_folder/ web_static".format(tar_name))
        local('rm -rf git_folder')
        file_name = "versions/web_static_{}.tgz".format(date)
        return file_name
    except Exception:
        return None
