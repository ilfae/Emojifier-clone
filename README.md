#####################################INTRO#####################################

ImgToEmoji Converter

The

####################################INSTALL#####################################

1. Install python and pip

2. Install packages (specified at requirements.txt)
   You can install everything by running "pip install -r requirements.txt"

3. Install Install the ImageMagick CLI.

If you have trouble installing, talk to me (@frmsaul). I always have trouble
setting up software too, so would love to help a fellow struggler. 

#####################################HOW TO USE#################################
You can emojify by running:

"python emoji.py [FLAGS]"

Where the flags are specified here:
  --company: <Brow|Chart|Appl|Goog|Twtr|One|FB|FBM|Sams|Wind|GMail|SB|DCM|KDDI>: the
    emoji implementation
    (default: 'Appl')
  --emoji_size: The font size in the resulting html.May also be the size in pixels of
    each emoji.outputed by the converter.
    (default: '10')
    (a positive integer)
  --emojis_in_width: Number of emojis to compose
    (default: '60')
    (a non-negative integer)
  --output_file: The output file
    (default: 'output.html')
  --src_image: the image you want to transform
    (default: '')
  --[no]use_kd_tree: Use kd_tree instead of brute force.
    (default: 'true')
  --work_location: the location where the emojis will be generated
    (default: '/tmp/Emojis')

A few examples:

