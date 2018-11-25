# <a href="#">Drip</a>

## Install on Chrome (For development)

* Download chrome-extension directory
* Go to "chrome://extensions
* Click "load unpacked extension"
* Choose the directory you downloaded it to (Make sure that "manifest.json" is located in this directory!)


## Quick documentation
* "popup.html" is the displayed view when the extension opens
* "popup.html" has a "capture region of screen function"
* "capture region of screen function" is defined in: "screenshot.js"
* "screenshot.js" calls a function named: 'load_cropper_without_selection()' 
* 'load_cropper_without_selection()' is located within "cropper.js"
* "cropper.js" creates a movable rectangle on the screen, and there is a "Save" button that saves the image within the rectangle.

* the save location can be change by defining "localStorage" variable in "background.js"
* (not sure if right) "background.js" contains definitions for "api" and "isEnableUrl", maybe this is how we can make our extension call the backend 


## Issues to solve
* The screenshot can be saved into the local computer, but we need it to send the image to our server/backend
* The "popup.html" page closes after completing the screenshot, but we want to display the search results within the "popup.html" page. Perhaps we can get the "popup.html" to become transparent instead of close, when doing the screenshot. If that approach doesn't work, we could open a new tab that receives search results.


## License

ISC License Copyright (c) 2018, <a href="#">Drip</a>

Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
