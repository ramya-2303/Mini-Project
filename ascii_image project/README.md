# ASCII Image Generator in C

This project converts an input image into **ASCII art** using the C programming language.  
Each pixel of the image is analyzed, converted to grayscale, and then mapped to a corresponding ASCII character based on its intensity.

## Files in this Folder

- **ascii_image.c**  
  C program that reads an image file and converts it into ASCII art.

- **input1.png**  
  Input image used for ASCII conversion.

- **my_ascii_output.txt**  
  Output file containing the generated ASCII art.

## How It Works

1. The program loads the image using the **stb_image** library.
2. Each pixel’s RGB values are converted into a grayscale value.
3. The grayscale value is mapped to an ASCII character.
4. The ASCII characters are written line by line into a text file.

## Compilation and Execution

Make sure `stb_image.h` is present in the same folder.

gcc ascii_image.c -o ascii_image
./ascii_image
