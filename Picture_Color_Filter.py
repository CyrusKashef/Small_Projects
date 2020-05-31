from PIL import Image
from math import floor
from os import path

### IMAGE FUNCTIONS ###

def open_image(directory):
    """Returns an image object created from the image at the directory"""
    print("Opening Image")
    image = Image.open(directory)
    return image

def closed_image(image):
    """Closes the image object session"""
    print("Closing Image")
    image.close()

def save_new_image(res, directory):
    """Saves new image at the inputted directory"""
    print("Saving Image At: " + directory)
    res.save(directory)

def show_new_image(res):
    """Displays a preview of the image object"""
    print("Showing Image")
    res.show()

def new_image_name(image_dir, color_list):
    """Returns string of new directory using original image's directory and colors filtered"""
    print("Creating Directory For New Image")
    color_name = ""
    for color in color_list:
        color_name += "_" + color
    new_dir = image_dir.split(".")[0] + color_name + "." + image_dir.split(".")[1]
    print("New Directory: " + new_dir)
    return new_dir

def create_alt_image(image):
    """Returns a blank image with the mode and size of the original image"""
    print("Creating Blank Image")
    res = Image.new(image.mode, image.size)
    return res

### COLOR FILTERS ###

def is_red(red, green, blue):
    """Returns true if the red value is significantly greater than blue and green"""
    boolean = (red > (1.3 * blue)) and (red > (1.3 * green))
    return boolean

def is_blue(red, green, blue):
    """Returns true if the blue value is significantly greater than red and green"""
    boolean = (blue > (1.3 * red)) and (blue > (1.3 * green))
    return boolean

def is_green(red, green, blue):
    """Returns true if the green value is significantly greater than blue and red"""
    boolean = (green > (1.3 * blue)) and (green > (1.3 * red))
    return boolean

def is_yellow(red, green, blue):
    """Returns true if the red and green values are approximately close and are significantly greater than blue"""
    boolean = (green > (1.3 * blue)) and (abs(green - red) < (green * 0.05))
    return boolean

def is_magenta(red, green, blue):
    """Returns true if the red and blue values are approximately close and are significantly greater than green"""
    boolean = (blue > (1.3 * green)) and (abs(blue - red) < (blue * 0.05))
    return boolean

def is_turquoise(red, green, blue):
    """Returns true if the green and blue values are approximately close and are significantly greater than red"""
    boolean = (blue > (1.3 * red)) and (abs(blue - green) < (blue * 0.05))
    return boolean

def is_orange(red, green, blue):
    """Returns true if the red value is greater or equal to green which is greater or equal to blue"""
    boolean = (green >= blue) and (red >= green)
    return boolean

def is_lime(red, green, blue):
    """Returns true if the green value is greater or equal to red which is greater or equal to blue"""
    boolean = (red >= blue) and (green >= red)
    return boolean

def is_teal(red, green, blue):
    """Returns true if the green value is greater or equal to blue which is greater or equal to red"""
    boolean = (blue >= red) and (green >= blue)
    return boolean

def is_denim(red, green, blue):
    """Returns true if the blue value is greater or equal to green which is greater or equal to red"""
    boolean = (green >= red) and (blue >= green)
    return boolean

def is_pink(red, green, blue):
    """Returns true if the red value is greater or equal to blue which is greater or equal to green"""
    boolean = (blue >= green) and (red >= blue)
    return boolean

def is_purple(red, green, blue):
    """Returns true if the blue value is greater or equal to red which is greater or equal to green"""
    boolean = (red >= green) and (blue >= red)
    return boolean

def filter_color(image, color_list):
    """Returns the filtered version of the original image"""
    print("Checking Color List")
    res = create_alt_image(image)
    height, width = image.size
    for row in range(height):
        print("Row " + str(row) + "/" + str(height))
        for col in range(width):
            try:
                red, green, blue = image.getpixel((row, col))
            except ValueError:
                red, green, blue, sat = image.getpixel((row, col))
            # RED
            if((("red" in color_list) and is_red(red, green, blue)) or
            # BLUE
               (("blue" in color_list) and is_blue(red, green, blue)) or
            # GREEN
               (("green" in color_list) and is_green(red, green, blue)) or
            # YELLOW
               (("yellow" in color_list) and is_yellow(red, green, blue)) or
            # MAGENTA
               (("magenta" in color_list) and is_magenta(red, green, blue)) or
            # TURQUOISE
               (("turquoise" in color_list) and is_turquoise(red, green, blue)) or
            # ORANGE
               (("orange" in color_list) and is_orange(red, green, blue)) or
            # LIME
               (("lime" in color_list) and is_lime(red, green, blue)) or
            # TEAL
               (("teal" in color_list) and is_teal(red, green, blue)) or
            # DENIM
               (("denim" in color_list) and is_denim(red, green, blue)) or
            # PINK
               (("pink" in color_list) and is_pink(red, green, blue)) or
            # PURPLE
               (("purple" in color_list) and is_purple(red, green, blue))):
                res.putpixel((row, col), (red, green, blue))
            else:
                avg = floor((red + blue + green) / 3)
                res.putpixel((row, col), (avg, avg, avg))
    return res

### MAIN FUNCTION ###

def highlight_color(image_dir, color_list):
    """Main Function That Runs Filter"""
    print("Highlighting Color Main Function")
    color_list = are_colors(color_list)
    directory_exists(image_dir)
    image = open_image(image_dir)
    new_dir = new_image_name(image_dir, color_list)
    res = filter_color(image, color_list)
    save_new_image(res, new_dir)
    closed_image(image)

### VALIDATION ###

def are_colors(color_list):
    """Returns list of lower cased colors; Errors if invalid color is in list"""
    valid_color_list = ["red", "blue", "green", "yellow", "magenta", "turquoise", "orange", "lime", "teal", "denim", "pink", "purple"]
    fixed_color_list = []
    for color in color_list:
        if(color.lower() not in valid_color_list):
            raise Exception("Color selected is not a valid color: " + str(color))
        else:
            fixed_color_list.append(color.lower())
    return fixed_color_list

def directory_exists(directory):
    """Checks if image file exists"""
    if(not path.isfile(directory)):
        raise Exception("Directory given is not a file.")
    file_extension = directory.split(".")[-1]
    if(file_extension not in ["jpg", "jpeg", "png"]):
        raise Exception("File extension must be jpg, jpeg, or png")

##################
### TEST CASES ###
##################

# Location of the file
#image_dir = "C:/Users/Cyrus/Pictures/Jiggly_Parry.png"
# Colors you wish to filter by
#color = ["pink", "yellow", "magenta", "purple", "orange"]
# Run the Function
#highlight_color(image_dir, color)
