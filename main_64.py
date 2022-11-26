from PIL import Image
from color import Color
from octree_quantizer import OctreeQuantizer

def main():
    image = Image.open('paisaje.png')
    pixels = image.load()
    width, height = image.size

    octree = OctreeQuantizer()

    # add colors to the octree
    for j in range(height):
        for i in range(width):
            octree.add_color(Color(*pixels
            [i, j]))

    # 64 colors for 8 bits per pixel 
    # output image
    palette = octree.make_palette(64)

    # create palette for 64 color max and 
    # save to file
    palette_image = Image.new('RGB', (8, 8))
    palette_pixels = palette_image.load()
    for i, color in enumerate(palette):
        palette_pixels[i % 8, i / 8] = (int(color.red), int(color.green),
        int(color.blue))
    
    palette_out_1 = Image.new('RGB', (64, 64))
    palette__out_p_1 = palette_out_1.load()
    for j in range(64):
      for i in range(64):
            palette__out_p_1[i, j] = palette_pixels[i / 8, j / 8]

    palette_out = Image.new('RGB', (width, height))
    palette__out_p = palette_out.load()
    for j in range(height):
      for i in range(width):
            palette__out_p[i, j] = palette__out_p_1[i / 4, j / 4]

    palette_out.save('paisaje_palette_64.png')

    # save output image
    out_image = Image.new('RGB', (width, 
    height))
    out_pixels = out_image.load()
    for j in range(height):
        for i in range(width):
            index = octree.get_palette_index(Color(*pixels[i, j]))
            color = palette[index]
            out_pixels[i, j] = (int(color.red), int(color.green), int(color.blue))
    out_image.save('paisaje_out_64.png')


if __name__ == '__main__':
    main()