# Image Filtering
> I've always wondered how image filters worked and I kept playing with the idea in my head until one day I thought of a pretty simple model. The idea was simple, treat pixels like points in 3-Dimensional space and then apply linear mappings from R3 to R3. With the help of some python libraries, I was able to do just that! Further research led me to an [_article_](https://ai.stanford.edu/~syyeung/cvweb/tutorial1.html#:~:text=Image%20filtering%20changes%20the%20range,points%20without%20changing%20the%20colors.) from Stanford and I adapted their strategies to blur and sharpen images. My favorite part of this project was that it allowed me to apply knowledge from both my Computer Science courses as well as my Linear Algebra courses. It's always a treat when cross disciplinary projects come together like this!


## Technologies Used
- Python
- SciKit Image (python library)
- Matplotlib (python library)


## Features
- Image Sharpening
- Image Blurring
- Increasing image contrast
- Brightness/dimming controls
- Tinting an entire image towards any color using the desired color's RGB values
- Converting color images into black and white images


## Project Status
> This project is in progress. Current next steps include improving efficiency and allowing users to select their own image files to apply filters to. 


## Acknowledgements
The sharpening and blurring portion of this project were incredibly satisfying and it would not have been possible without the online resources posted by Serena Yeung of Stanford University. 
