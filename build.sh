cd "$(dirname "$0")"

rm -rf build dist ./*.egg-info
virtualenv .3 -p 3
.3/bin/python setup.py sdist bdist_wheel
rm -rf .3
