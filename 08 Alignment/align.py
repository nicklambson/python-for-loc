import os
from bleualign.align import Aligner

options = {'srcfile': r'6_for_alignment/segmented_en_US.txt',
           'targetfile': r'6_for_alignment/segmented_es.txt',
           'srctotarget': [r'6_for_alignment/machineTranslated_spa.txt'],
           'targettosrc': [],
           'output-src': 'output_src.txt',
           'output-target': "output_tgt.txt", }

a = Aligner(options)
a.mainloop()
output_src, output_target = a.results()