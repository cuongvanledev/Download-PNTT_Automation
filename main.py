import os
import download
import PNTT_GetLink
import sys


def main():
    links = PNTT_GetLink.getlinks()
    index = 200

    for i in range(200, 466):
        if i == (index + 5):
            os.system("pause")
            index += 5
        download.downloadLink(links[i])


if __name__ == "__main__":
    main()