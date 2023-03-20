# merge_files_in_a_folder # 合并音频
import os
import glob
import numpy as np
import scipy.io.wavfile as wav
import shutil


def merge_files(path_read_folder, files, path_write_wav_file):
    #
    # files = os.listdir(path_read_folder)
    merged_signal = []
    for filename in files:
        # print(filename)
        if filename != '':
            sr, signal = wav.read(os.path.join(path_read_folder,'{}.wav'.format(filename)))
            merged_signal.append(signal)
    merged_signal = np.hstack(merged_signal)
    merged_signal = np.asarray(merged_signal, dtype=np.int16)
    wav.write(path_write_wav_file, sr, merged_signal)


def rmWavs(path):
    shutil.rmtree(path)
    os.mkdir(path)
