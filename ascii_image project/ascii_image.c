#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#include <stdio.h>
#include <stdlib.h>

const char *ascii_chars = "@%#*+=-:. ";

char get_ascii_char(int gray) {
    int len = 10;
    int index = (gray * (len - 1)) / 255;
    return ascii_chars[index];
}

int main() {
    int width, height, channels;
    unsigned char *img = stbi_load("input1.png", &width, &height, &channels, 3); // force 3 channels
    if (img == NULL) {
        printf("Failed to load image.\n");
        return 1;
    }

    FILE *fp = fopen("my_ascii_output.txt", "w");
    if (!fp) {
        printf("Failed to create output file.\n");
        return 1;
    }

    for (int y = 0; y < height; y += 8) {
        for (int x = 0; x < width; x += 4) {
            int i = (y * width + x) * 3; 
            unsigned char r = img[i];
            unsigned char g = img[i + 1];
            unsigned char b = img[i + 2];

            int gray = 0.299 * r + 0.587 * g + 0.114 * b;
            fputc(get_ascii_char(gray), fp);
        }
        fputc('\n', fp);
    }

    fclose(fp);
    stbi_image_free(img);

    printf("ASCII art is saved to my_ascii_output.txt\n");
    return 0;
}

//gcc ascii_image.c -o ascii_image.exe
//./ascii_image.exe
