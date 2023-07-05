import os
import shutil

sn = os.path.basename(__file__)

if not os.path.exists('first'):
    os.mkdir('first')

shutil.copyfile(__file__,f'first/{sn}')
    
if not os.path.exists('second'):
    os.mkdir('second')
    
if not os.path.exists('third'):
    os.mkdir('third')
    
