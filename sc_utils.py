"""utilities hack to run seam carver
    Requires ffmpeg
"""
import os
import subprocess as sp
import json

def ffgetsize(file_in):
    """fast method to get image size in python"""
    _fcmd = ['ffprobe', '-v', 'error', '-show_entries',
             'stream=width,height', '-of', 'json', file_in]
    proc = sp.Popen(_fcmd, stdin=sp.PIPE, stderr=sp.PIPE, stdout=sp.PIPE)
    out, _ = proc.communicate()
    _out = json.loads(out)['streams'][0]
    return (_out['width'], _out['height'])

def ffgetformat(file_in):
    """check if image is correct format for seam carving"""
    _fcmd = ['ffprobe', '-v', 'error', '-show_entries',
             'stream=pix_fmt', '-of', 'json', file_in]
    proc = sp.Popen(_fcmd, stdin=sp.PIPE, stderr=sp.PIPE, stdout=sp.PIPE)
    out, _ = proc.communicate()
    _out = json.loads(out)['streams'][0]
    return _out['pix_fmt']

def ffconvert(file_in, file_out, imsize):
    """converts image to bgra and rotates counter clockwise if needed
    gpu-seamcarving only considers vertical seams
    """
    _fcmd = ['ffmpeg', '-i', file_in, '-pix_fmt', 'bgra']
    if imsize[1] > imsize[0]:
        _fcmd = _fcmd + ['-vf', 'transpose=2']

    if max(imsize[1], imsize[0]) > 1024:
        if len(_fcmd) < 7:
            _fcmd.append('-vf')
        _fcmd.append('scale=1024:-1')

    _fcmd.append(file_out)
    sp.Popen(_fcmd, stdin=sp.PIPE, stderr=sp.PIPE, stdout=sp.PIPE)

    return file_out

def ffrotate(file_in, file_out):
    """rotates image clockwise"""
    _fcmd = ['ffmpeg', '-y', '-i', file_in, '-vf', 'transpose=1', file_out]
    sp.Popen(_fcmd, stdin=sp.PIPE, stderr=sp.PIPE, stdout=sp.PIPE)
    return file_out

def ffresize(file_in, file_out):
    """resizes to max width: 1024"""
    _fcmd = ['ffmpeg', '-y', '-i', file_in, '-vf', 'scale=1024:-1', file_out]
    sp.Popen(_fcmd, stdin=sp.PIPE, stderr=sp.PIPE, stdout=sp.PIPE)
    return file_out

def get_folder(folder):
    if not os.path.isdir(folder):
        try:
            os.mkdir(folder)
        except:
            return False
    return True

def get_file(folder, file):
    if not os.path.isdir(folder):
        return None
    _file = os.path.join(folder, file)
    if not os.path.isfile(_file):
        return None
    return _file

def set_file(folder, file, ext):
    get_folder(folder)
    _file = os.path.join(folder, os.path.splitext(os.path.basename(file))[0] + ext)
    return _file

def remove_seams(file_in, file_out, n_seams, gpu=False):
    exe = ('cuda' if gpu else 'sequential')+'/driver.out'

    _fcmd = [exe, '-n', str(n_seams), '-i', file_in, '-o', file_out]
    print(' '.join(_fcmd))
    proc = sp.Popen(_fcmd, stdin=sp.PIPE, stderr=sp.PIPE, stdout=sp.PIPE)
    out, err = proc.communicate()
    return out, err
