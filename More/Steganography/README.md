# Steganography

## Techniques
Simple technique: add extra data at the end of a file
* Often does not change the handling of the file
* Detected only by inspecting the contents of the file

Simplest version: add text string
* cat (print as ASCII), strings (print ASCII strings from the file)
* Search / filter the result with grip / bgrep

Can add entire additional files
* Eg ZIP file stored at the bottom of a PNG
* PNG ends with the trailer IEND, so the image viewer is unaffected 

## Image Steganography
Media files are specially suitable for steganography

Pixels
Color channels: RGB
Plans: typically 8 
![Image Stego](../../Images/Image-stego.png)

## Examples
![Stego image](../../Images/Stego-image.png)

![Stego cover](../../Images/Stego-cover.png)

## Steganography Checklist
### File
Just to be sure what file you are facing with, check its type with  
`type <filename>`

### Strings
View all strings in a binary file with strings  
`strings <filename>`

### Exiftool
Check all image metadata  
`exiftool <filename>` 

### Binwalk
We use binwalk to recursively checck and extract any image's for hidden embedded files.  
`binwalk -Me <filename>` 

### Pngcheck
We can use pngcheck to look for optional/correct broken chunks. This is vital if the image appears corrupt.    
`pngcheck -p <filename>`

### Explore Colour & Bit Planes
Images can be hidden inside of the colour/bit planes. Upload your image the site below. On the image menu page, explore all options in the top panel (i.e. Full Red, Inverse, LSB etc).
Go to "Browse Bit Planes", and browse through all available planes.

If there appears to be some static at the top of any planes, try extracting the data from them in the "Extract Files/Data" menu.

Find it [here](https://stegonline.georgeom.net/upload).

### Extract LSB Data
As mentioned in the secton before, there could be some static in bit planes. If so, navigate to the "Extract Files/Data" page, and select the relevant bits.

Find it [here](https://stegonline.georgeom.net/upload).

### Check RGB Values
ASCII Characters/other data can be hidden in the RGB(A) values of an image.

Try converting them to text, and see if any flag is found. It might be worth looking at just the R/G/B/A values on their own.

Upload your image [here](https://stegonline.georgeom.net/upload), and preview the RGBA values.

### Found a password? (Or not)
If you've found a password, the goto application to check should be steghide. Bear in mind that steghide can be used without a password, too.

You can extract data by running:  
`steghide extract -sf <filename>`

## Tools
* Step Solve: inspect the individual color channels and bit planes of images
* Especially useful for images stored in other images
* step: find saved text data in PNG and BMP
* steghide: embed / extract data in image and audio files
  * More sophisticated method than LSB
  * Optional password for embedding, requires the same password for extraction
  * Tip: password may be blank
  * Tip: use stegseek to bruteforce passwords
* [Stego Toolkit](https://github.com/DominicBreuker/stego-toolkit) - a collection of tools for steganography
* [Pixrecovery](https://online.officerecovery.com/pixrecovery/) - repair corrupt JPEG, PNG, GIF, BMP, TIFF, and RAW images.  
* [stego-lsb](https://pypi.org/project/stego-lsb/) - LSB steganography tool for images, text, and audio files.