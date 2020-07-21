import sys
sys.path.append('/root/test1/day2')
from read import read_csv
from json_rw import to_json

l = read_csv('sample.csv')
to_json(l,'result.json')
