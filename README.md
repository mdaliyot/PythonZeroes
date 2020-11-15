create virtualenv
-----------------
> python -m venv <env name>
> <env name>\Scripts\activate
# Verify venv is activated using:
> pip3 -V
> pip3 install -r requirements.txt

Run python script
-----------------
usage: ExPyZeroes.py [-h] --wav WAV [--xrange XRANGE] [--yrange YRANGE]
                     [--max_burst MAX_BURST] [--max_repetition MAX_REPETITION]

optional arguments:
  -h, --help            show this help message and exit
  --wav WAV, -w WAV     wave file
  --xrange XRANGE, -x XRANGE
                        Histogram X Range. Format: --xrange=xmin,xmax. e.g.
                        --xrange=3,42
  --yrange YRANGE, -y YRANGE
                        Histogram Y Range. Format: --yrange=ymin,ymax. e.g.
                        --yrange=3,42
  --max_burst MAX_BURST, -b MAX_BURST
                        max allowed burst size
  --max_repetition MAX_REPETITION, -r MAX_REPETITION
                        max allowed repetitions of max allowed burst
