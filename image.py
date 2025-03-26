from PIL import Image, ImageDraw, ImageFont

def create_pipe_image():
    width, height = 50, 320
    pipe_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(pipe_img)

    draw.rectangle([0, 20, width, height], fill='green')

    draw.rectangle([0, 0, width, 20], fill='darkgreen')

    return pipe_img

def create_background_image():
    width, height = 288, 512    
    bg_img = Image.new('RGB', (width, height), 'skyblue')
    draw = ImageDraw.Draw(bg_img)

    draw.ellipse([50, 50, 100, 70], fill='white')
    draw.ellipse([200, 80, 250, 100], fill='white')
    draw.ellipse([150, 150, 210, 180], fill='white')

    return bg_img

def create_bird_img():
    width, height = 34, 24
    bird_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(bird_img)

    draw.ellipse([2, 2, 32, 22], fill='yellow')

    draw.polygon([ (24, 12), (34, 8), (34, 16)], fill ='orange')

    draw.ellipse([10, 6, 18, 14], fill= 'white')
    draw.ellipse([14, 10, 16, 12], fill = 'black')

    return bird_img

def create_base_img():
    width, height = 288, 112
    base_img = Image.new('RGB', (width, height), 'brown')
    draw = ImageDraw.Draw(base_img)

    draw.rectangle([0, 0, width, 10], fill='green')

    return base_img

def create_digit_image(digit, font):
    width, height = 24, 36
    digit_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(digit_img)
    
    # Draw the digit
    text = str(digit)
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2
    draw.text((text_x, text_y), text, font=font, fill='white')
    
    return digit_img

font_path = "/haris/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_size = 28
font = ImageFont.truetype(font_path, font_size)


for digit in range(10):
    digit_img = create_digit_image(digit, font)
    digit_img.save(f'D:\\VS code\\python programs\\flappy bird\\{digit}.png')

digit_images = [create_digit_image(digit, font) for digit in range(10)]
create_digit_image()



pipe_img = create_pipe_image()
pipe_img.save('pipe.png')

bg_img = create_background_image()
bg_img.save('background.jpg')

bird_img = create_bird_img()
bird_img.save('bird.png')

base_img = create_base_img()
base_img.save('base.png')

pipe_img.show()
bg_img.show()
bird_img.show()
base_img.show()

