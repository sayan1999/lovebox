from xmltodict import parse as parsetodict
from os.path import expanduser
from pandas import DataFrame
from utils import savedata
from env import RHYTHMBOXXMLPATH

detailed_listofsongs=parsetodict(open(RHYTHMBOXXMLPATH, 'r').read())['rhythmdb']['entry']
print("Reading rhythmbox config file...")
data=DataFrame([(x, y) for x, y in [(elem['title'], elem['location']) for elem in detailed_listofsongs]], columns=['song', 'location'])

data=data.mask(data.eq(None)).dropna()
data['song']=data['song'].apply(lambda x : x.lower())
print("Saving python object using pickle...")
savedata(data, './objects/df.obj')