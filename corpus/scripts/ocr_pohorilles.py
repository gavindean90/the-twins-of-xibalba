#!/usr/bin/env python3
"""Recreate provisional OCR; requires pdftoppm, Tesseract, Pillow and German data."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import tempfile
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tessdata-dir',required=True)
    parser.add_argument('--output',type=Path,required=True,help='Separate output for review; do not overwrite historical OCR silently')
    args=parser.parse_args()
    pdf=ROOT/'sources/scans/pohorilles-1913.pdf'
    if not pdf.exists():parser.error('Run acquire.py --id pohorilles-pdf first')
    with tempfile.TemporaryDirectory() as directory:
        tmp=Path(directory)
        def page(n):
            base=tmp/f'{n:03d}'
            subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','200','-singlefile','-jpeg',str(pdf),str(base)],check=True,capture_output=True)
            im=Image.open(str(base)+'.jpg');w,h=im.size;parts=[]
            for side,box in [('left',(0,0,w//2,h)),('right',(w//2,0,w,h))]:
                image=tmp/f'{n:03d}-{side}.png';im.crop(box).save(image)
                result=subprocess.run(['tesseract',str(image),'stdout','--tessdata-dir',args.tessdata_dir,'-l','deu','--psm','3'],check=True,capture_output=True)
                parts.append(f'\n[PDF page {n}; {side} half; printed page unverified]\n'+result.stdout.decode())
                image.unlink()
            Path(str(base)+'.jpg').unlink()
            return ''.join(parts)+'\f\n'
        with ThreadPoolExecutor(max_workers=4) as pool, args.output.open('w') as out:
            for text in pool.map(page,range(1,72)):out.write(text)

if __name__=='__main__':main()
