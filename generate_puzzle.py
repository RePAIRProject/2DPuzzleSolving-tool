import argparse
import pdb
from src.generator import PuzzleGenerator

def generate_puzzle(args):

    print('Groundtruth img path:', args.img_path)
    print('Piece num: %d, sample num: %d\n' % (args.piece_n, args.sample_n))
    print('Background color:', args.bg_color)

    generator = PuzzleGenerator(args.img_path)

    for i in range(args.sample_n):

        print('Sample:', i)

        generator.run(args.piece_n, args.offset_h, args.offset_w, args.small_region, args.rotate, args.smooth_flag,
                      args.alpha_channel, args.perc_missing_fragments, args.erosion, args.borders)
        generator.save(args.bg_color, args.save_regions)

if __name__ == '__main__':

    # Hyper parameters
    parser = argparse.ArgumentParser(description='A tool for generating puzzles.')
    parser.add_argument('-i', '--img-path', default=None, type=str, required=True,
        help='Path to the input image.')
    parser.add_argument('-n', '--piece-n', default=100, type=int,
        help='Number of puzzle pieces. Default is 100. The actual number of puzzle pieces may be different.')
    parser.add_argument('-t', '--sample-n', default=1, type=int,
        help='Number of puzzle you want to generate from the input image. Default is 1.')
    parser.add_argument('--offset-h', default=1, type=float,
        help='Provide the horizontal offset rate when chopping the image. Default is 1. \
        The offset is the rate of the initial rigid piece height. If the value is less than \
        0.5, no interaction will happen.')
    parser.add_argument('--offset-w', default=1, type=float,
        help='Provide the vertical offset rate when chopping the image. Default is 1. \
        The offset is the rate of the initial piece width. If the value is less than \
        0.5, no interaction will happen.')
    parser.add_argument('-s', '--small-region', default=0.25, type=float,
        help='A threshold controls the minimum area of a region with respect to initial rigid \
        piece area. Default is 0.25.')
    parser.add_argument('-r', '--rotate', default=180, type=float,
        help='A range of random rotation (in degree) applied on puzzle pieces. Default is 180. \
        The value should be in [0, 180]. Each piece randomly select a rotation degree in [-r, r]')
    parser.add_argument('--bg_color', default=[0, 0, 0], type=int, nargs=3,
        help='Background color to fill the empty area. Default is [0, 0, 0]. The type is three uint8 \
        numbers in BGR OpenCV format.')

    ## added
    parser.add_argument('-sf', '--smooth-flag', default=False, type=bool,
        help='Boolean flag to enable or disable the interpolation of the cuts. False (default) will cut \
        the image using segments, True will use smooth curves.')
    parser.add_argument('-ac', '--alpha_channel', default=False, type=bool,
        help='Boolean flag to enable the alpha channel. It will save the individual fragments images \
        as transparent (.png) images with alpha = 0 in the background.')
    parser.add_argument('-svr', '--save_regions', default=False, type=bool,
        help='Boolean flag to save a color-coded and an integer version of the regions.')
    parser.add_argument('-pmf', '--perc_missing_fragments', default=0, type=float,
        help='Percentage of missing fragments: values between 0 (no missing fragments) and 100 (all missing). \
        The actual number will be calculated using floor(num_frags * perc) and will be saved in the output.')
    parser.add_argument('-e', '--erosion', default=0, type=int,
        help='Erosion (type): default is 0, which means no erosion. 1 means uniform erosion, 2 means partial erosion \
        in some randomly chosen points and 3 means combining 1 and 2 (uniform + random points)')
    parser.add_argument('-b', '--borders', default=False, type=bool,
        help='Create an additional version of the fragments (in a folder) with extrapolated borders for experiments')
    args = parser.parse_args()

    args.bg_color = tuple(args.bg_color)
    #pdb.set_trace()
    generate_puzzle(args)
