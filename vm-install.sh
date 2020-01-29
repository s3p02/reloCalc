sudo yum install -y centos-release-scl
sudo yum install -y rh-python36
scl enable rh-python36 bash
which python3
virtualenv -p /PATH/TO/bin/python3 py3env
source py3env/bin/activate
pip install requests
