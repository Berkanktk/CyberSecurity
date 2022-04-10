# Steganography checklist
## File
Just to be sure what file you are facing with, check its type with  
`type <filename>`

## Strings
View all strings in a binary file with strings  
`strings <filename>`

## Exiftool
Check all image metadata  
`exiftool <filename>` 

## Binwalk
We use binwalk to recursively checck and extract any image's for hidden embedded files.  
`binwalk -Me <filename>` 

## Pngcheck
We can use pngcheck to look for optional/correct broken chunks. This is vital if the image appears corrupt.    
`pngcheck -p <filename>`

## Explore Colour & Bit Planes
Images can be hidden inside of the colour/bit planes. Upload your image the site below. On the image menu page, explore all options in the top panel (i.e. Full Red, Inverse, LSB etc).
Go to "Browse Bit Planes", and browse through all available planes.

If there appears to be some static at the top of any planes, try extracting the data from them in the "Extract Files/Data" menu.

Find it [here](https://stegonline.georgeom.net/upload).

## Extract LSB Data
As mentioned in the secton before, there could be some static in bit planes. If so, navigate to the "Extract Files/Data" page, and select the relevant bits.

Find it [here](https://stegonline.georgeom.net/upload).

## Check RGB Values
ASCII Characters/other data can be hidden in the RGB(A) values of an image.

Try converting them to text, and see if any flag is found. It might be worth looking at just the R/G/B/A values on their own.

Upload your image [here](https://stegonline.georgeom.net/upload), and preview the RGBA values.

## Found a password? (Or not)
If you've found a password, the goto application to check should be steghide. Bear in mind that steghide can be used without a password, too.

You can extract data by running:  
`steghide extract -sf <filename>`