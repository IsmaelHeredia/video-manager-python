# Video Manager

This project would be a script made in Python with a separate GUI version with the most important options. Most of the features are geared toward YouTube videos.

In the case of the script, the commands to use would be:

-download-video = The link of the video to download in MP4 format is requested as an argument, it can be combined with -output-name.

-download-song = The video link to download in MP3 format is requested as an argument, it can be combined with -output-name.

-download-videos = A file with a list of links to download the videos in MP4 format is requested as an argument.

-download-songs = A file with a list of links to download in MP3 format is requested as an argument.

-convert-to-mp3 = The local location of a video is requested as an argument to convert it to MP3, it must be combined with -output-name to save the song.

-findsong-and-download = The name of the song is requested as an argument to search on Google and later download in MP3 format.

-findsongs-and-download = A file with a list of names to search on Google and download in MP3 format is requested as an argument.

-read-playlist = The playlist link is requested as an argument to list the corresponding links, it must be combined with the -output-name command to set the name of the file in which the results will be saved.

-download-playlist-videos = The playlist link is requested as an argument to download all the videos in MP4 format.

-download-playlist-songs = The playlist link is requested as an argument to download all the videos in MP3 format.

-output-name = The name with which the file will be saved is requested as an argument, it has to be just the name, without an extension.

-output-folder = The name of the folder in which it will be saved is requested as an argument, if it does not exist, it creates it, this option can be combined with all the functions in which videos or songs are downloaded.

In the GUI version it is only allowed to download videos and songs with the option to choose a name and folder. Additionally, when starting it will detect if there is a valid link on the clipboard to insert it directly into the Link textbox.

The project was designed to be used on Windows so all downloads will be saved in the "Music" and "Videos" folders, the subfolder will be called "Video_downloads", the script itself will detect if it is a song or a video and save it in its corresponding folder.

Some example images of use for each version:

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhpXAIAZoUdSG599C6UrsCIE23uO_euq4hsTTCB9PPshMJhWF2FxtjJ2zI37sn1jWpzZoXbRxsmh61AtimPH_YItZ-58ipisNM-d-VfoALDlgqf_IjjrS5yEtMEjFS-vRK1QzgyTTYKvlSJz4ADpuDXbZO7baPcDC_SZCRsTeqZMupSJuF83RObWWm5cbA/s976/1.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHU6kAdWCZalDI-Pa2JBOYS01Xq0wu1hEPxOhnJjtV57LSHBLJEeKlWknbx6XsfStj2GmjiIMaWRQtP2lddu8P86Tu0hZBFHmI1c79ikNSIjRgnbU3S8JG0BBDTeMr5Jhjrb2cCiSsoTceOU3Lp8MalTUISkZZFaCrlHmIegFfMiOIcNeBuY3jMs8kJu8/s975/2.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguKnw7EOeHBgosPVhQXh5tLoPPHzCr05PlJZYHGIVxi_Fyd6wv8nE-pj9abCQpgDMQmuoh1S4PtF_5WGiM7heqaAgxN45oBAy-729RX98FzzcX6242558YjaLEcllxDrJQY2Fw3x4jTk7AUrVAGv4EGxldK_3lsIL10PTy3sRk2ip5gjZYzazcuPNZRu0/s489/3.png)

![screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8VizZuiySzWOQxzjPcCAQ30Hw1-2EaO9PKuNggqHwSgt3utH3uAthqT04JJ5PXtTsqiS5yglTJgd74qw2iUYzkZA3ygJ8PAYzDN62D_-nNVsp7kP4-KZInM7vFas0MwP1ck11R5ib79rrzWx9iErXe2spjbyJA6ziQVVxrEs9iOSAminzhfYCFm_gJww/s489/4.png)
