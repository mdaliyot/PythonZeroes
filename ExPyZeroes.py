import wave
import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser
from tkinter import Tk
from tkinter import messagebox

parser = ArgumentParser()
parser.add_argument("--wav", "-w", type=str, required=True, help="wave file")
parser.add_argument("--xrange", "-x", type=str, required=False, default='',
                    help="Histogram X Range. Format: --xrange=xmin,xmax. e.g. --xrange=3,42")
parser.add_argument("--yrange", "-y", type=str, required=False, default='',
                    help="Histogram Y Range. Format: --yrange=ymin,ymax. e.g. --yrange=3,42")
parser.add_argument("--max_burst", "-b", type=int, required=False, default=10, help="max allowed burst size")
parser.add_argument("--max_repetition", "-r", type=int, required=False, default=5,
                    help="max allowed repetitions of max allowed burst")

try:
	args = parser.parse_args()
except Exception as ex:
	print(ex)
	exit()

wf = wave.open(args.wav)
xrange = ('', '') if not args.xrange else tuple('' if i == '' else int(i) for i in args.xrange.split(','))
yrange = ('', '') if not args.yrange else tuple('' if i == '' else int(i) for i in args.yrange.split(','))
if isinstance(xrange[0], int) and isinstance(xrange[1], int) and xrange[0] >= xrange[1]:
	raise Exception("x range invalid! aborting.")
if isinstance(yrange[0], int) and isinstance(yrange[1], int) and yrange[0] >= yrange[1]:
	raise Exception("y range invalid! aborting.")

# save wav frames into an array
frames = wf.readframes(-1)
arr = np.frombuffer(frames, dtype=np.int16)

# calc zeros sequences
pass
# slow calculation
# i = 0
# seq_size = 0
# list_seq = []
# while i < len(arr):
# 	if arr[i] == 0:
# 		while i < len(arr) and arr[i] == 0:
# 			i += 1
# 			seq_size += 1
# 		list_seq.append(seq_size)
# 		seq_size = 0
# 	i += 1
pass
# fast calculation
arr = np.concatenate(([0, 1], arr, [1, 0]))
zeros_index = np.where(arr == 0)[0]
change_index = np.where(zeros_index[1:] > zeros_index[:-1] + 1)[0]
arr_seq = change_index[1:] - change_index[:-1]

# calc histogram array
arr_bins, arr_counts = np.unique(arr_seq, return_counts=True)
arr_hist = np.vstack((arr_bins, arr_counts))

# remove bins according to required range
if xrange[0]:
	arr_hist = arr_hist[:, arr_hist[0, :] >= xrange[0]]
if xrange[1]:
	arr_hist = arr_hist[:, arr_hist[0, :] <= xrange[1]]

# remove repetitions according to required range
if yrange[0]:
	arr_hist = arr_hist[:, arr_hist[1, :] >= yrange[0]]
if yrange[1]:
	arr_hist = arr_hist[:, arr_hist[1, :] <= yrange[1]]

# plot histogram
plt.figure()
plt.bar(x=arr_hist[0, :], height=arr_hist[1, :], width=1, align='edge')
plt.grid(axis='y', alpha=0.75)
plt.xlabel('seq size')
plt.ylabel('Repetitions')
plt.title('Zeros Sequence Histogram')
plt.show(block=False)

# prompt a message
root = Tk()
root.wm_attributes("-topmost", 1)
root.withdraw()
# check pass/fail criteria
arr_bins = arr_hist[0, :]  # re-calc bins array
max_burst = np.max(arr_bins)
max_burst_repetitions = arr_hist[1, int(np.where(arr_bins == max_burst)[0])]
if max_burst > args.max_burst:
	messagebox.showinfo("Histogram Failed!",
	                    f"max burst size is {max_burst} - greater than maximum allowed!({args.max_burst})")
elif max_burst_repetitions > args.max_repetition:
	messagebox.showinfo("Histogram Failed!",
	                    f"repetition of max burst is {max_burst_repetitions} - greater than maximum allowed!({args.max_repetition})")
else:
	messagebox.showinfo("Histogram Passed!", "Histogram is OK!")
