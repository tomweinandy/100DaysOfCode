from PIL import Image


def add(a, b):
    return a + b


def watermark(filepath, black_or_white='white', opacity=0.65, output_filename='default'):
    # Load images
    # filename = input('What image in your downloads folder would you like to watermark?: ')
    img = Image.open(filepath)
    logo_black = Image.open('pie.png')

    # Set opacity
    logo = logo_black.convert("RGBA")
    datas = logo.getdata()

    # Change colors and make semi-transparent
    newData = []
    for item in datas:
        new_opacity = int(item[3] * opacity)

        # If 'white' is selected
        if black_or_white == 'white':
            # If rbg is black (0,0,0) then make it white (255, 255, 255) and opaque
            if item[0:3] == (0, 0, 0):
                newData.append((255, 255, 255, new_opacity))

            # Otherwise, keep colors but make it transparent
            else:
                newData.append((item[0], item[1], item[2], 0))

        # Otherwise assume 'black' is selected
        else:
            # If rbg is black (0,0,0) then keep it black but make opaque
            if item[0:3] == (0, 0, 0):
                newData.append((0, 0, 0, new_opacity))

            # Otherwise, keep colors but make it transparent
            else:
                newData.append((item[0], item[1], item[2], 0))


    logo.putdata(newData)

    # Place watermark in the bottom-right corner
    x_placement = img.size[0] - logo.size[0]
    y_placement = img.size[1] - logo.size[1]
    logo_placement = (x_placement, y_placement)
    img.paste(logo, logo_placement, logo)

    # Show image
    img.show()

    # Save new image in Downloads folder

    # Select the filename from everything after the last backslash
    filename = filepath.split('/')[-1]

    # Return the partial filepath as everything before the filename
    partial_filepath = filepath[:-len(filename)]

    if output_filename == 'default':
        name_split = filename.split('.')
        output_filename = name_split[0] + '_watermarked.' + name_split[1]

    img.save(partial_filepath + output_filename)
