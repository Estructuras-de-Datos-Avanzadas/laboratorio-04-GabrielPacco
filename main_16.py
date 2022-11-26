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
            octree.add_color(Color
            (*pixels[i, j]))

    # 16 colors for 8 bits per pixel 
    # output image
    palette = octree.make_palette(16)

    # create palette for 16 color max and 
    # save to file
    palette_image = Image.new('RGB', 
    (4, 4))
    palette_pixels = palette_image.load()
    for i, color in enumerate(palette):
        palette_pixels[i % 4, i / 4] = (int(color.red), int(color.green), 
        int(color.blue))
    
    palette_out_1 = Image.new('RGB', (16, 16))
    palette__out_p_1 = palette_out_1.load()
    for j in range(16):
      for i in range(16):
            palette__out_p_1[i, j] = palette_pixels[i / 4, j / 4]

    palette_out = Image.new('RGB', (width, 
    height))
    palette__out_p = palette_out.load()
    for j in range(height):
      for i in range(width):
            palette__out_p[i, j] = palette__out_p_1[i / 16, j / 16]

    palette_out.save('paisaje_palette_16.png')

    # save output image
    out_image = Image.new('RGB', (width, 
    height))
    out_pixels = out_image.load()
    for j in range(height):
        for i in range(width):
            index = octree.get_palette_index(Color(*pixels[i, j]))
            color = palette[index]
            out_pixels[i, j] = (int(color.red), int(color.green), int(color.blue))
    out_image.save('paisaje_out_16.png')


if __name__ == '__main__':
    main()